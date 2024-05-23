import datetime
from collections import OrderedDict


class LFUCache:
    '''
    Implement the LFUCache class:

    LFUCache(int capacity) Initializes the object with the capacity of the data structure.

    int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
    
    void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. 
    When the cache reaches its capacity, it should invalidate and remove the least frequently used key before i
    nserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), t
    he least recently used key would be invalidated.
    '''
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = OrderedDict()
        # track key, value, frequency, and timestamp?
        # {key: key, value: value, frequency: int, timestamp: float}

    def get(self, key: int) -> int:
        if key in self.lookup:
            self.lookup[key]['frequency'] += 1
            self.lookup[key]['timestamp'] = datetime.datetime.now()
            self.lookup.move_to_end(key, last=False)
            return self.lookup[key]['value']
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.lookup[key]['frequency'] += 1
            self.lookup[key]['timestamp'] = datetime.datetime.now()
            self.lookup[key]['value'] = value
            self.lookup.move_to_end(key, last=False)
        else:
            self.lookup[key] = {
                'key': key,
                'value': value,
                'frequency' : 0,
                'timestamp' : datetime.datetime.now(),
            }
            self.lookup.move_to_end(key, last=False)
            if len(self.lookup) > self.capacity:
                lowest_freq = float('inf')
                least_frequently_used_objects = []
                for key, obj in self.lookup.items():
                    if obj['frequency'] < lowest_freq:
                        least_frequently_used_objects = []
                        lowest_freq = obj['frequency']
                        least_frequently_used_objects.append(obj)
                    elif obj['frequency'] == lowest_freq:
                        least_frequently_used_objects.append(obj)
                if len(least_frequently_used_objects) > 1:
                    least_recent = 0
                    remove_me = None
                    for obj in least_frequently_used_objects:
                        if obj['timestamp'] > least_recent:
                            remove_me = obj
                    del self.lookup[remove_me['key']]
                else:
                    del self.lookup[least_frequently_used_objects[0]['key']]



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)