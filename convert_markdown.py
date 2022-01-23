from importlib_metadata import pathlib
from markdown2 import Markdown


# read the markdown input file
md_file = pathlib.Path.cwd() / 'sample_markdown.md'

# define an output file saved in the cwd
output_file = pathlib.Path.cwd() / 'output.html'

# read markdown file
with open(md_file) as f:
    markdown_content = f.readlines()

# convert markdown to html
markdowner = Markdown()
html_output = markdowner.convert(''.join(markdown_content))

# write the result to the output file
output_file.write_text(html_output)

print(html_output)