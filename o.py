import os

def generate_pdf_list_html(subfolder_path):
    # 修改为使用 h3 标签
    html_content = '<ul style="list-style-type: none; margin: 0; padding: 0;">\n'
    for item in sorted(os.listdir(subfolder_path)):
        if item.lower().endswith('.pdf'):
            file_name_without_extension = item.rsplit('.', 1)[0]
            html_content += f'<li style="line-height: 1;"><h3><a href="{item}">{file_name_without_extension}</a></h3></li>\n'
    html_content += '</ul>\n'
    return html_content

def generate_subfolder_index_html(subfolder_path, root_folder):
    folder_name = os.path.basename(subfolder_path)
    pdf_list_html = generate_pdf_list_html(subfolder_path)
    root_relative_path = os.path.relpath(root_folder, start=subfolder_path)
    
    html_str = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{folder_name}</title>
    <style>
        * {{ margin: 10; padding: 10; }}
        body {{ font-family: Arial, sans-serif; font-size: 20px; }}
        .absoluteCenter {{ width: 900px; height: 600px; position: absolute; left: 50%; top: 10%; margin-left: -450px; }}
        a {{ text-decoration: none; color: black; }}
        a:hover {{ text-decoration: underline; }}
        h3 {{ font-size: 20px; }} /* 确保 h3 标签的字体大小适用 */
    </style>
</head>
<body>
    <div class="absoluteCenter">
        <h2>{folder_name}</h2>
        {pdf_list_html}
    </div>
</body>
</html>"""
    index_html_path = os.path.join(subfolder_path, 'index.html')
    with open(index_html_path, 'w', encoding='utf-8') as f:
        f.write(html_str)

def generate_root_index_html(root_folder):
    html_str = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Ref</title>
    <style>
        * {{ margin: 10; padding: 10; }}
        body {{ font-family: Arial, sans-serif; font-size: 20px; }}
        .absoluteCenter {{ width: 900px; height: 600px; position: absolute; left: 50%; top: 10%; margin-left: -450px; }}
        a {{ text-decoration: none; color: black; }}
        a:hover {{ text-decoration: underline; }}
        h3 {{ font-size: 20px; }} /* 确保 h3 标签的字体大小适用 */
    </style>
</head>
<body>
    <div class="absoluteCenter">
        
        <h2>Ref Directory</h2>
        """

    for first_level_folder in sorted(os.listdir(root_folder)):
        if os.path.isdir(os.path.join(root_folder, first_level_folder)) and first_level_folder != ".git":
            first_level_path = os.path.join(root_folder, first_level_folder)
            subfolders = [f for f in sorted(os.listdir(first_level_path)) if os.path.isdir(os.path.join(first_level_path, f)) and f != ".git"]
            for subfolder in subfolders:
                generate_subfolder_index_html(os.path.join(first_level_path, subfolder), root_folder)  # Generate index.html for each subfolder
                
            subfolder_links = [f'<a href="{os.path.join(first_level_folder, f, "index.html")}">{f}</a>' for f in subfolders]
            subfolder_str = " - ".join(subfolder_links)
            html_str += f'<h3>{first_level_folder}: {subfolder_str}</h3>\n'
    
    html_str += "</div>\n</body>\n</html>"

    index_html_path = os.path.join(root_folder, 'index.html')
    with open(index_html_path, 'w', encoding='utf-8') as f:
        f.write(html_str)

current_folder_path = os.getcwd()
generate_root_index_html(current_folder_path)
