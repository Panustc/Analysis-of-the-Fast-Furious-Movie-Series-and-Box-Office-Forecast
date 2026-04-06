import jieba
from wordcloud import WordCloud
from bilibili_api import video, sync

# 视频BV号
bv = 'BV1QR4y1q7ou'

# 创建Video对象
v = video.Video(bvid=bv)

# 获取弹幕列表
dms = sync(v.get_danmakus())

# 将所有弹幕的文本拼接成一个字符串
text = ''
for dm in dms:
    text += dm.text

# 使用jieba分词将字符串分词
words = jieba.cut(text)

# 将分词结果转换为列表
word_list = list(words)

# 去除一些无意义的词汇
stopwords = ['的', '了', '是', '我', '你', '他', '她', '我们', '你们', '他们', '她们','啊','这']
word_list = [word for word in word_list if word not in stopwords]

# 将词汇列表转换为以空格分隔的字符串
word_str = ' '.join(word_list)

# 制作词云
wc = WordCloud(width=800, height=600, background_color='white', font_path='msyh.ttc')
wc.generate(word_str)

# 显示词云
wc.to_file('速度与激情10预告弹幕云图.png')

