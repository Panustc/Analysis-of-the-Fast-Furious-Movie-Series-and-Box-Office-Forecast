import requests
from bs4 import BeautifulSoup
from snownlp import SnowNLP
import pandas as pd
import matplotlib.pyplot as plt

movie_id = '35766491'

# 一共爬取的页数
pages = 15

# 构造请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 存储情感分值和评分数据
sentiment_scores = []
ratings = []

# 爬取数据
for page_num in range(pages):
    # 构造 URL
    url = f'https://movie.douban.com/subject/{movie_id}/comments?start={page_num * 20}&limit=20&sort=new_score&status=P'

    # 发送请求并解析 HTML 页面
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有评论所在的 div 标签
    comments_divs = soup.find_all('div', class_='comment-item')

    for comment_div in comments_divs:
        rating_span = comment_div.find('span', class_='comment-info').find_all('span')[1]
        rating = rating_span['class'][0][7]  # 评分为 1-5 星，对应 class 为 rating1-5
        comment = comment_div.find('span', class_='short').text
        s = SnowNLP(comment)
        sentiment_score = s.sentiments

    # 判断评论长度是否大于等于50，且评分为数字
        if len(comment) >= 10 and rating.isdigit():
            sentiment_scores.append(sentiment_score)
            ratings.append(int(rating))
# 将数据转化为DataFrame格式
data = pd.DataFrame({'Sentiment Score': sentiment_scores, 'Rating': ratings})

# 绘制散点图
plt.scatter(data['Rating'], data['Sentiment Score'], alpha=0.5)
plt.xlabel('Rating')
plt.ylabel('Sentiment Score')
plt.title('Relationship between Sentiment Score and Rating')

# 显示图像
plt.show()
