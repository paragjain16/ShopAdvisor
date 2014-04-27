from scrapy import cmdline

import urllib
from xml.dom import minidom
import os
import logging

def start_crawl():
	with open('crawl', 'r') as f:
		for line in f:
			logging.info('Starting to crawl '+line)
			cmdline.execute(("scrapy crawl spiderSM -a smf="+line.strip()).split())
logging.basicConfig(filename='StartLog.log', level=logging.DEBUG)
start_crawl()
