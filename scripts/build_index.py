#!/usr/bin/env python3
"""
Script to generate index.json for blog posts by scanning markdown files
"""
import json
import os
import re
import yaml
from datetime import datetime
from pathlib import Path

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content"""
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if frontmatter_match:
        frontmatter_yaml = frontmatter_match.group(1)
        markdown_content = frontmatter_match.group(2)
        frontmatter = yaml.safe_load(frontmatter_yaml)
        return frontmatter, markdown_content
    else:
        # If no frontmatter found, return empty dict
        return {}, content

def get_file_modification_time(file_path):
    """Get the modification time of a file"""
    if os.path.exists(file_path):
        mod_timestamp = os.path.getmtime(file_path)
        return datetime.fromtimestamp(mod_timestamp).strftime('%Y-%m-%d')
    else:
        return datetime.now().strftime('%Y-%m-%d')

def get_category_from_path(file_path):
    """Extract category and subcategory from file path"""
    path_parts = file_path.split('/')
    if len(path_parts) >= 2:
        category = path_parts[0]
        if len(path_parts) >= 3:
            subcategory = path_parts[1]
        else:
            subcategory = ""
    else:
        category = ""
        subcategory = ""

    return category, subcategory

def generate_blog_index():
    # Walk through all markdown files in the repository
    markdown_files = []
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories and scripts directory
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'scripts']
        for file in files:
            if file.endswith('.md') and file != 'README.md':  # Exclude README.md
                file_path = os.path.join(root, file)
                if file_path.startswith('./'):  # Remove leading ./
                    file_path = file_path[2:]
                markdown_files.append(file_path)

    index_data = []
    for file_path in markdown_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter, markdown_content = extract_frontmatter(content)

        # Only include posts that have publish: true in frontmatter or no publish field
        if frontmatter.get('publish', True) is False:
            continue

        # Extract information from frontmatter
        title = frontmatter.get('title', '')
        date = frontmatter.get('date', get_file_modification_time(file_path))
        tags = frontmatter.get('tags', [])
        description = frontmatter.get('description', '')

        # Determine category and subcategory from path
        category, subcategory = get_category_from_path(file_path)

        # Create raw URL for the post
        raw_url = f"https://raw.githubusercontent.com/study-overflow/vault-overflow/main/{file_path.replace('./', '')}"

        # Create index entry
        index_entry = {
            "title": title,
            "file": file_path,
            "date": str(date),
            "tags": tags,
            "description": description,
            "category": category,
            "subcategory": subcategory,
            "raw_url": raw_url
        }

        index_data.append(index_entry)

    # Sort by date (newest first)
    index_data.sort(key=lambda x: x['date'], reverse=True)

    # Write index.json
    with open('index.json', 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    print(f"Generated index.json with {len(index_data)} blog posts")

if __name__ == "__main__":
    generate_blog_index()