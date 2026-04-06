#from bilibili_api import video, sync, Credential

#v = video.Video(bvid='BV1UT411c7iu')

#dms = sync(v.get_danmakus(0))

#for dm in dms:
   #print(dm)
import re
from bilibili_api import video, sync, Credential

v = video.Video(bvid='BV1UT411c7iu')
dms = sync(v.get_danmakus(0))

pattern = re.compile('[\u4e00-\u9fa5]+')
danmu = ''
for dm in dms:
    text = dm.text # 使用点符号语法访问Danmaku对象的text属性
    result = re.findall(pattern, text)
    danmu += ''.join(result)

with open('danmu.txt', 'w', encoding='utf-8') as f:
    f.write(danmu)
