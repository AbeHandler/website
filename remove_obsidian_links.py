#!/usr/bin/env python3
"""
Obsidian Link Remover

This script removes Obsidian-style links from markdown files by replacing them
with their display text (the part after the | pipe character).

Usage:
    python obsidian_link_remover.py input_file.md

Examples:
    [[ROLEX A Novel Method|Kim et al. (2023)]] => Kim et al. (2023)
    [[Simple Link]] => Simple Link
    [[Link with|Display Text]] => Display Text
"""

import re
import sys
import argparse
from pathlib import Path


def remove_obsidian_links(text):
    """
    Remove Obsidian-style links from text.
    
    Replaces [[link|display]] with display text, or [[link]] with link text.
    
    Args:
        text (str): Input text containing Obsidian links
        
    Returns:
        str: Text with Obsidian links replaced
    """
    # Pattern to match [[link|display]] or [[link]]
    # Group 1: everything before | (if present)
    # Group 2: everything after | (if present)
    pattern = r'\[\[([^|\]]+)(?:\|([^\]]+))?\]\]'
    
    def replace_link(match):
        link_text = match.group(1).strip()
        display_text = match.group(2)
        
        # If there's display text (after |), use it
        if display_text:
            return display_text.strip()
        # Otherwise, use the link text itself
        else:
            return link_text
    
    return re.sub(pattern, replace_link, text)


def process_file(input_path):
    """
    Process a file to remove Obsidian links and print to console.
    
    Args:
        input_path (str or Path): Path to input file
    """
    input_path = Path(input_path)
    
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Read the input file
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Try with different encoding if UTF-8 fails
        with open(input_path, 'r', encoding='latin-1') as f:
            content = f.read()
    
    # Process the content
    processed_content = remove_obsidian_links(content)
    
    # Just print the processed content to console
    print(processed_content)


def main():
    parser = argparse.ArgumentParser(
        description="Remove Obsidian-style links from markdown files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python obsidian_link_remover.py document.md
  
Link transformations:
  [[ROLEX A Novel Method|Kim et al. (2023)]] => Kim et al. (2023)
  [[Simple Link]] => Simple Link
  [[Complex Link Name|Short Display]] => Short Display
        """
    )
    
    parser.add_argument('input_file', help='Input markdown file')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be changed without modifying files')
    
    args = parser.parse_args()
    
    try:
        if args.dry_run:
            # Show what would be changed
            with open(args.input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            processed = remove_obsidian_links(content)
            
            if content != processed:
                print("Changes that would be made:")
                print("-" * 50)
                
                # Find and show the differences
                import difflib
                diff = difflib.unified_diff(
                    content.splitlines(keepends=True),
                    processed.splitlines(keepends=True),
                    fromfile="BEFORE (with links)",
                    tofile="AFTER (links removed)"
                )
                print(''.join(diff))
            else:
                print("No Obsidian links found - no changes needed.")
        else:
            process_file(args.input_file)
            
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()