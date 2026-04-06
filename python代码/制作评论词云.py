import jieba
from wordcloud import WordCloud
from bilibili_api import comment, sync

async def main():
    # 存储评论
    comments = []
    # 页码
    page = 1
    # 当前已获取数量
    count = 0
    while True:
        # 获取评论
        c = await comment.get_comments(86045769, comment.CommentResourceType.VIDEO, page)
        # 判断 c['replies'] 是否为 None，如果是就跳过
        if c['replies'] is None:
            break
        # 存储评论
        comments.extend(c['replies'])
        # 增加已获取数量
        count += c['page']['size']
        # 增加页码
        page += 1
        if count >= c['page']['count']:
            # 当前已获取数量已达到评论总数，跳出循环
            break

    # 将所有评论的文本拼接成一个字符串
    text = ''
    for cmt in comments:
        text += cmt['content']['message']

    # 使用jieba分词将字符串分词
    words = jieba.cut(text)

    # 将分词结果转换为列表
    word_list = list(words)

    # 去除一些无意义的词汇
    stopwords = ['的', '了', '是', '我', '你', '他', '她', '我们', '你们', '他们', '她们']
    word_list = [word for word in word_list if word not in stopwords]

    # 将词汇列表转换为以空格分隔的字符串
    word_str = ' '.join(word_list)

    # 制作词云
    wc = WordCloud(width=800, height=600, background_color='white', font_path='msyh.ttc')
    wc.generate(word_str)

    # 显示词云
    wc.to_file('comments_wordcloud.png')

sync(main())
