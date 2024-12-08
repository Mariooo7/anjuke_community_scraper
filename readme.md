# Anjuke Scraper

## 项目简介

此项目用于爬取安居客网站二手房小区信息，支持指定城市、区域和页数。

## 项目结构

anjuke-scraper/

│

├── anjuke_scraper/          # 主文件夹

│   ├── init.py

│   ├── **anjuke_scraper.py**           # 主要爬虫代码

│   ├── utils.py             # 工具函数

│   └── **config.py**            # 配置文件，包含爬取城市、区域、页数、cookies、headers参数

│

├── tests/                   # 测试文件夹

│   ├── test_scraper.py      # 测试爬虫

│   └── test_utils.py        # 测试工具函数

│

├── **requirements.txt**         # 依赖库文件，列出项目需要的第三方库

├── README.md                # 项目说明文件，描述如何使用、安装等

└── .gitignore               # 忽略文件


## 安装和使用

1. **下载**

   下载压缩包到本地，或克隆仓库`git clone https://github.com/Mariooo7/anjuke-scraper.git`

2. **安装依赖**

   `pip install -r requirements.txt`

3. **使用**

   1. 修改`config.py`中的参数

   2. 运行爬虫

      `python -m anjuke_scraper.anjuke_scraper`

## 注意事项

1. `cookies`参数注意改成自己的安居客网站会话`cookies`，否则无法爬取

   > cookies 获取方法：F12 --> applications(应用程序) --> cookies 

2. 有时无法爬取是因为频繁操作需要进行真人验证，手动操作后再进行爬取即可
