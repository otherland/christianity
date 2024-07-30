import os
import re
import shutil
from datetime import datetime
from youtube_search import YoutubeSearch

def backup_directory(source_dir):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = f"{source_dir}_backup_{timestamp}"
    shutil.copytree(source_dir, backup_dir)
    print(f"Backup created: {backup_dir}")

def get_frontmatter(content):
    match = re.search(r'---\s*(.*?)\s*---', content, re.DOTALL)
    return match.group(1) if match else ''

def get_tags(frontmatter):
    match = re.search(r'Tags:\s*(.*)', frontmatter)
    return match.group(1).strip().split(', ') if match else []

def search_youtube(query):
    results = YoutubeSearch(query, max_results=1).to_dict()
    if results:
        return results[0]['id']
    return None

def create_embed(video_id):
    return f'\n<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>\n'

def insert_embed_before_last_heading(content, embed):
    # Find all level 2 headings
    headings = list(re.finditer(r'^##\s+.*$', content, re.MULTILINE))
    
    if headings:
        # Get the last heading
        last_heading = headings[-1]
        
        # Insert the embed before the last heading
        return content[:last_heading.start()] + embed + content[last_heading.start():]
    else:
        # If no headings found, append the embed to the end of the content
        return content + embed

def process_markdown_files(directory):
    markdown_files = [f for f in os.listdir(directory) if f.endswith('.md')]
    
    for index, filename in enumerate(markdown_files):
        if (index + 1) % 4 == 0:  # Process every 4th file
            filepath = os.path.join(directory, filename)
            
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            frontmatter = get_frontmatter(content)
            tags = get_tags(frontmatter)
            
            if tags:
                query = ' '.join(tags)
                video_id = search_youtube(query)
                
                if video_id:
                    embed = create_embed(video_id)
                    
                    # Insert the embed before the last heading
                    new_content = insert_embed_before_last_heading(content, embed)
                    
                    # Write the changes back to the file
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    
                    print(f'Added YouTube embed to {filename}')
                else:
                    print(f'No suitable video found for {filename}')
            else:
                print(f'No tags found in {filename}')
        else:
            print(f'Skipping {filename} (not every 4th file)')

if __name__ == '__main__':
    markdown_directory = '/Users/tomyates/niche_sites/sites/christianity/content'
    
    # Create a backup before processing
    backup_directory(markdown_directory)
    
    # Process the markdown files
    process_markdown_files(markdown_directory)