import os
import re
from pathlib import Path
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
import random
import logging
import sys
import yaml
from datetime import datetime
import shutil 
# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Download necessary NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Check and download spaCy model if not present
def download_spacy_model():
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        logging.info("Downloading spaCy model. This may take a few minutes...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    finally:
        nlp = spacy.load("en_core_web_sm")
    return nlp

# Load spaCy model
nlp = download_spacy_model()

def duplicate_content_folder(folder_path):
    parent_dir = os.path.dirname(folder_path)
    folder_name = os.path.basename(folder_path)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder_name = f"{folder_name}_backup_{timestamp}"
    backup_folder_path = os.path.join(parent_dir, backup_folder_name)
    
    shutil.copytree(folder_path, backup_folder_path)
    logging.info(f"Created backup of content folder: {backup_folder_path}")
    return backup_folder_path

def split_frontmatter(content):
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if frontmatter_match:
        frontmatter_raw = frontmatter_match.group(1)
        content = content[frontmatter_match.end():]
        
        # Parse frontmatter manually
        frontmatter = {}
        for line in frontmatter_raw.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                frontmatter[key.strip()] = value.strip()
    else:
        frontmatter = {}
    return frontmatter, content

def read_markdown_files(folder_path):
    markdown_files = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    frontmatter, markdown_content = split_frontmatter(content)
                    markdown_files[filename] = {
                        'content': markdown_content,
                        'frontmatter': frontmatter
                    }
            except Exception as e:
                logging.error(f"Error processing file {filename}: {str(e)}")
    logging.info(f"Read {len(markdown_files)} markdown files from {folder_path}")
    return markdown_files

def preprocess_text(text):
    # Remove code blocks, inline code, URLs
    text = re.sub(r'```[\s\S]*?```', '', text)
    text = re.sub(r'`[^`\n]+`', '', text)
    text = re.sub(r'http\S+', '', text)
    return text

def extract_keywords(content, frontmatter, num_keywords=20):
    # Prioritize tags from frontmatter
    declared_keywords = []
    if 'Tags' in frontmatter:
        declared_keywords = [tag.strip().lower() for tag in frontmatter['Tags'].split(',')]
    
    # Extract additional keywords from content
    processed_text = preprocess_text(content)
    doc = nlp(processed_text)
    
    keyword_candidates = []
    keyword_candidates.extend([chunk.text.lower() for chunk in doc.noun_chunks if len(chunk.text.split()) >= 3])
    keyword_candidates.extend([ent.text.lower() for ent in doc.ents if len(ent.text.split()) >= 3])
    
    vectorizer = TfidfVectorizer(ngram_range=(3, 5))  # Consider phrases of 3 to 5 words
    tfidf_matrix = vectorizer.fit_transform(keyword_candidates)
    feature_names = vectorizer.get_feature_names_out()
    dense = tfidf_matrix.todense()
    scores = dense.sum(axis=0).tolist()[0]
    scored_keywords = [(keyword, score) for keyword, score in zip(feature_names, scores)]
    
    sorted_keywords = sorted(scored_keywords, key=lambda x: x[1], reverse=True)
    extracted_keywords = [keyword for keyword, _ in sorted_keywords[:num_keywords]]
    
    # Combine declared and extracted keywords, prioritizing declared ones
    combined_keywords = declared_keywords + [kw for kw in extracted_keywords if kw not in declared_keywords]
    return combined_keywords[:num_keywords]

def find_relevant_links(markdown_files, keywords, num_links=10):
    relevant_links = {}
    
    for filename, file_data in markdown_files.items():
        relevant_links[filename] = []
        content = file_data['content'].lower()
        
        for other_filename, other_file_data in markdown_files.items():
            if filename != other_filename:
                other_slug = other_file_data['frontmatter'].get('Slug', '')
                for keyword in keywords[other_filename]:
                    if keyword.lower() in content and len(keyword.split()) >= 3:
                        relevant_links[filename].append((keyword, other_slug))
        
        random.shuffle(relevant_links[filename])  # Randomize to avoid always linking the same keywords
        relevant_links[filename] = relevant_links[filename][:num_links]
    
    logging.info(f"Found relevant links for {len(relevant_links)} files")
    return relevant_links

def create_seo_optimized_links(content, relevant_links, max_links=3):
    link_count = 0
    used_anchors = set()
    
    for keyword, slug in relevant_links:
        if link_count >= max_links:
            break
        
        # Ensure the keyword is not part of an existing link
        if re.search(rf'\[.*{re.escape(keyword)}.*\]', content, re.IGNORECASE):
            continue
        
        # Find the keyword in the content, ensuring it's not part of a larger word
        matches = list(re.finditer(rf'\b{re.escape(keyword)}\b', content, re.IGNORECASE))
        if matches and keyword not in used_anchors:
            match = random.choice(matches)  # Randomly choose one occurrence to link
            start, end = match.span()
            anchor_text = content[start:end]
            link = f'[{anchor_text}](/{slug})'
            content = content[:start] + link + content[end:]
            used_anchors.add(keyword)
            link_count += 1
            logging.info(f"Added link: {link}")
    
    return content

def update_markdown_files(folder_path, markdown_files, relevant_links):
    for filename, file_data in markdown_files.items():
        original_content = file_data['content']
        updated_content = create_seo_optimized_links(original_content, relevant_links[filename])
        
        if updated_content != original_content:
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                full_content = file.read()
            
            # Replace only the main content part, preserving frontmatter
            full_updated_content = re.sub(
                r'^---\n.*?\n---\n',
                lambda m: m.group(0) + updated_content,
                full_content,
                flags=re.DOTALL
            )
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(full_updated_content)
            logging.info(f"Updated {filename}")
        else:
            logging.info(f"No changes needed in {filename}")

def main(folder_path):
    logging.info(f"Starting improved SEO-optimized interlinking for folder: {folder_path}")
    
    # Create a backup of the content folder
    backup_folder = duplicate_content_folder(folder_path)
    logging.info(f"Backup created at: {backup_folder}")
    
    markdown_files = read_markdown_files(folder_path)
    logging.info(f"Found {len(markdown_files)} markdown files")
    
    keywords = {filename: extract_keywords(file_data['content'], file_data['frontmatter']) 
                for filename, file_data in markdown_files.items()}
    logging.info("Extracted keywords from all files")
    
    relevant_links = find_relevant_links(markdown_files, keywords)
    logging.info("Found relevant links between files")
    
    update_markdown_files(folder_path, markdown_files, relevant_links)
    logging.info("Improved SEO-optimized interlinking complete!")
    logging.info(f"Original content backed up at: {backup_folder}")

if __name__ == "__main__":
    folder_path = "/Users/tomyates/niche_sites/sites/christianity/content"
    main(folder_path)