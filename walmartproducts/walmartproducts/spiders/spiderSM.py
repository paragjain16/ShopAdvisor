from scrapy import log
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import SitemapSpider
from walmartproducts.items import WalmartproductsItem

class MySpider(SitemapSpider):
    name = 'spiderSM' 

    def __init__(self, *args, **kwargs):
    	super(MySpider, self).__init__(*args, **kwargs)
    	self.sitemap_urls = [kwargs.get('smf')]

    def parse(self, response):
        #print 'Inside parser'
        #print response
        hxs = HtmlXPathSelector(response)
        item = WalmartproductsItem()
	try:
	        item['id'] = response.url.split('/')[-1]
	        item['url'] = response.url
	        item['src'] = 'walmart'
	        item['name'] = hxs.select('*//h1[@class="productTitle"]/text()').extract()[0]
	        item['price'] = float((hxs.select('*//div[@class="columnTwo"]//div[contains(@class, "PricingInfo")]//span[@class="bigPriceText1"]/text()')[0].extract()+hxs.select('*//div[@class="columnTwo"]//div[contains(@class, "PricingInfo")]//span[@class="smallPriceText1"]/text()')[0].extract())[1:])
		rating = hxs.select('*//div[@class="columnTwo"]//div[@class="CustomerRatings"]//img[contains(@src, "rating.png")]/@title')
	        item['rating'] = ''
		if rating is not None:
			item['rating'] = float(rating[0].extract().split(" ")[0])
	        cat = ''
	        for li in hxs.select('//*[@id="crumbs"]/li') :
	                cat = cat+li.select('./a/text()').extract()[0]+': '
	        item['category'] = cat
	        #item['description'] = node.xpath('description').extract()
		return item
	except Exception:
		return item
