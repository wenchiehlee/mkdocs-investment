import os
import glob
import yaml
from pymdownx.slugs import slugify

def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    - filter: a decorator function, to declare a filter.
    """

    @env.macro
    def render_categories():
        """
        Scans docs/blog/posts/*.md for categories and renders a list.
        """
        # Adjust path if necessary. valid for running 'mkdocs serve' from root
        base_path = os.path.join("docs", "blog", "posts")
        categories = {}
        
        files = glob.glob(os.path.join(base_path, "*.md"))
        print(f"Scanning {len(files)} files for categories...")

        for filename in files:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if content.startswith('---'):
                try:
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        frontmatter = parts[1]
                        metadata = yaml.safe_load(frontmatter)
                        
                        if metadata and 'categories' in metadata:
                            cats = metadata['categories']
                            if cats:
                                if isinstance(cats, list):
                                    for cat in cats:
                                        if cat:
                                            categories[cat] = categories.get(cat, 0) + 1
                                elif isinstance(cats, str):
                                    categories[cats] = categories.get(cats, 0) + 1
                except Exception as e:
                    print(f"Error parsing frontmatter in {filename}: {e}")
                    continue

        if not categories:
            return "No categories found."

        output = []
        # Sort by category name
        sorted_cats = sorted(categories.items())
        
        # Create slugifier function matching default mkdocs-material behavior
        # usually it's simple lowercase for ascii
        slugifier = slugify(case="lower")

        for cat, count in sorted_cats:
            slug = slugifier(cat, '-')
            # Link format: ../blog/category/<slug>/
            # Using HTML to bypass MkDocs 'unrecognized relative link' validation for virtual pages
            url = f"../blog/category/{slug}/"
            output.append(f"<li><a href=\"{url}\">{cat}</a> ({count})</li>")
            
        return "<ul>" + "\n".join(output) + "</ul>"
