import csv
import requests
from bs4 import BeautifulSoup

movie_id = '1304899'
pages = 5
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 创建CSV文件并写入表头
with open('豆瓣评论.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['评分', '评论'])

    for page_num in range(pages):
        url = f'https://movie.douban.com/subject/{movie_id}/comments?start={page_num * 20}&limit=20&sort=new_score&status=P'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        comments_divs = soup.find_all('div', class_='comment-item')

        for comment_div in comments_divs:
            rating_span = comment_div.find('span', class_='comment-info').find_all('span')[1]
            rating = rating_span['class'][0][7]
            comment = comment_div.find('span', class_='short').text

            if len(comment) >= 50:
                writer.writerow([rating, comment])
