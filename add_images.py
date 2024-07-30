import os
import re
import random
from pathlib import Path

def get_image_from_frontmatter(content):
    match = re.search(r'Image:\s*(.*)', content)
    return match.group(1).strip() if match else None

def add_image_to_frontmatter(content, image):
    if 'Image:' in content:
        return re.sub(r'(Image:).*', f'\\1 {image}', content)
    else:
        return content.replace('---\n', f'---\nImage: {image}\n', 1)

def process_markdown_files():
    content_dir = Path('/Users/tomyates/niche_sites/sites/christianity/content')
    unused_images_dir = Path('/Users/tomyates/Desktop/bible_unused')
    
    unused_images = list(unused_images_dir.glob('*'))
    files_processed = 0

    for md_file in content_dir.glob('**/*.md'):
        with open(md_file, 'r') as f:
            content = f.read()
        
        if not get_image_from_frontmatter(content):
            if not unused_images:
                print("Ran out of unused images!")
                break
            
            new_image = random.choice(unused_images)
            unused_images.remove(new_image)
            
            relative_path = f'images/{new_image.name}'
            updated_content = add_image_to_frontmatter(content, relative_path)
            
            with open(md_file, 'w') as f:
                f.write(updated_content)
            
            # Move the image to the content/images directory
            dest_path = content_dir / 'images' / new_image.name
            new_image.rename(dest_path)
            
            print(f"Added image {new_image.name} to {md_file}")
            files_processed += 1

    print(f"Processed {files_processed} files")
    print(f"Remaining unused images: {len(unused_images)}")

if __name__ == "__main__":
    process_markdown_files()