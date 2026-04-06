### pip install matplotlib bilibili-api-python

import matplotlib.pyplot as plt
from bilibili_api import search, sync
from datetime import datetime
from collections import Counter
import time

# 1. 改进搜索函数，支持传入页码
async def get_search_results(keyword, page_num):
    # 注意：search_by_type 的参数名在不同版本可能微调，请确认 page 对应参数
    return await search.search_by_type(
        keyword, 
        search_type=search.SearchObjectType.VIDEO,
        page=page_num
    )

results = []
print("开始抓取数据...")

# 循环获取数据
for page in range(1, 11):  # 抓取前10页数据
    try:
        res = sync(get_search_results("家人侠", page))
        videos = res.get("result", [])
        if not videos: break
            
        for item in videos:
            dt = datetime.fromtimestamp(item.get('pubdate'))
            # 【关键修改】：将时间格式化为 "YYYY-MM" 字符串
            month_str = dt.strftime('%Y-%m') 
            results.append(month_str)
            
        print(f"第 {page} 页抓取成功")
        time.sleep(1) 
    except Exception as e:
        print(f"错误: {e}")
        break

# 1. 统计每个月出现的次数
month_counts = Counter(results)

# 2. 排序：确保 X 轴的时间是按先后顺序排列的
sorted_months = sorted(month_counts.keys())
sorted_values = [month_counts[m] for m in sorted_months]

# 3. 绘图
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.figure(figsize=(12, 6))

# 使用折线图（Plot）或柱状图（Bar）在按月归纳时效果更好
plt.plot(sorted_months, sorted_values, marker='o', linestyle='-', color='b')

plt.title("B站‘家人侠’视频投稿量按月趋势统计")
plt.xlabel("年份-月份")
plt.ylabel("投稿数量")

# 4. 如果月份太多，让 X 轴标签每隔几个显示一个，防止重叠
plt.xticks(rotation=45, fontsize=8)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.savefig('家人侠每月投稿统计.png')
plt.show()




