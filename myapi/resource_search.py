import json
import falcon
import requests

class SearchResource(object):
    

    def __init__(self):
        self.list = []

    def on_get(self, req, resp, experiencetype):
        """Handles GET requests"""
        #response = self.search_domain(domain)
        #as_string = json.dumps(response)

        # Set attributes of the Response which is sent to requestor

        #resp.body = self.object
       
        resp.body = '{"data":' + json.dumps(self.list) + "}" 
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        request_info = json.dumps(req.media)
        resp.body = request_info
        self.list.append(request_info)
        #self.list = request_info
        resp.status = falcon.HTTP_200


    def search_domain(self, domain):
        domain_find = {'q' : domain, 'pagestart' : '4', 'pagesize': '4'}
        info = requests.get("https://www.godaddy.com/domainsapi/v1/search/all?", params = domain_find)
        x = info.json()
        return x

        
