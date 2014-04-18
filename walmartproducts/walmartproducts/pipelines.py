'''
 PRODUCT_ID     | bigint(20)
 PRODUCT_NAME   | varchar(255)
 MAP_ID         | bigint(20)
 BARCODE        | bigint(20)
 SOURCE         | varchar(255)
 SOURCE_LINK    | varchar(255)
 RATING         | tinyint(4)
 PRICE          | decimal(15,2)
 IMAGE_ID       | varchar(255)
 LAST_REVIEW_ID | bigint(20)
'''
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import MySQLdb
from scrapy import log
import logging
class WalmartproductsPipeline(object):
    def process_item(self, item, spider):
	try:
		conn = MySQLdb.connect('192.168.2.10', 'mysql', 'mysql', 'shopadvisor', charset='utf8', use_unicode=True)
		cursor = conn.cursor()
		itemid = int(item.get('id', -1))
		#print itemid 
		#print 'above item id' 
 		cursor.execute("SELECT PRODUCT_ID FROM PRODUCTS WHERE PRODUCT_ID = %s", itemid)
	
		res = cursor.fetchone()
		if res is None:
			cursor.execute("""INSERT INTO PRODUCTS VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (itemid, item.get('name',''), 0, 0, 'walmart',item.get('url',''), int(item.get('rating',0)), float(item.get('price',0.0)), item.get('image',''),0))
			conn.commit()
		else:
			cursor.execute("""UPDATE PRODUCTS SET PRODUCT_NAME= %s, MAP_ID= %s, BARCODE= %s, SOURCE= %s, SOURCE_LINK= %s, RATING=%s, PRICE= %s, IMAGE_ID= %s, LAST_REVIEW_ID= %s WHERE PRODUCT_ID= %s """,(item.get('name'), 0, 0, 'walmart',item.get('url',''), int(item.get('rating',0)), float(item.get('price',0.0)), item.get('image',''),0, itemid)) 
			conn.commit()
        #return item
	except Exception as e:
		log.msg(str(e), level=log.ERROR)
		log.err()
