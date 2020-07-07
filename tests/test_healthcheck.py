import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../myapi')))
from falcon import testing
from app import app

class HealthCheckTest(testing.TestCase):
    """
    falcon.testing.TestCase is an extension of unittest.TestCase
    Creates a fake client-server connection to test your falcon code
    This allows for methods like simulate_get which generate web requests to your app
    https://falcon.readthedocs.io/en/stable/api/testing.html
    """
    def setUp(self):
        super().setUp()
        self.app = app

    def test_status_good(self):
        """Basic test to verify health check works"""
        response = self.simulate_get("/v1/healthchecks/ping")
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()
