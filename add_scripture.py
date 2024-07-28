import re
import os

def get_bible_books():
    return (
        "Genesis|Exodus|Leviticus|Numbers|Deuteronomy|Joshua|Judges|Ruth|"
        "1 Samuel|2 Samuel|1 Kings|2 Kings|1 Chronicles|2 Chronicles|Ezra|Nehemiah|Esther|"
        "Job|Psalms|Psalm|Proverbs|Ecclesiastes|Song of Solomon|Isaiah|Jeremiah|Lamentations|Ezekiel|"
        "Daniel|Hosea|Joel|Amos|Obadiah|Jonah|Micah|Nahum|Habakkuk|Zephaniah|Haggai|Zechariah|"
        "Malachi|Matthew|Mark|Luke|John|Acts|Romans|1 Corinthians|2 Corinthians|Galatians|"
        "Ephesians|Philippians|Colossians|1 Thessalonians|2 Thessalonians|1 Timothy|2 Timothy|"
        "Titus|Philemon|Hebrews|James|1 Peter|2 Peter|1 John|2 John|3 John|Jude|Revelation"
    )

def add_scripture_hyperlink(match):
    full_reference = match.group(0)
    book = match.group(1).replace(" ", "-")
    chapter = match.group(2)
    verse = match.group(3)
    
    # Extract only the start verse if a range is given
    start_verse = verse.split('-')[0]
    
    url = f"https://www.bibleref.com/{book}/{chapter}/{book}-{chapter}-{start_verse}.html"
    return f"[{full_reference}]({url})"

def process_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if the content already contains links
    if '[' in content and '](' in content:
        print(f"Skipping {file_path} as it already contains links")
        return

    bible_books = get_bible_books()
    # Pattern to match Bible references not already in a link
    pattern = rf'\b({bible_books})\s(\d+):(\d+(?:-\d+)?)\b(?!\])'
    
    updated_content = re.sub(pattern, add_scripture_hyperlink, content, flags=re.IGNORECASE)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

def process_markdown_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path}")
                try:
                    process_markdown_file(file_path)
                    print(f"Successfully processed {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")

# Example usage
folder_path = "./content"
process_markdown_folder(folder_path)