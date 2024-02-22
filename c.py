import os

def generate_pdf_list_html(subfolder_path):
    """
    生成二级子文件夹的PDF列表HTML。
    """
    html_content = '<ul style="list-style-type: none; padding-left: 0;">\n'
    for item in sorted(os.listdir(subfolder_path)):
        if item.lower().endswith('.pdf'):
            html_content += f'  <li><a href="{item}" target="_blank" style="text-decoration: none; color: #333;">{item}</a></li>\n'
    html_content += '</ul>\n'
    return html_content

def generate_subfolder_index_html(subfolder_path):
    """
    为二级子文件夹生成index.html。
    """
    folder_name = os.path.basename(subfolder_path)
    pdf_list_html = generate_pdf_list_html(subfolder_path)
    
    html_str = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{folder_name}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 18px;
            background-color: #f7f8fa;
            color: #333;
            padding: 20px;
        }}
    </style>
</head>
<body>
    <h1 style="font-size: 24px; color: #ff6b00;">{folder_name}</h1>
    {pdf_list_html}
</body>
</html>"""

    index_html_path = os.path.join(subfolder_path, 'index.html')
    with open(index_html_path, 'w', encoding='utf-8') as f:
        f.write(html_str)

def generate_root_index_html(root_folder):
    """
    为根文件夹生成index.html。
    """
    html_str = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>索引页面</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 18px;
            background-color: #f7f8fa;
            color: #333;
            padding: 20px;
        }
        .folder-row {
            margin-bottom: 10px;
        }
        .folder-name {
            font-size: 24px;
            color: #ff6b00;
        }
        .subfolder-link {
            margin-left: 20px;
            font-size: 18px;
            text-decoration: none;
            color: #333;
        }
        .subfolder-link:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1 style="font-size: 30px;">索引页面</h1>\n"""

    for first_level_folder in sorted(os.listdir(root_folder)):
        first_level_path = os.path.join(root_folder, first_level_folder)
        if os.path.isdir(first_level_path):
            html_str += f'  <div class="folder-row"><span class="folder-name">{first_level_folder}</span>\n'
            for second_level_folder in sorted(os.listdir(first_level_path)):
                second_level_path = os.path.join(first_level_path, second_level_folder)
                if os.path.isdir(second_level_path):
                    generate_subfolder_index_html(second_level_path)
                    second_level_relative_path = os.path.relpath(second_level_path, start=root_folder)
                    html_str += f'  <a href="{os.path.join(second_level_relative_path, "index.html")}" class="subfolder-link">{second_level_folder}</a>\n'
            html_str += '  </div>\n'

    html_str += "</body>\n</html>"

    index_html_path = os.path.join(root_folder, 'index.html')
    with open(index_html_path, 'w', encoding='utf-8') as f:
        f.write(html_str)

# 获取Python脚本所在的目录路径
current_folder_path = os.getcwd()

# 调用函数生成主索引页面
generate_root_index_html(current_folder_path)
