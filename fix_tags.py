import os
import re

def fix_numeric_tags(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Look for tags block
                if "tags:" in content:
                    # Regex to find numeric list items in yaml frontmatter
                    # Pattern looks for "  - 0.25" or "  - 0.5" etc. and quotes them
                    # We simple look for hyphens followed by space and then a number (int or float) at end of line
                    new_content = re.sub(r'^(\s*-\s+)([0-9]+(\.[0-9]+)?)\s*$', r'\1"\2"', content, flags=re.MULTILINE)
                    
                    if content != new_content:
                        print(f"Fixing numeric tags in {filepath}")
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(new_content)

if __name__ == "__main__":
    fix_numeric_tags("docs")
