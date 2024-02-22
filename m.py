import os

def generate_pdf_list_html(subfolder_path):
    html_content = '<ul class="pdf-list">\n'
    for item in sorted(os.listdir(subfolder_path)):
        if item.lower().endswith('.pdf'):
            file_name_without_extension = item.rsplit('.', 1)[0]
            html_content += f'  <li><a href="{item}">{file_name_without_extension}</a></li>\n'
    html_content += '</ul>\n'
    return html_content

def generate_subfolder_index_html(subfolder_path, root_folder):
    folder_name = os.path.basename(subfolder_path)
    pdf_list_html = generate_pdf_list_html(subfolder_path)
    root_relative_path = os.path.relpath(root_folder, start=subfolder_path)
    
    html_str = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{folder_name}</title>
    <style>
        body {{
            font-family: 'Helvetica', 'Arial', sans-serif;
            font-size: 20px; /* Updated font size */
            color: #333;
            background-color: #fff;
            margin: 0;
            padding: 20px;
        }}
        ul.pdf-list {{
            list-style-type: disc;
            margin: 0;
            padding-left: 20px;
        }}
        ul.pdf-list li {{
            margin: 5px 0;
        }}
        a {{
            color: #333;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .return-link {{
            display: block;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <a href="{root_relative_path}/index.html" class="return-link">← Back to Ref</a>
    <h1>{folder_name}</h1>
    {pdf_list_html}
</body>
</html>"""
    index_html_path = os.path.join(subfolder_path, 'index.html')
    with open(index_html_path, 'w', encoding='utf-8') as f:
        f.write(html_str)

def generate_root_index_html(root_folder):
    html_str = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ref Directory</title>
    <style>
        body {{
            font-family: 'Helvetica', 'Arial', sans-serif;
            font-size: 20px; /* Updated font size */
            color: #333;
            background-color: #fff;
            margin: 0;
            padding: 20px;
        }}
        .folder-row {{
            margin-bottom: 15px;
        }}
        .folder-name {{
            font-weight: bold;
            font-size: 22px; /* Slightly larger for hierarchy */
        }}
        a {{
            color: #333;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <h1>Ref Directory</h1>\n"""

    for first_level_folder in sorted(os.listdir(root_folder)):
        if os.path.isdir(os.path.join(root_folder, first_level_folder)) and first_level_folder != ".git":
            first_level_path = os.path.join(root_folder, first_level_folder)
            subfolders = [f for f in sorted(os.listdir(first_level_path)) if os.path.isdir(os.path.join(first_level_path, f)) and f != ".git"]
            if subfolders:
                subfolder_links = [f'<a href="{os.path.join(first_level_folder, f, "index.html")}">{f}</a>' for f in subfolders]
                subfolder_str = " - ".join(subfolder_links)
                html_str += f'<div class="folder-row"><span class="folder-name">{first_level_folder}: </span>{subfolder_str}</div>\n'
            else:
                html_str += f'<div class="folder-row"><span class="folder-name">{first_level_folder}</span></div>\n'
    
    html_str += "</body>\n</html>"

    index_html_path = os.path.join(root_folder, 'index.html')
    with open(index_html_path, 'w', encoding='utf-8') as f:
        f.write(html_str)

current_folder_path = os.getcwd()
generate_root_index_html(current_folder_path)
