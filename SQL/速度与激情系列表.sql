CREATE TABLE bilibili_videos (
    -- 基础信息 (主键)
    bvid VARCHAR(20) PRIMARY KEY COMMENT 'B站视频BV号',
    aid BIGINT NOT NULL COMMENT '视频AV号',
    title VARCHAR(255) NOT NULL COMMENT '视频标题',
    pubdate DATETIME COMMENT '发布时间',
    duration INT COMMENT '视频时长(秒)',
    -- UP主信息
    uploader_mid BIGINT COMMENT 'UP主UID',
    uploader_name VARCHAR(100) COMMENT 'UP主昵称',
    -- 互动数据 (核心指标)
    view_count INT DEFAULT 0 COMMENT '播放量',
    danmaku_count INT DEFAULT 0 COMMENT '弹幕数',
    reply_count INT DEFAULT 0 COMMENT '评论数',
    like_count INT DEFAULT 0 COMMENT '点赞数',
    coin_count INT DEFAULT 0 COMMENT '投币数',
    favorite_count INT DEFAULT 0 COMMENT '收藏数',
    share_count INT DEFAULT 0 COMMENT '分享数',
    -- 运营/标签信息
    tags TEXT COMMENT '视频动态/标签',
    highest_rank INT COMMENT '全站最高排行(若无则为0)',
    -- 系统字段
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '数据入库时间',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '数据更新时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='B站视频基本信息及互动数据表';


####速度与激情9数据
INSERT INTO bilibili_videos (
    bvid, aid, title, pubdate, duration, 
    uploader_mid, uploader_name, 
    view_count, danmaku_count, reply_count, 
    like_count, coin_count, favorite_count, share_count, 
    tags, highest_rank
) VALUES (
    'BV197411s7gm', 
    86045769, 
    '《速度与激情9》曝！首支预告！', 
    FROM_UNIXTIME(1580525060), -- B站返回的是时间戳，用MySQL函数自动转换为日期时间格式
    231, 
    494915529, 
    '环球影业Official', 
    1182125, 
    5854, 
    3432, 
    25972, 
    6669, 
    7604, 
    32088, 
    '#速度与激情##预告##范迪塞尔#', 
    87 -- 从 honor_reply 中提取的最高排名
);

INSERT INTO bilibili_videos (
    bvid, aid, title, pubdate, duration, 
    uploader_mid, uploader_name, 
    view_count, danmaku_count, reply_count, 
    like_count, coin_count, favorite_count, share_count, 
    tags, highest_rank
) VALUES (
    'BV1kM411Y7ML', 
    524136440, 
    '是这个味儿！《速度与激情10》首支预告发布', 
    FROM_UNIXTIME(1676044651), -- 2023-02-10 13:17:31
    221, 
    494915529, 
    '环球影业Official', 
    816646, 
    2390, 
    2814, 
    17443, 
    1646, 
    2912, 
    18466, 
    '《速度与激情10》首支预告正式发布，经典角色悉数回归，重返飙车赛场，上演生死竞速！', -- 动态为空，这里使用了desc字段补位
    0 -- 该视频未显示全站排行榜具体名次，故设为0
);


CREATE TABLE dim_movies (
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title_cn VARCHAR(100) NOT NULL COMMENT '中文标题',
    title_en VARCHAR(100) NOT NULL COMMENT '英文标题',
    release_year INT COMMENT '上映年份',
    director VARCHAR(50) COMMENT '导演',
    budget_mUSD DECIMAL(10, 2) COMMENT '制作成本(百万美元)',
    global_box_office_mUSD DECIMAL(10, 2) COMMENT '全球票房(百万美元)',
    series_order INT COMMENT '系列序号'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
###### 速度与激情系列电影主表

INSERT INTO dim_movies (title_cn, title_en, release_year, director, budget_mUSD, global_box_office_mUSD, series_order) VALUES
('速度与激情', 'The Fast and the Furious', 2001, 'Rob Cohen', 38.00, 207.30, 1),
('速度与激情2', '2 Fast 2 Furious', 2003, 'John Singleton', 76.00, 236.40, 2),
('速度与激情3：东京漂移', 'The Fast and the Furious: Tokyo Drift', 2006, 'Justin Lin', 85.00, 158.50, 3),
('速度与激情4', 'Fast & Furious', 2009, 'Justin Lin', 85.00, 360.40, 4),
('速度与激情5', 'Fast Five', 2011, 'Justin Lin', 125.00, 626.10, 5),
('速度与激情6', 'Fast & Furious 6', 2013, 'Justin Lin', 160.00, 788.70, 6),
('速度与激情7', 'Furious 7', 2015, 'James Wan', 190.00, 1515.30, 7),
('速度与激情8', 'The Fate of the Furious', 2017, 'F. Gary Gray', 250.00, 1236.00, 8),
('速度与激情：特别行动', 'Hobbs & Shaw', 2019, 'David Leitch', 200.00, 760.70, 0), -- 衍生剧设为0
('速度与激情9', 'F9', 2021, 'Justin Lin', 200.00, 726.20, 9),
('速度与激情10', 'Fast X', 2023, 'Louis Leterrier', 340.00, 704.80, 10);

CREATE TABLE fact_box_office (
    fact_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT NOT NULL COMMENT '关联dim_movies的外键',
    domestic_box_office_mUSD DECIMAL(10, 2) COMMENT '北美票房(百万美元)',
    international_box_office_mUSD DECIMAL(10, 2) COMMENT '海外票房(不含北美, 百万美元)',
    china_box_office_mUSD DECIMAL(10, 2) COMMENT '中国内地票房(折算百万美元)',
    total_global_box_office_mUSD DECIMAL(10, 2) COMMENT '全球总票房(百万美元)',
    CONSTRAINT fk_movie FOREIGN KEY (movie_id) REFERENCES dim_movies(movie_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
##### 速度与激情系列票房事实表

INSERT INTO fact_box_office (movie_id, domestic_box_office_mUSD, international_box_office_mUSD, china_box_office_mUSD, total_global_box_office_mUSD) VALUES
(1, 144.53, 62.75, 0.00, 207.28),    -- 速1 (中国未正式公映)
(2, 127.15, 109.19, 0.00, 236.35),   -- 速2
(3, 62.51, 95.95, 0.00, 158.47),     -- 速3
(4, 155.06, 208.10, 4.51, 363.16),   -- 速4 (国内票房约3000万RMB)
(5, 209.83, 416.28, 38.01, 626.12),  -- 速5 (国内开始发力)
(6, 238.67, 550.00, 66.30, 788.67),  -- 速6
(7, 353.00, 1162.00, 390.90, 1515.00),-- 速7 (巅峰：保罗效应+中国市场大爆发)
(8, 226.00, 1010.00, 392.80, 1236.00),-- 速8 (海外依赖度极高)
(10, 173.00, 553.20, 216.00, 726.20), -- 速9 (疫情影响下表现)
(11, 145.90, 558.90, 138.60, 704.80); -- 速10
#### 插入票房数据

CREATE TABLE fact_social_reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT NOT NULL COMMENT '关联dim_movies的外键',
    maoyan_score DECIMAL(3, 1) COMMENT '猫眼评分(10分制)',
    douban_score DECIMAL(3, 1) COMMENT '豆瓣评分(10分制)',
    imdb_score DECIMAL(3, 1) COMMENT 'IMDb评分(10分制)',
    rotten_tomatoes_pct INT COMMENT '烂番茄新鲜度(百分比)',
    CONSTRAINT fk_movie_review FOREIGN KEY (movie_id) REFERENCES dim_movies(movie_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='电影口碑评分事实表';

INSERT INTO fact_social_reviews (movie_id, maoyan_score, douban_score, imdb_score, rotten_tomatoes_pct) VALUES
(1, 8.8, 8.1, 6.8, 54),   -- 速1
(2, 8.5, 7.5, 5.9, 36),   -- 速2
(3, 8.4, 7.0, 6.0, 38),   -- 速3
(4, 8.7, 7.8, 6.6, 29),   -- 速4
(5, 9.3, 8.5, 7.3, 78),   -- 速5 (口碑爆发点)
(6, 9.1, 7.9, 7.0, 71),   -- 速6
(7, 9.4, 8.4, 7.1, 81),   -- 速7 (巅峰：保罗·沃克纪念)
(8, 9.2, 7.0, 6.6, 67),   -- 速8
(10, 7.6, 5.1, 5.2, 59),  -- 速9 (系列最低点)
(11, 8.6, 6.1, 5.8, 56);  -- 速10
#### 插入评分数据


CREATE TABLE dim_cast_crew (
    cast_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT NOT NULL,
    director VARCHAR(50) COMMENT '导演',
    star_1 VARCHAR(50) COMMENT '第一主演(通常是范·迪塞尔)',
    star_1_twitter_m BIGINT COMMENT '第一主演推特粉丝数(单位:万)',
    star_2 VARCHAR(50) COMMENT '第二主演',
    star_2_twitter_m BIGINT COMMENT '第二主演推特粉丝数',
    star_3 VARCHAR(50) COMMENT '第三主演',
    star_3_twitter_m BIGINT COMMENT '第三主演推特粉丝数',
    
    CONSTRAINT fk_movie_cast FOREIGN KEY (movie_id) REFERENCES dim_movies(movie_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO dim_cast_crew (movie_id, director, star_1, star_1_twitter_m, star_2, star_2_twitter_m, star_3, star_3_twitter_m) VALUES
(1, 'Rob Cohen', 'Vin Diesel', 100, 'Paul Walker', 50, 'Michelle Rodriguez', 30),
(2, 'John Singleton', 'Paul Walker', 60, 'Tyrese Gibson', 20, 'Ludacris', 25),
(3, 'Justin Lin', 'Lucas Black', 5, 'Bow Wow', 15, 'Sung Kang', 10),
(4, 'Justin Lin', 'Vin Diesel', 150, 'Paul Walker', 120, 'Gal Gadot', 10),
(5, 'Justin Lin', 'Vin Diesel', 300, 'Paul Walker', 250, 'Dwayne Johnson', 800), -- 强森加盟，粉丝量级质变
(6, 'Justin Lin', 'Vin Diesel', 500, 'Paul Walker', 400, 'Dwayne Johnson', 1200),
(7, 'James Wan', 'Vin Diesel', 800, 'Paul Walker', 800, 'Jason Statham', 500), -- 保罗遗作，关注度巅峰
(8, 'F. Gary Gray', 'Vin Diesel', 1200, 'Dwayne Johnson', 2500, 'Jason Statham', 1500),
(10, 'Justin Lin', 'Vin Diesel', 1300, 'Michelle Rodriguez', 1300, 'John Cena', 1400), -- 赵喜娜加盟
(11, 'Louis Leterrier', 'Vin Diesel', 1400, 'Jason Momoa', 1700, 'Michelle Rodriguez', 1400); -- 海王加盟

#### 添加一列宣发成本列
ALTER TABLE dim_movies 
ADD COLUMN marketing_cost_mUSD DECIMAL(10, 2) AFTER budget_mUSD;
UPDATE dim_movies SET marketing_cost_mUSD = 20.00 WHERE series_order = 1;  -- 速1：初期宣发规模较小
UPDATE dim_movies SET marketing_cost_mUSD = 35.00 WHERE series_order = 2;
UPDATE dim_movies SET marketing_cost_mUSD = 40.00 WHERE series_order = 3;
UPDATE dim_movies SET marketing_cost_mUSD = 50.00 WHERE series_order = 4;
UPDATE dim_movies SET marketing_cost_mUSD = 80.00 WHERE series_order = 5;  -- 规模开始扩大
UPDATE dim_movies SET marketing_cost_mUSD = 100.00 WHERE series_order = 6;
UPDATE dim_movies SET marketing_cost_mUSD = 150.00 WHERE series_order = 7; -- 全球现象级宣发
UPDATE dim_movies SET marketing_cost_mUSD = 160.00 WHERE series_order = 8;
UPDATE dim_movies SET marketing_cost_mUSD = 140.00 WHERE series_order = 9; -- 受疫情影响宣发节奏有调整
UPDATE dim_movies SET marketing_cost_mUSD = 175.00 WHERE series_order = 10; -- 顶级大片标配宣发

SELECT DATEDIFF('2020-01-25','2020-01-30') FROM bilibili_videos



















