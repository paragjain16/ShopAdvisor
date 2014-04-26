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
	hxs = HtmlXPathSelector(response)
	item = WalmartproductsItem()
        try:
		item['id'] = response.url.split('/')[-1]
	        item['url'] = response.url
        	item['src'] = 'walmart'
	        item['name'] = hxs.select('*//h1[@class="productTitle"]/text()').extract()[0]
		item['rating'] = 0
      	        cat = ''
		try:
        	 	for li in hxs.select('//*[@id="crumbs"]/li') :
                	       	cat = cat+li.select('.//text()').extract()[0]+': '
		        item['category'] = cat
		except Exception as e:	
                	log.msg(str(e)+' '+response.url, level=log.ERROR)
			log.err()
		try:
			item['image'] = hxs.select('*//div[@class="columnOne"]/div[@class="BoxContent"]//a[@id="Zoomer"]/@href')[0].extract()
		except Exception as e:	
                	log.msg(str(e)+' '+response.url, level=log.ERROR)
			log.err()

		try:
			item['price'] = float(((hxs.select('*//div[@class="columnTwo"]//span[@class="bigPriceText1"]/text()')[0].extract()+hxs.select('*//div[@class="columnTwo"]//span[@class="smallPriceText1"]/text()')[0].extract())[1:]).replace(",",""))
	        except Exception as e:
			item['price'] = float((hxs.select('*//div[@class="columnTwo"]//span[@class="SubmapPrice"]/text()')[0].extract()[1:]).replace(",",""))	
                	log.msg(str(e)+' '+response.url, level=log.ERROR)
			log.err()

	                #rating = hxs.select('*//div[@class="columnTwo"]//div[@class="CustomerRatings"]//img[contains(@src, "rating.png")]/@title')
        	        #if len(rating) is not 0:
                	#        item['rating'] = float(rating[0].extract().split(" ")[0])
        	        #item['description'] = node.xpath('description').extract()
               	return item
	except Exception as e:	
               	log.msg(str(e)+' '+response.url, level=log.ERROR)
		log.err()
                return item
