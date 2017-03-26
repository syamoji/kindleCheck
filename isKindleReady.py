# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2, sys

# sample url
# getUrl = "https://www.amazon.co.jp/dp/4091275133/"

# 引数チェック
if len(sys.argv) <= 1:
  print("url is needed")
  print("Usage: python isKindleReady.py AMAZON_URL")
  sys.exit()

# 取得したいamazonページを引数から取得
getUrl = sys.argv[1]


html = urllib2.urlopen(getUrl)

soup = BeautifulSoup(html, "html.parser")

# 書籍情報の「コミック」「Kindle」部分を読み込み
# Kindleという文字列があればTrue
formatList = soup.select('div#tmmSwatches')

if "Kindle" in str(formatList[0]):
  print("True, Kindle is available")
else:
  print("False, Kindle is not available")
