import os
import random
from datetime import datetime, timedelta
import yaml
import markdown

# Directory containing markdown files
MARKDOWN_DIR = './content'

# Function to generate a random date within the last 6 months
def random_date_within_last_6_months():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=180)
    return start_date + (end_date - start_date) * random.random()

# Function to update the date in the front matter of a markdown file
def update_front_matter_date(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Split front matter and markdown content
    parts = content.split('---')
    if len(parts) < 3:
        return
    
    front_matter = parts[1]
    md_content = '---'.join(parts[2:])

    # Load front matter as a dictionary
    front_matter_data = yaml.safe_load(front_matter)

    # Update the date in the front matter
    random_date = random_date_within_last_6_months()
    front_matter_data['date'] = random_date.strftime('%Y-%m-%d')

    # Convert front matter back to YAML
    updated_front_matter = yaml.dump(front_matter_data, default_flow_style=False)

    # Write updated content back to the file
    with open(file_path, 'w') as file:
        file.write('---\n')
        file.write(updated_front_matter)
        file.write('---\n')
        file.write(md_content)

# Iterate through all markdown files in the directory
for filename in os.listdir(MARKDOWN_DIR):
    if filename.endswith('.md'):
        file_path = os.path.join(MARKDOWN_DIR, filename)
        update_front_matter_date(file_path)

print("Dates updated successfully.")