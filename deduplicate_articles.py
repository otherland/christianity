import os
import shutil
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from difflib import SequenceMatcher

def preprocess_sentence(sentence):
    tokens = word_tokenize(sentence.lower())
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    return ' '.join(tokens)

def similarity_ratio(seq1, seq2):
    return SequenceMatcher(None, seq1, seq2).ratio()

def split_into_blocks(text):
    return re.split(r'\n\s*\n', text)

def analyze_repetition(text, similarity_threshold=0.8):
    blocks = split_into_blocks(text)
    preprocessed_blocks = [' '.join(preprocess_sentence(sent) for sent in sent_tokenize(block)) for block in blocks]
    
    similar_groups = []
    for i, block in enumerate(preprocessed_blocks):
        if not any(i in group for group in similar_groups):
            group = [i]
            for j in range(i+1, len(preprocessed_blocks)):
                if similarity_ratio(block, preprocessed_blocks[j]) > similarity_threshold:
                    group.append(j)
            if len(group) > 1:
                similar_groups.append(group)
    
    total_blocks = len(blocks)
    unique_blocks = total_blocks - sum(len(group) - 1 for group in similar_groups)
    repeated_blocks = total_blocks - unique_blocks
    repetition_rate = repeated_blocks / total_blocks if total_blocks > 0 else 0
    
    return similar_groups, blocks, total_blocks, unique_blocks, repeated_blocks, repetition_rate

def remove_near_duplicates(text, similarity_threshold=0.8):
    similar_groups, blocks = analyze_repetition(text, similarity_threshold)[:2]
    unique_blocks = []
    for i, block in enumerate(blocks):
        if not any(i in group[1:] for group in similar_groups):
            unique_blocks.append(block)
    return '\n\n'.join(unique_blocks)

def process_markdown_file(file_path, backup_dir, similarity_threshold=0.8):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Analyze original content
    similar_groups, blocks, total, unique, repeated, rate = analyze_repetition(content, similarity_threshold)
    
    print(f"\nProcessing: {file_path}")
    print(f"Original - Total blocks: {total}, Unique: {unique}, Repeated: {repeated}, Repetition rate: {rate:.2%}")
    
    # Remove near-duplicates
    deduped_content = remove_near_duplicates(content, similarity_threshold)
    
    # Analyze deduped content
    _, _, total_deduped, unique_deduped, repeated_deduped, rate_deduped = analyze_repetition(deduped_content, similarity_threshold)
    
    print(f"Deduped  - Total blocks: {total_deduped}, Unique: {unique_deduped}, Repeated: {repeated_deduped}, Repetition rate: {rate_deduped:.2%}")
    
    # Write deduped content back to file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(deduped_content)

def process_directory(directory_path, similarity_threshold=0.8):
    # Create backup directory
    backup_dir = directory_path + '_backup'
    if not os.path.exists(backup_dir):
        shutil.copytree(directory_path, backup_dir)
        print(f"Backup created at: {backup_dir}")
    else:
        print(f"Backup directory already exists at: {backup_dir}")
    
    # Process all markdown files
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_markdown_file(file_path, backup_dir, similarity_threshold)

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Set the path to your articles
articles_path = '/Users/tomyates/niche_sites/sites/christianity/content'

# Process the directory
process_directory(articles_path)

print("\nProcessing complete. Original files have been backed up and deduplicated versions saved.")