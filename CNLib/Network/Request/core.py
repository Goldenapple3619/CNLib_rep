from http import client
from json import loads, dumps

from .header import Header
from .constants import SSL_CONTEXT
from .body import Body

class Request(object):
    def __init__(self, url: str, method: str, header: Header = Header(), body: Body = Body(), timeout = 10, port: int = None, encoding: str = "utf-8", json_body: bool = True) -> None:
        self.url = url.strip('/')
        self.method = method
        self.json_body = json_body
        self.encoding = encoding

        self.connexion = client.HTTPSConnection(self.url.split('/')[0], timeout=timeout, port=port, context=SSL_CONTEXT)

        self.request_header = header
        self.request_body = body

        self.status = -1
        self.message = "not sended"

        self.response_header = Header()
        self.response_body = Body()

        self.redirected = self.url
    
    def call(self) -> None:
        self.connexion.request(self.method.upper(), '/' + '/'.join(self.url.split('/')[1:]), headers = self.request_header.data, body = self.request_body.to_string() if not self.json_body else dumps(self.request_body.data))
        response = self.connexion.getresponse()
        self.status = response.status
        self.message = response.reason
        self.response_header = Header(dict(response.headers.items()))
        self.response_body = response.read()
        if (self.encoding):
            self.response_body = self.response_body.decode(self.encoding, errors="ignore")
        response.close()

    def to_json(self) -> dict:
        return (loads(self.response_body))

    def close(self) -> None:
        self.connexion.close()

#R = Request("httpbin.org/post", "post", body=Body({"test": "test"}), header=Header({'Content-type': 'application/json'}, Accept="application/json, text/javascript, */*; q=0.01"))
#R.call()
#print(R.response_body)
#R.close()
#exit(0)