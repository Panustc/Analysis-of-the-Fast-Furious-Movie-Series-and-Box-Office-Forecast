import requests
from bs4 import BeautifulSoup
from snownlp import SnowNLP

movie_id = '25728006'

# 一共爬取的页数
pages = 5

# 构造请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

for page_num in range(pages):
    # 构造 URL
    url = f'https://movie.douban.com/subject/{movie_id}/comments?start={page_num * 20}&limit=20&sort=new_score&status=P'

    # 发送请求并解析 HTML 页面
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有评论所在的 div 标签
    comments_divs = soup.find_all('div', class_='comment-item')

    # 遍历每个评论，提取出评分和评论内容，并进行情感分析
    for comment_div in comments_divs:
        rating_span = comment_div.find('span', class_='comment-info').find_all('span')[1]
        rating = rating_span['class'][0][7]  # 评分为 1-5 星，对应 class 为 rating1-5
        comment = comment_div.find('span', class_='short').text

        # 判断评论长度是否大于等于50
        if len(comment) >= 50:
            s = SnowNLP(comment)
            sentiment_score = s.sentiments
            print(f'评分：{rating}，评论：{comment}，情感分值：{sentiment_score}')
