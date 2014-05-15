ps -ef | grep "start.sh" | awk '{print $2}' | xargs kill -s SIGTERM
ps -ef | grep "scrapy crawl spiderSM" | awk '{print $2}' | xargs kill -s SIGTERM
