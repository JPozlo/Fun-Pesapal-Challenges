import markdown

# Read the contents of the Markdown file and uses the 'markdown' module to convert to HTML text
with open('test_markdown.md', 'r') as f:
    md_text = f.read()
    html_text = markdown.markdown(md_text)

# Write the converted HTML text into a HTML file within the same directory
with open('test_html.html', 'w') as f:
    f.write(html_text)
