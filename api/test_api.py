import unittest
import requests

class APITest(unittest.TestCase):
    """Test API endpoints"""

    def setUp(self) -> None:
        self.session = requests.Session()
        return super().setUp()

    def test_home_endpoint(self):
        res = self.session.get('http://127.0.0.1:5000/')
        self.assertTrue(res.status_code == 200)
    
    def test_list_endpoint_with_no_argument(self):
        res = self.session.get('http://127.0.0.1:5000/list', params={})
        result = res.json()
        self.assertTrue(res.status_code == 200)
        self.assertTrue(type(result) == dict)
        self.assertIn("Articles", result)
        article = result['Articles'][0]
        self.assertIn("Link", article)
        self.assertIn("Title", article)
        self.assertIn("Date", article)
        self.assertIn("Article", article)
    
    def test_list_endpoint_with_bad_argument(self):
        res = self.session.get('http://127.0.0.1:5000/list', params={"argument":"bad"})
        self.assertTrue(res.status_code == 400)
        self.assertTrue(type(res.json()) == dict)
    
    def test_list_endpoint_with_argument(self):
        res = self.session.get('http://127.0.0.1:5000/list', params={"start":0})
        result = res.json()
        self.assertTrue(res.status_code == 200)
        self.assertTrue(type(result) == dict)
        self.assertIn("Articles", result)
        article = result['Articles'][0]
        self.assertIn("Link", article)
        self.assertIn("Title", article)
        self.assertIn("Date", article)
        self.assertIn("Article", article)
    
    def test_search_endpoint_with_no_search_argument(self):
        res = self.session.get('http://127.0.0.1:5000/search', params={})
        self.assertTrue(res.status_code == 400)
        self.assertTrue(type(res.json()) == dict)
    
    def test_search_endpoint_with_bad_argument(self):
        res = self.session.get('http://127.0.0.1:5000/search', params={"argument":"bad"})
        self.assertTrue(res.status_code == 400)
        self.assertTrue(type(res.json()) == dict)
    
    def test_search_endpoint_with_argument(self):
        res = self.session.get('http://127.0.0.1:5000/search', params={"start":0, "query":"australia"})
        result = res.json()
        self.assertTrue(res.status_code == 200)
        self.assertTrue(type(result) == dict)
        self.assertIn("Articles", result)
        article = result['Articles'][0]
        self.assertIn("Link", article)
        self.assertIn("Title", article)
        self.assertIn("Date", article)
        self.assertIn("Article", article)
        
    def test_search_endpoint_with_random_search_argument(self):
        res = self.session.get('http://127.0.0.1:5000/search', params={"start":0, "query":"some_random_string"})
        self.assertTrue(res.status_code == 200)
        self.assertTrue(type(res.json()) == dict)
        self.assertTrue(res.json() == {"Message": "No Articles Found"})
    
    def test_search_endpoint_with_random_search_argument(self):
        res = self.session.get('http://127.0.0.1:5000/search', params={"start":10, "query":"some_random_string"})
        self.assertTrue(res.status_code == 200)
        self.assertTrue(type(res.json()) == dict)
        self.assertTrue(res.json() == {"Message": "No Articles Found"})

    def test_article_endpoint_with_random_id(self):
        res = self.session.get(f'http://127.0.0.1:5000/article/{"some_random_id"}')
        self.assertTrue(res.status_code == 200)
        self.assertTrue(type(res.json()) == dict)
        self.assertTrue(res.json() == {"Message": "Article Not Found or Invalid Input"})
    
    def test_article_endpoint_with_valid_id(self):
        res = self.session.get(f'http://127.0.0.1:5000/article/{"60d08f6ceadf0fec4c48341e"}')
        result = res.json()
        self.assertTrue(res.status_code == 200)
        self.assertTrue(type(result) == dict)
        self.assertIn("Link", result)
        self.assertIn("Title", result)
        self.assertIn("Date", result)
        self.assertIn("Author", result)
        self.assertIn("Category", result)

    def tearDown(self) -> None:
        self.session.close()
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()