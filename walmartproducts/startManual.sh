#!/bin/sh
#python getsitemaps.py
while read line           
do
  echo "crawling  $line " >> runlog
  scrapy crawl spiderSM -a smf=$line
done < crawl

