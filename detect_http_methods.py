import urllib3

HTTP_METHODS = [
    'GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS',
    'PATCH', 'TRACE', 'CONNECT'
]

class Detect_Http_Method:
    def __init__(self, url):
        self.__url = url
        self.__http = urllib3.PoolManager()
        self.__methods = {}

    def __send_request(self, method)->bool:
        response = self.__http.request(method, self.__url, timeout=3.0, retries=False)
        if response.status < 400:
            return True
        elif response.status != 405:
            return True
  
    def discover_http_methods(self)->dict:
        for method in HTTP_METHODS:
            if method not in self.__methods:
                self.__methods[method] = False
            try:
                if self.__send_request(method) == True:
                    self.__methods[method] = True
            except Exception as e:
                raise Exception(f"URL {self.__url} not found")
        return dict( sorted( self.__methods.items(), key=lambda x: (not x[1], x[0])))


        
