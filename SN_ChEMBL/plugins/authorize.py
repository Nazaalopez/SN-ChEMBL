from bottle import request, response
from SN_ChEMBL import config

class Authorize(object):
    name = 'authorize'
    api = 2

    def apply(self, fn, context):
        def _authorize(*args, **kwargs):
            if hasattr(request, 'forms') and 'token' in request.forms and request.forms['token'] == config.get('token'):
                return fn(*args, **kwargs)
            response.status = 401
            return "Not authorized"
        return _authorize
