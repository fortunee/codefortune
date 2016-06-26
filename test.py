import unittest
from app import app

class CodeFortuneTestCase(unittest.TestCase):
    '''is the project up and running properly?'''

    def test_index(self):
        '''tests if index page loads properly'''
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_actual_index(self):
        ''' tests if its the actual index page'''
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Hello there!' in response.data)

    def test_projects_route(self):
        '''tests if projects page loads properly'''
        tester = app.test_client(self)
        response = tester.get('/projects', content_type='html/text')
        self.assertTrue(b'Featured Projects' in response.data)

    def test_blogs_route(self):
        '''tests if blogs page loads correctly'''
        tester = app.test_client(self)
        response = tester.get('/blogs', content_type='html/text')
        self.assertTrue(b'YoungTechMind' in response.data)

    def test_about_route(self):
        '''test if about page loads properly'''
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        self.assertTrue(b'I\'d really love to help' in response.data)

    def test_contact_route(self):
        '''tests if contact page loads properly'''
        tester = app.test_client(self)
        response = tester.get('/contact', content_type='html/text')
        self.assertTrue(b'Social Media Links' in response.data)

    def test_contact_form_is_filled_incorrectly(self):
        '''tests if contact form provides appropriate error with
            incorrect details'''
        tester = app.test_client(self)
        response = tester.post(
            '/contact',
            data=dict(
                name='fortune',
                email='fortune',
                subject='hello',
                message='hi'
            ),
            follow_redirects=True
        )
        self.assertIn(
            b"Please check the form for the incorrect detail(s)",
            response.data
        )


if __name__ == '__main__':
    unittest.main()
