# -*- coding: utf-8 -*-
import os
# Scrapy settings for myFirst project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'myFirst'

SPIDER_MODULES = ['myFirst.spiders']
NEWSPIDER_MODULE = 'myFirst.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'myFirst (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'myFirst.middlewares.MyfirstSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'myFirst.middlewares.MyfirstDownloaderMiddleware': 543,
#}


#DOWNLOADER_MIDDLEWARES = {

     #'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':None,
     #'myFirst.middlewares.RandomProxyMiddleware':125,
     #'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware':None
#}



# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'myFirst.pipelines.MyfirstPipeline': 300,
#}

ITEM_PIPELINES = {
    # 后面的数字代表执行优先级 ，当执行pipeine的时候会按照数字由小到大执行
    'myFirst.pipelines.MyfirstPipeline': 300,
    'scrapy.pipelines.images.ImagesPipeline':5   #scrapy 自带的图片pipeline
    #在此添加我们新定义的pipeline
    #'douban.pipelines.tongcheng_pipeline_json': 300,
}
IMAGES_URLS_FIELD ="imageUrl"  #imageUrl是在items.py中配置的网络爬取得图片地址 必须是list列表
project_dir=os.path.abspath(os.path.dirname(__file__))  #获取当前爬虫项目的绝对路径
IMAGES_STORE=os.path.join(project_dir,'images')  #组装新的图片路径
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60DOWNLOADER_MIDDLEWARES
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


MONGO_HOST = "localhost"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "scrapy"  # 库名
MONGO_COLL = "movie"  # 表名
MONGO_IP = "ip"  # 表名
