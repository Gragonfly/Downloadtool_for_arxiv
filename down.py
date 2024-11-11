import requests
import os

# 定义包含链接的文件路径和PDF保存的文件夹
link_file = 'arxiv_abs_links.txt'  # 包含论文链接的txt文件
output_folder = 'arxiv_papers'  # PDF文件存储的文件夹

# 创建存储文件夹（如果不存在）
os.makedirs(output_folder, exist_ok=True)

# 从txt文件中逐行读取链接并下载PDF
with open(link_file, 'r') as file:
    for line in file:
        url = line.strip()  # 去掉行末的换行符和空格
        if url and url.startswith('https://arxiv.org/abs/'):
            # 将链接中的 'abs' 替换为 'pdf' 以获得 PDF 下载链接
            pdf_url = url.replace('abs', 'pdf')
            paper_id = url.split('/')[-1]  # 获取论文ID作为文件名
            pdf_path = os.path.join(output_folder, f'{paper_id}.pdf')

            if os.path.exists(pdf_path):
                print(f"已存在，跳过下载: {pdf_path}")
                continue
            
            # 下载PDF并保存
            try:
                response = requests.get(pdf_url)
                response.raise_for_status()  # 检查请求是否成功
                with open(pdf_path, 'wb') as pdf_file:
                    pdf_file.write(response.content)
                print(f"已成功下载: {pdf_path}")
            except requests.exceptions.RequestException as e:
                print(f"下载失败: {pdf_url} - {e}")

print("所有下载任务已完成。")

