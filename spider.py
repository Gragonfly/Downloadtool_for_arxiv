import requests
from bs4 import BeautifulSoup

# 替换为您要爬取的 arXiv 搜索结果页面链接
url = 'https://arxiv.org/search/?query=Carla&searchtype=abstract&abstracts=hide&order=-announced_date_first&size=50&date-date_type=submitted_date&start=500'

# 获取页面内容
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 打开文件以写入模式保存链接
with open('arxiv_abs_links2.txt', 'a') as file:
    # 找到所有包含类名 'arxiv-result' 的项目
    results = soup.find_all('li', class_='arxiv-result')
    
    # 遍历每个结果，并提取其中的符合条件的链接
    for result in results:
        abs_link = result.find('a', href=True)
        if abs_link and 'https://arxiv.org/abs' in abs_link['href']:
            # 写入链接到文件中
            file.write(abs_link['href'] + '\n')

print("包含 'https://arxiv.org/abs' 的链接已成功保存到 arxiv_abs_links.txt 文件中。")

