import csv
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
    
    # 创建CSV文件并写入评论
    with open('B站评论.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['用户名', '评论内容'])
        for cmt in comments:
            writer.writerow([cmt['member']['uname'], cmt['content']['message']])
    
    # 打印评论总数
    print(f"\n\n共有 {count} 条评论（不含子评论）")

sync(main())
