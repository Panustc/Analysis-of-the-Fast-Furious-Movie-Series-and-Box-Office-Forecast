import asyncio
from bilibili_api import video

#速度与激情9首支预报 BV197411s7gm
#速度与激情10首支预报 BV1kM411Y7ML

async def main() -> None:
    # 实例化 Video 类
    v = video.Video(bvid="BV1kM411Y7ML")
    # 获取信息
    info = await v.get_info()
    # 打印信息
    print(info)

if __name__ == '__main__':
    asyncio.run(main())



