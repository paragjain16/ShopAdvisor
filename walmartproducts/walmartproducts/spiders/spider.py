from scrapy.contrib.spiders import CrawlSpider, Rule, SitemapSpider
from scrapy.spider import BaseSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy import log
from walmartproducts.items import WalmartproductsItem
from scrapy.http import Request
import urlparse

class walmartproducts(BaseSpider):

	name='walmartproducts'
	allowed_domains = ['walmart.com']
	start_urls = ['http://www.walmart.com/browse/0/0?ic=60_0']
	log.ScrapyFileLogObserver(open('log.log','a'), level=log.INFO).start()
	#download_delay = 1
	def parse(self, response):
     		#items = []         
		#yield Request(response.url, meta={'items':items},callback=self.parse_items)
	     	#get next button link 
		#print 'inside browser'
		pages = int(response.url.split('_')[-1])
		if pages%700 == 0:
			log.msg('Crawled '+str(pages)+' list pages of 60 products each')
		sel = HtmlXPathSelector(response)
		links = sel.select('.//div[@class="prodInfoBox"]/a/@href')
		for link in links:
			yield Request('http://www.walmart.com'+link.extract(), self.parse_product)
		'''
		divs=sel.select('//*[@id="shelfDiv"]//*[@id="border"]/div')
		for p in divs:
			if (len(p.re('i_[\d]*')) == 1):
				item = WalmartproductsItem()
				try:
					item['id']= p.select('@id').extract()[0].split('_')[1]
					info = pi.select('.//*[@class="prodInfo"]')
					item['url'] = info.select('.//div[@class="prodInfoBox"]/a/@title').extract()[0]
					yield item
				except Exception:
					#print item.get('url', '')
					#print 'Trying to print url'
					yield item
		'''
	     	next_page = sel.select('//a[text()="Next" and contains(@href, "ic")]/@href') 
	     	if len(next_page) == 1 : 
	        	yield Request('http://www.walmart.com'+next_page.extract()[0], self.parse)
	def parse_product(self, response):
	        #print 'Inside product parser'
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
	                item['rating'] = 0
        	        if len(rating) is not 0:
                	        item['rating'] = float(rating[0].extract().split(" ")[0])
	                cat = ''
        	        for li in hxs.select('//*[@id="crumbs"]/li') :
                	        cat = cat+li.select('./a/text()').extract()[0]+': '
	                item['category'] = cat
			item['image'] = hxs.select('*//div[@class="columnOne"]/div[@class="BoxContent"]//a[@id="Zoomer"]/@href')[0].extract()
        	        #item['description'] = node.xpath('description').extract()
                	return item
	        except Exception as e:	
                	log.msg(str(e), level=log.ERROR)
			log.err()
        	        return item

