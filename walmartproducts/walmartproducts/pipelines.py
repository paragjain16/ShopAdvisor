'''
+------------------+---------------+------+-----+---------+-------+
| PRODUCT_ID       | bigint(20)    | NO   | PRI | 0       |       |
| PRODUCT_NAME     | varchar(255)  | NO   | PRI |         |       |
| MAP_ID           | bigint(20)    | YES  |     | NULL    |       |
| BARCODE          | bigint(20)    | YES  |     | NULL    |       |
| SOURCE           | varchar(255)  | YES  |     | NULL    |       |
| SOURCE_LINk      | varchar(255)  | YES  |     | NULL    |       |
| RATING           | decimal(3,2)  | YES  |     | NULL    |       |
| PRICE            | decimal(15,2) | YES  |     | NULL    |       |
| IMAGE_ID         | varchar(255)  | YES  |     | NULL    |       |
| LAST_REVIEW_ID   | bigint(20)    | YES  |     | NULL    |       |
| LAST_REVIEW_DATE | date          | YES  |     | NULL    |       |
| CATEGORY         | varchar(255)  | YES  |     | NULL    |       |
+------------------+---------------+------+-----+---------+-------+

'''
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import MySQLdb
from scrapy import log
import logging
class WalmartproductsPipeline(object):
    def process_item(self, item, spider):
        try:
		conn = MySQLdb.connect('localhost', 'root', 'hello_iknowx', 'shopadvisor', charset='utf8', use_unicode=True)
                itemid = int(item.get('id', -1))
                cursor = conn.cursor()
                #print itemid
                #print 'above item id'
                cursor.execute("""SELECT PRODUCT_ID FROM PRODUCTS WHERE PRODUCT_ID = %s""", [itemid])

                res = cursor.fetchone()
                if res is None:
                        cursor.execute("""INSERT INTO PRODUCTS(PRODUCT_ID, PRODUCT_NAME, SOURCE, SOURCE_LINk, RATING, PRICE, IMAGE_ID, CATEGORY) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""", (itemid, item.get('name',''), 'walmart',item.get('url',''), int(item.get('rating',0)), float(item.get('price',0.0)), item.get('image',''), item.get('category','')))
                        conn.commit()
                else:
                        cursor.execute("""UPDATE PRODUCTS SET PRODUCT_NAME= %s, SOURCE= %s, SOURCE_LINK= %s, RATING=%s, PRICE= %s, IMAGE_ID= %s, CATEGORY=%s WHERE PRODUCT_ID= %s """,(item.get('name'), 'walmart',item.get('url',''), int(item.get('rating',0)), float(item.get('price',0.0)), item.get('image',''), item.get('category',''), itemid))
                        conn.commit()
        #return item
        except Exception as e:
                log.msg(str(e)+itemid, level=log.ERROR)
                log.err()
