import unittest
# import dataset

# connecting to a MySQL database with user and password
# db = dataset.connect('mysql+pymysql://root:123456@localhost/test')

class MysqlTestCase(unittest.TestCase):
    def test_create_table(self):
        print('test create table')
        
        # self.assertEqual('a', 'b', 'msg')
        pass

    # def test_insert(self):
    #     print('test insert')
    #     pass

    # def test_raw_sql_query(self):
    #     print('test raw sql query')
    #     pass

    # def test_orm_query(self):
    #     print('test orm query')
    #     pass

    # def test_update(self):
    #     print('test update')
    #     pass

    # def test_delete(self):
    #     print('test delete')
    #     pass

    # def test_transaction(self):
    #     print('test transaction')
    #     pass

if __name__ == '__main__':
    unittest.main()
