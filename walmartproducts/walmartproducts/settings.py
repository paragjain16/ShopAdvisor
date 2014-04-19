# Scrapy settings for walmartproducts project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'walmartproducts'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['walmartproducts.spiders']
NEWSPIDER_MODULE = 'walmartproducts.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = {
    'walmartproducts.pipelines.WalmartproductsPipeline': 300
}
#AUTOTHROTTLE_ENABLED = True
CONCURRENT_REQUESTS = 100 
