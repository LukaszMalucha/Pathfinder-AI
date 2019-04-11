from unittest import TestCase
from app import app


class TestHome(TestCase):

    ## Home Test

    def test_home(self):
        with app.test_client() as c:
            resp = c.get('/')
            self.assertEqual(resp.status_code, 200)

    # Login page loads correctly

    def test_login_page_loads(self):
        with app.test_client() as c:
            response = c.get('/login', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Please Log in' in response.data)

    # Signup page loads correctly

    def test_signin_page_loads(self):
        with app.test_client() as c:
            response = c.get('/register', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Sign In' in response.data)

    # Ensure that canvas shows on the  homepage

    def test_form_shows_up(self):
        with app.test_client() as c:
            response = c.get('/', follow_redirects=True)
            self.assertTrue(b'Create the Environment for AI' in response.data)
            self.assertEqual(response.status_code, 200)
