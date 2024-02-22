import os

def generate_pdf_list_html(subfolder_path):
    html_content = '<ul style="list-style-type: none; margin: 0; padding: 0;"><h2>\n'
    for item in sorted(os.listdir(subfolder_path)):
        if item.lower().endswith('.pdf'):
            file_name_without_extension = item.rsplit('.', 1)[0]
            html_content += f'<h2><li style="line-height: 2;"><a href="{item}">{file_name_without_extension}</a></li></h2>\n'
    html_content += '</h2></ul>\n'
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
    </style>
</head>
<body>
    <div class="absoluteCenter">
        <h1>{folder_name}</h1>\n<h2>
        {pdf_list_html}\n</h2>
        
    </div>
</body>
</html>"""
    index_html_path = os.path.join(subfolder_path, 'index.html')
    with open(index_html_path, 'w', encoding='utf-8') as f:
        f.write(html_str)

def generate_root_index_html(root_folder):
    html_str = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Ref</title>
    <style>
        * {{ margin: 10; padding: 10; }}
        .absoluteCenter {{ width: 900px; height: 600px; position: absolute; left: 50%; top: 10%; margin-left: -450px; }}
        body {{ font-family: Arial, sans-serif; font-size: 20px; }}
        a {{ text-decoration: none; color: black; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <div class="absoluteCenter">
        <h1>Roy</h1>
       <h1>Ref Directory</h1>\n<h2><ol>
        <font style="line-height:2;">\n"""
    
    for first_level_folder in sorted(os.listdir(root_folder)):
        if os.path.isdir(os.path.join(root_folder, first_level_folder)) and first_level_folder != ".git":
            first_level_path = os.path.join(root_folder, first_level_folder)
            subfolders = [f for f in sorted(os.listdir(first_level_path)) if os.path.isdir(os.path.join(first_level_path, f)) and f != ".git"]
            subfolder_links = [f'<a href="{os.path.join(first_level_folder, f, "index.html")}">{f}</a>' for f in subfolders]
            subfolder_str = " - ".join(subfolder_links)
            html_str += f'<div class="folder-row"><span class="folder-name">{first_level_folder}: </span>{subfolder_str}</div>\n'
    
    html_str += "</font></ol></h2></div></body>\n</html>"


    index_html_path = os.path.join(root_folder, 'index.html')
    with open(index_html_path, 'w', encoding='utf-8') as f:
        f.write(html_str)

current_folder_path = os.getcwd()
generate_root_index_html(current_folder_path)
