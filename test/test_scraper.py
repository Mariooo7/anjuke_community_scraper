import os.path
import unittest
from anjuke_scraper import get_communities
from anjuke_scraper import headers, cookies

class Scraper(unittest.TestCase):
    def test_get_communities(self):
        get_communities('guangzhou', 'haizhu', 1, headers, cookies)
        self.assertTrue(os.path.exists('guangzhou_haizhu_1.csv'))  # 确保结果存入csv
    def tearDown(self):
        if os.path.exists('guangzhou_haizhu_1.csv'):
            os.remove('guangzhou_haizhu_1.csv')

if __name__ == '__main__':
    unittest.main()