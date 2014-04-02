
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
	start_urls = ['http://www.walmart.com/browse/0/0']
	download_delay = 3
	def parse(self, response):
     		items = []         

		#yield Request(response.url, meta={'items':items},callback=self.parse_items)
	     	#get next button link 
		sel = HtmlXPathSelector(response)
		divs=sel.select('//*[@id="shelfDiv"]//*[@id="border"]/div')
		for p in divs:
			if (len(p.re('i_[\d]*')) == 1):
				item = WalmartproductsItem()	
				item['id']= p.select('@id').extract()[0].split('_')[1]
				info = p.select('.//*[@class="prodInfo"]')
				item['url'] = info.select('.//div[@class="prodInfoBox"]/a/@title').extract()[0]
				yield item
	     	next_page = sel.select('//a[text()="Next" and contains(@href, "ic")]/@href') 
	     	if len(next_page) == 1 : 
	        	yield Request('http://www.walmart.com'+next_page.extract()[0], self.parse)

