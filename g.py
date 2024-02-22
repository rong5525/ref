import os

def generate_pdf_list_html(subfolder_path):
    html_content = '<ul>\n'
    for item in sorted(os.listdir(subfolder_path)):
        if item.lower().endswith('.pdf'):
            file_name_without_extension = item.rsplit('.', 1)[0]
            html_content += f'<li><a href="{item}">{file_name_without_extension}</a></li>\n'
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
        body, a {{
            font-family: Arial, sans-serif;
            font-size: 22px;
            background-color: #f7f8fa;
            color: #333;
            padding: 20px;
            text-decoration: none;
        }}
        ul {{
            list-style-type: none; 
            padding-left: 0;
        }}
        li {{
            padding-bottom: 5px;
        }}
    </style>
</head>
<body>
    <a href="{root_relative_path}/index.html" style="font-weight: bold;">Ref</a> - <span>{folder_name}</span>
    {pdf_list_html}
</body>
</html>"""
    index_html_path = os.path.join(subfolder_path, 'index.html')
    with open(index_html_path, 'w', encoding='utf-8') as f:
        f.write(html_str)

def generate_root_index_html(root_folder):
    html_str = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ref</title>
    <style>
        body, a {{
            font-family: Arial, sans-serif;
            font-size: 22px;
            background-color: #f7f8fa;
            color: #333;
            padding: 20px;
            text-decoration: none;
        }}
        .folder-row {{
            margin-bottom: 15px;
        }}
        .folder-name {{
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h1>Ref</h1>\n"""
    for first_level_folder in sorted(os.listdir(root_folder)):
        first_level_path = os.path.join(root_folder, first_level_folder)
        if os.path.isdir(first_level_path) and first_level_folder != ".git":
            html_str += f'<div class="folder-row"><span class="folder-name">{first_level_folder}:</span>\n'
            subfolders = [f for f in sorted(os.listdir(first_level_path)) if os.path.isdir(os.path.join(first_level_path, f)) and f != ".git"]
            for second_level_folder in subfolders:
                second_level_path = os.path.join(first_level_path, second_level_folder)
                generate_subfolder_index_html(second_level_path, root_folder)
                second_level_relative_path = os.path.relpath(second_level_path, start=root_folder)
                html_str += f'<a href="{os.path.join(second_level_relative_path, "index.html")}">{second_level_folder}</a> - '
            html_str = html_str.rstrip(' - ')  # Remove the trailing separator
            html_str += '</div>\n'
    html_str += "</body>\n</html>"
    index_html_path = os.path.join(root_folder, 'index.html')
    with open(index_html_path, 'w', encoding='utf-8') as f:
        f.write(html_str)

# 获取当前工作目录
current_folder_path = os.getcwd()
# 生成主索引页面
generate_root_index_html(current_folder_path)
