import unittest
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

class TestCase(unittest.TestCase):
    def test_get(self):
        print("Test get")
        v = r.get('a')
        print('v = ', v)
        r.set('a', 'av1')

        v = r.get('a')
        print('get a after set = ', v)
        pass

    def test_set_ttl(self):
        print("Test set ttl")
        ttla = r.ttl('a')
        print('ttla = ', ttla)
        pass

if __name__ == '__main__':
    unittest.main()