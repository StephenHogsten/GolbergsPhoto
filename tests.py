#!flask/bin/python
import os
import unittest
from StringIO import StringIO

from app import app

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()

    def test_file_upload(self):
        test_file = 'test string xyz'
        test_filename = 'test_filename.jpg'
        result = self.app.post('/pic', data=dict(
            file_field=(StringIO(test_file), test_filename),
        ))
        assert result.status_code == 200
        assert result.data == test_file
        assert 2 == 0

if __name__ == '__main__':
    unittest.main()


# def test_logo(self):  
#    data = dict(logo=(io.BytesIO(b'test'), 'test_file.jpg')
#    response = self.client.post(
#        url_for('items.save'), data=data,
#        follow_redirects=True,
#        content_type='multipart/form-data'
#    )
#    self.assertIn(b'Your Item has been saved.', response.data)
#    item = Item.query.get(1)
#    self.assertIsNotNone(item.logo)

#    eturn client.post('/login', data={
#         'username': username,
#         'password': password
# }, follow_redirects=True)