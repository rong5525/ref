import os

def generate_index_html(folder_path):
    html_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>文件夹内容索引</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f7f8fa;
            color: #333;
            padding: 20px;
            font-size: 16px;
        }
        .folder-row {
            margin-bottom: 10px;
        }
        .folder-name {
            font-weight: bold;
            color: #ff6b00;
        }
        .pdf-link {
            margin-left: 10px;
            color: #000;
            text-decoration: none;
        }
        .pdf-link:hover {
            text-decoration: underline;
        }
        .separator {
            color: #ff6b00;
            margin: 0 5px;
        }
    </style>
</head>
<body>
"""

    # 遍历文件夹内的子文件夹
    for folder_name in sorted(os.listdir(folder_path)):
        subfolder_path = os.path.join(folder_path, folder_name)
        if os.path.isdir(subfolder_path):  # 确认是文件夹
            html_str += f'<div class="folder-row"><span class="folder-name">{folder_name}</span>'
            # 遍历子文件夹内的PDF文件
            first_file = True
            for file_name in sorted(os.listdir(subfolder_path)):
                if file_name.lower().endswith('.pdf'):
                    if not first_file:
                        html_str += f'<span class="separator">-</span>'
                    else:
                        first_file = False
                    file_path = os.path.join(folder_name, file_name)
                    html_str += f'<a href="{file_path}" class="pdf-link" target="_blank">{file_name}</a>'
            html_str += '</div>\n'

    # 结束HTML字符串
    html_str += """
</body>
</html>
"""

    # 写入HTML文件
    index_html_path = os.path.join(folder_path, 'index.html')
    with open(index_html_path, 'w', encoding='utf-8') as f:
        f.write(html_str)

    # 输出生成的HTML文件路径
    return index_html_path

# 使用示例：
# 假设你的文件夹路径是'C:/path/to/your/folder'
import os
folder_path = os.getcwd()
index_html_path = generate_index_html(folder_path)
print(f"Generated HTML file at: {index_html_path}")
