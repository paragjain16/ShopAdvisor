from scrapy import cmdline

import urllib
from xml.dom import minidom
import os
import logging

'''
def start_crawl():
	with open('crawl', 'r') as f:
		for line in f:
			logging.info('Starting to crawl '+line)
			cmdline.execute(("scrapy crawl spiderSM -a smf="+line.strip()).split())

logging.basicConfig(filename='StartLog.log', level=logging.DEBUG)
'''
url = 'http://www.walmart.com/sitemap_ip.xml'
dom = minidom.parse(urllib.urlopen(url))
nodes = dom.getElementsByTagNameNS('http://www.sitemaps.org/schemas/sitemap/0.9','sitemap')
if os.path.isfile('oldfile') :
	os.remove('oldfile')
	
tocrawl = open('crawl', 'w')

if os.path.isfile('currentfile') :
	os.rename('currentfile', 'oldfile')
else :
	open('oldfile', 'a').close()
old = open('oldfile', 'r')
curr = open('currentfile', 'w')

for node in nodes :
	att = node.childNodes
	line = att[1].firstChild.nodeValue +' '+ att[3].firstChild.nodeValue
	curr.write(line+'\n')
	if not line.strip() == old.readline().strip() :
		tocrawl.write(att[1].firstChild.nodeValue+'\n')
tocrawl.close()
old.close()
curr.close()
#start_crawl()
