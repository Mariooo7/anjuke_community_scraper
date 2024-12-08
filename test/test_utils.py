import unittest
from anjuke_scraper import get_url, get_community_details, save_to_csv
from anjuke_scraper.config import headers, cookies

class TestUtils(unittest.TestCase):
    def test_get_url(self):
        result = get_url('guangzhou', 'haizhu', 2, headers, cookies)
        self.assertIsNotNone(result)  # 确保返回的内容不是None

    def test_get_community_details(self):
        test_url = 'https://guangzhou.anjuke.com/community/view/874347'
        result = get_community_details(test_url, headers, cookies)
        self.assertEqual(len(result), 6)  # 确保解析出的属性数量为6
        self.assertEqual(result['小区名字'], '珠江帝景苑')
        self.assertEqual(result['小区地址'], '海珠-广州塔-灏景街1号')

if __name__ == '__main__':
    unittest.main()