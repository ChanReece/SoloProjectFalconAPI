"""
This is where you define your application
by associated resource objects to their endpoints
"""
import falcon
from myapi.resource_healthcheck import HealthResource

# This creates the WSGI application which understands HTTP
app = falcon.API()

# Instantiate the server resource and associate it to an endpoint
healthcheck_resource = HealthResource()
app.add_route('/v1/healthchecks/ping', healthcheck_resource)
