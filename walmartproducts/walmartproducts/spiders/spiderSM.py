from scrapy import log
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import SitemapSpider
from walmartproducts.items import WalmartproductsItem

class MySpider(SitemapSpider):
    name = 'spiderSM'
    sitemap_urls = ['http://www.walmart.com/sitemap_ip.xml']
    sitemap_follow = ['http://www.walmart.com/sitemap_ip74.xml.gz']
    print 'Inside SM'

    #sitemap_rules = [
    #    ('/product/', 'parse_product'),
    #    ('/category/', 'parse_category'),
    #]

    def parse(self, response):
        print 'Inside parser'
        print response
        hxs = HtmlXPathSelector(response)
        item = WalmartproductsItem()
        item['id'] = response.url.split('/')[-1]
        item['url'] = response.url
        item['src'] = 'walmart'
        item['name'] = hxs.select('*//h1[@class="productTitle"]/text()').extract()[0]
        item['price'] = float((hxs.select('*//div[@class="columnTwo"]//div[contains(@class, "PricingInfo")]//span[@class="bigPriceText1"]/text()')[0].extract()+hxs.select('*//div[@class="columnTwo"]//div[contains(@class, "PricingInfo")]//span[@class="smallPriceText1"]/text()')[0].extract())[1:])
        item['rating'] = ''
        cat = ''
        for li in hxs.select('//*[@id="crumbs"]/li') :
                cat = cat+li.select('./a/text()').extract()[0]+': '
        item['category'] = cat
        #item['description'] = node.xpath('description').extract()
	return item
