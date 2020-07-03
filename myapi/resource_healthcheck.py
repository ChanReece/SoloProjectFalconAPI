import json
import falcon

class HealthResource(object):

    def on_get(self, req, resp):
        """Handles GET requests"""
        response = {"status": "good"}
        as_string = json.dumps(response)

        # Set attributes of the Response which is sent to requestor
        resp.body = as_string
        resp.status = falcon.HTTP_200
