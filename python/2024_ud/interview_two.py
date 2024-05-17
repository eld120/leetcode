from collections import deque



'''
class method that takes requests
requests can pass or fail
rate limiting (leaky bucket?)
on init, take a req per sec argument
3
'''

class RateLimiter:

    def __init__(self, rate) -> None:
        # actually the req/s upper limit
        self.upper_limit = rate
        self.database = []
        


    def response(self, request: int)-> bool:
        if len(self.database) == 0:        
            self.database.append(request)
            
            return True
        elif request - self.database[len(self.database)-1] < 1000:
            count = 0
            if count < self.upper_limit:
                for index in range(len(self.database)-1,0, -1):
                    if request - self.database[index] < 1000 :
                        count += 1
                    elif request - self.database[index] > 1000 and count < self.upper_limit:
                        self.database.append(request)
                        return True
                return False
        

    # target O(1) for a single run
    # target O(rate) for multiple runs


class WebApi:
    def __init__(self, rate: int) -> None:
        self.rate_limit = rate
        self.database = deque()
        self.head = None

    def purge_old_requests(self, request)-> None:
        while request - self.head > 1000 and self.database:
            head = self.database.popleft()
            if request - head < 1000:
                self.database.appendleft(head)
                self.head = head

    def response(self, request: int)-> bool:
        if self.head:
            self.purge_old_requests(request)
        if not self.database:
            self.database.append(request)
            self.head = request
            return True
        else:
            if request - self.head <= 1000 and len(self.database) < self.rate_limit:
                self.database.append(request)
                return True
        return False


def test_one():
    '''
    [1000, ]
    '''
    web_server = WebApi(2)
    assert web_server.response(1000) == True
    assert web_server.response(1001) == True
    assert web_server.response(1002) == False
    assert web_server.response(2000) == False
    assert web_server.response(3500) == True

def test_two():
    web_server = WebApi(4)
    assert web_server.response(1000) == True
    assert web_server.response(1001) == True
    assert web_server.response(1002) == True
    assert web_server.response(1003) == True
    assert web_server.response(1004) == False
    assert web_server.response(2004) == True
    assert web_server.response(2005) == True
    assert web_server.response(2006) == True
    assert web_server.response(2007) == True
    assert web_server.response(2008) == False
    assert web_server.response(2009) == False
    assert web_server.response(3500) == True
    assert web_server.response(3600) == True
    assert web_server.response(3700) == True
    assert web_server.response(4500) == True
