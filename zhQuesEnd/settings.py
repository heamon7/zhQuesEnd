# -*- coding: utf-8 -*-

# Scrapy settings for zhQuesEnd project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'zhQuesEnd'

CONCURRENT_REQUESTS = 100
CONCURRENT_REQUESTS_PER_DOMAIN = 100

SPIDER_MODULES = ['zhQuesEnd.spiders']
NEWSPIDER_MODULE = 'zhQuesEnd.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhQuesEnd (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'zhQuesEnd.pipelines.FirstPipline': 300,
   # 'zhihut.pipelines.SecondPipline': 800,
}