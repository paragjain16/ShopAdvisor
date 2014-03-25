from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy import log
from walmartproducts.items import WalmartproductsItem

class walmartproducts(CrawlSpider):

	name='walmartproducts'
	allowed_domains = ['walmart.com']
	start_urls = ['http://www.walmart.com/browse/cookies/976759_976787_1001391/']
	#rules = [Rule(SgmlLinkExtractor(allow=['']), 'parse_walmart')]
	#print 'outside def'
	def parse(self, response):
		print 'inside def'
		productList = []
		sel = HtmlXPathSelector(response)
		#p = sel.select('//*[@id="shelfDiv"]//*[@id="border"]/div')
		divs=sel.select('//*[@id="shelfDiv"]//*[@id="border"]/div')
		for p in divs:
			if (len(p.re('i_[\d]*')) == 1):
				product = WalmartproductsItem()	
				product['id']= p.select('@id').extract()[0].split('_')[1]
				info = p.select('.//*[@class="prodInfo"]')
				product['url'] = info.select('.//div[@class="prodInfoBox"]/a/@title').extract()[0]
				#product['url'] = sel.select('//*[@id="shelfDiv"]//*[@id="border"]').extract()
				#product['id'] = ''
				productList.append(product)
		return productList

