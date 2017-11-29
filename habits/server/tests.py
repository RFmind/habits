import unittest

from app import app

class HabitsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client

    def test_index_route_status_ok(self):
        self.assertEqual(
            self.client().get('/').status_code,
            200)

if __name__ == '__main__':
    unittest.main()

