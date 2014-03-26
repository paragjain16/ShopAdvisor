from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.spider import BaseSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy import log
from walmartproducts.items import WalmartproductsItem
from scrapy.http import Request

class walmartproducts(CrawlSpider):

	name='walmartproductsold'
	allowed_domains = ['walmart.com']
	start_urls = ['http://www.walmart.com/browse/cookies/976759_976787_1001391/']
	productList = []
	#rules = [Rule(SgmlLinkExtractor(allow=['']), 'parse_walmart')]
	#print 'outside def'
	def parse(self, response):
		print 'inside parse'
		#productList = []
		#sel = HtmlXPathSelector(response)
		#if ( "ic" not in response.url ):
		for i in range(2) :
			#list = 
			request = Request ('http://www.walmart.com/browse/cookies/976759_976787_1001391/?ic=60_'+str(i*60), callback=self.parse_items)
		return request 
			#productList.extend(list)
		return self.productList
	def parse_items(self, response):
		print 'inside parse items'
		products = []
		sel = HtmlXPathSelector(response)
		divs=sel.select('//*[@id="shelfDiv"]//*[@id="border"]/div')
		for p in divs:
			if (len(p.re('i_[\d]*')) == 1):
				product = WalmartproductsItem()	
				product['id']= p.select('@id').extract()[0].split('_')[1]
				info = p.select('.//*[@class="prodInfo"]')
				product['url'] = info.select('.//div[@class="prodInfoBox"]/a/@title').extract()[0]
				#product['url'] = sel.select('//*[@id="shelfDiv"]//*[@id="border"]').extract()
				#product['id'] = ''
				products.append(product)
		self.productList.extend(products)
		return products
		
