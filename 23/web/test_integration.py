# from app import *
# import parse
# import unittest
# 
# 
# class TestCase(unittest.TestCase):
#     def test_valid_expression(self):
#         tester = app.test_client(self)
#         response = tester.post('/add',
#                                data={"expression":"1+1"},
#                                follow_redirects=True)
#         self.assertIn(b"1+1", response.data)
# 
#     def test_connection_to_db(self):
#         tester = app.test_client(self)
#         tester.post('/add',
#                     data={"expression": "1+1"},
#                     follow_redirects=True)
#         last_expr = db.session.query(Expression).order_by(Expression.now).first()
#         self.assertEqual(last_expr.text, "1+1")
# 
#     def test_invalid_expression(self):
#         tester = app.test_client(self)
#         tester.post('/add',
#                     data={"expression": "1+uyw"},
#                     follow_redirects=True)
#         self.assertRaises(Exception, parse.parseExpression)
# 
# 
# if __name__ == '__main__':
#     unittest.main()


import random
import requests
import unittest
from sqlalchemy import create_engine, text
from sqlalchemy import Table, MetaData
from sqlalchemy.orm import sessionmaker


URI = 'postgresql://cs162_user:cs162_password@localhost/cs162'
metadata = MetaData()
engine = create_engine(URI)
Expression = Table('expression', metadata, autoload=True, autoload_with=engine)
Session = sessionmaker(engine)  


class TestServer(unittest.TestCase):

    def test_connection(self):
        response = requests.get('http://localhost:5000')
        self.assertEqual(response.status_code, 200)
    def test_post(self):
        response = requests.post('http://localhost:5000/add', data={'expression':'1+1'})
        self.assertEqual(response.status_code, 200)

    def test_err(self):
        response = requests.post('http://localhost:5000/add', data={'expressions':'1+'})
        self.assertEqual(response.status_code, 400)


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.x = random.random()
        self.y = random.random()
        self.expr = str(self.x)+" + "+str(self.y)
        self.response = requests.post('http://localhost:5000/add', data={'expression':self.expr})

    def test_db(self):
        session = Session()
        row = session.query(Expression).order_by(text('Expression.now desc')).first()
        self.assertAlmostEqual(float(row.value), self.x+self.y)

if __name__ == '__main__':
    unittest.main()