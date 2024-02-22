import os

def generate_pdf_list_html(subfolder_path):
    html_content = '<ul style="list-style-type: none; padding-left: 0;">\n'
    for item in sorted(os.listdir(subfolder_path)):
        if item.lower().endswith('.pdf'):
            file_name_without_extension = item.rsplit('.', 1)[0]
            html_content += f'<li><a href="{item}" style="text-decoration: none; color: #333;">{file_name_without_extension}</a></li>\n'
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
            font-family: Arial, sans-serif;
            font-size: 22px; /* Updated to match root page size */
            background-color: #f7f8fa;
            color: #333;
            padding: 20px;
        }}
        ul {{
            padding-left: 20px;
        }}
        a {{
            text-decoration: none;
            color: #333;
        }}
        a.return {{
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <a href="{root_relative_path}/index.html" class="return">Ref</a> - <span>{folder_name}</span>
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
    <title>Ref</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            font-size: 22px;
            background-color: #f7f8fa;
            color: #333;
            padding: 20px;
            margin-left: 50px;
        }}
        .folder-row {{
            margin-bottom: 15px;
        }}
        .folder-name {{
            font-weight: bold;
        }}
        .subfolder-link {{
            text-decoration
none;
color: #333;
}}
.subfolder-link:not(:last-child)::after {{
content: " - ";
white-space: nowrap; /* Prevent wrapping */
}}
</style>

</head>
<body>
    <h2>Ref</h2>\n"""
    for first_level_folder in sorted(os.listdir(root_folder)):
        if os.path.isdir(os.path.join(root_folder, first_level_folder)) and first_level_folder != ".git":
            html_str += f'  <div class="folder-row"><span class="folder-name">{first_level_folder}</span>\n'
            subfolder_path = os.path.join(root_folder, first_level_folder)
            subfolders = [f for f in sorted(os.listdir(subfolder_path)) if os.path.isdir(os.path.join(subfolder_path, f)) and f != ".git"]
            subfolder_links = []
            for second_level_folder in subfolders:
                second_level_path = os.path.join(subfolder_path, second_level_folder)
                generate_subfolder_index_html(second_level_path, root_folder)
                second_level_relative_path = os.path.relpath(second_level_path, start=root_folder)
                subfolder_links.append(f'<a href="{os.path.join(second_level_relative_path, "index.html")}" class="subfolder-link">{second_level_folder}</a>')
            # Ensure only a single space and dash between names
            html_str += ' - '.join(subfolder_links).replace(' - ', ' - ') + '</div>\n'
    html_str += "</body>\n</html>"
    index_html_path = os.path.join(root_folder, 'index.html')
    with open(index_html_path, 'w', encoding='utf-8') as f:
        f.write(html_str)
current_folder_path = os.getcwd()
generate_root_index_html(current_folder_path)