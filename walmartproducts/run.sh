#!/bin/sh
while read line           
do
  echo "crawling  $line \n" >> runlog
  scrapy crawl spiderSM -a smf=$line
done < crawl

