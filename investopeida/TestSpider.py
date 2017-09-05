import unittest
import os
from spiders.investopedia import InvestopediaSpider 

from scrapy.http import TextResponse, Request, Response


class TestSpider(unittest.TestCase):

	def setUp(self):
		self.spider = InvestopediaSpider()

	

	def test_1(self):
		results = self.spider.parse_pages(self.spider.fake_response_from_file('/home/samuel/investopeida/investopeida/index.html'))
		test = False;
		if os.path.isfile('investopedia.csv'):
			if os.path.getsize('investopedia.csv') < 0:
				test = True;
		self.assertEqual(test, True)


if __name__ == '__main__':
    unittest.main()