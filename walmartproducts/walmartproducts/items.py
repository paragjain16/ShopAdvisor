# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class WalmartproductsItem(Item):
    	# define the fields for your item here like:
    	# name = Field()
    	#  pass
	#def __init__(self):
	#	url = ''
        #	src = ''
	#       name = ''
	#      id = ''
        #	price = ''
	#       image = ''
        #	rating = '' 
	#       category = ''
	url = Field()
      	src = Field()
      	name = Field()
      	id = Field()
	price = Field()
	image = Field()
	rating = Field()
	category = Field()
