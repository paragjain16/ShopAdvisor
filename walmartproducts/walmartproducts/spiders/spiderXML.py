from scrapy import log
from scrapy.contrib.spiders import XMLFeedSpider, SitemapSpider
from walmartproducts.items import WalmartproductsItem

class MySpider(XMLFeedSpider):
    name = 'walmartXML'
    allowed_domains = ['walmart.com']
    start_urls = ['http://www.walmart.com/sitemap_ip74.xml.gz']
    namespaces=[('m', 'http://www.sitemaps.org/schemas/sitemap/0.9')]
    #iterator = 'iternodes' # This is actually unnecessary, since it's the default value
    itertag = 'm:url'
    print 'instantiated dgfd'
    def parse_node(self, response, node):
	print 'inside parse node'
        item = WalmartproductsItem()
        item['id'] = node.xpath('loc').extract()
        item['url'] = ''
        #item['description'] = node.xpath('description').extract()
        return item
