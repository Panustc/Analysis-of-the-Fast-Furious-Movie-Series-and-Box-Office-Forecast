import requests
from bs4 import BeautifulSoup
import jieba
from wordcloud import WordCloud

movie_id = '1304899'

# 一共爬取的页数
pages = 20

# 构造请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 存储所有评论的文本
comments_text = ''

for page_num in range(pages):
    # 构造 URL
    url = f'https://movie.douban.com/subject/{movie_id}/comments?start={page_num * 20}&limit=20&sort=new_score&status=P'

    # 发送请求并解析 HTML 页面
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有评论所在的 div 标签
    comments_divs = soup.find_all('div', class_='comment-item')

    # 遍历每个评论，提取出评论文本
    for comment_div in comments_divs:
        comment = comment_div.find('span', class_='short').text
        comments_text += comment

# 使用 jieba 进行中文分词
words = jieba.lcut(comments_text)

# 过滤掉长度小于 2 的词语
words = [word for word in words if len(word) >= 2]

# 拼接词语为字符串
words_text = ' '.join(words)

# 制作词云图
wc = WordCloud(width=800, height=600, background_color='white', font_path='msyh.ttc')
wc.generate(words_text)
wc.to_file('速度与激情1豆瓣评论云图.png')
print('词云图制作完成！')
