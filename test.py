import unittest
import psycopg2
from helperFunction import *
from build_database import *
from filter_data import filter

conn = psycopg2.connect(host = '', database = '', user = '', password = '')
cur = conn.cursor()

class TestStringMethods(unittest.TestCase):

    def test_match(self):
        row = [11111, 'OFFENSE', 3701, 'stranger', '2017-10-10', '1111 Hi Rd', 'Squirrel Hill', 5]
        valueDict, script = match(row)
        self.assertEqual(script, "SELECT neighbor FROM neighborhoods" + \
        " WHERE LOWER(neighbor) LIKE LOWER('%Squirrel Hill%')" + \
        " OR LOWER('Squirrel Hill') LIKE format('%%%s%%', LOWER(neighbor));")

    def test_filter(self):
        valid_sections = ['3304','2709','3502','13(a)(16)','13(a)(30)','3701','3921',
                    '3921(a)','3934','3929','2701','2702','2501']
        self.assertEqual(filter('test_filter.csv', 'OFFENSE 2.0', valid_sections), 3)

if __name__ == '__main__':
    unittest.main()
