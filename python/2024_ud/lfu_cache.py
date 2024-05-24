import datetime
from collections import OrderedDict, defaultdict


# class LFUCache:
#     '''
#     works but doesn't meet the O(1) average time complexity 
#     '''
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.lookup = OrderedDict()
#         # track key, value, frequency, and timestamp?
#         # {key: key, value: value, frequency: int, timestamp: float}
#         self.timestamp = 0

#     def get(self, key: int) -> int:
#         if key in self.lookup:
#             self.lookup[key]['frequency'] += 1
#             self.lookup[key]['timestamp'] = self.timestamp
#             self.timestamp += 1
#             self.lookup.move_to_end(key, last=False)
#             return self.lookup[key]['value']
#         return -1
        

#     def put(self, key: int, value: int) -> None:
#         if key in self.lookup:
#             self.lookup[key]['frequency'] += 1
#             self.lookup[key]['timestamp'] = self.timestamp
#             self.timestamp += 1
#             self.lookup[key]['value'] = value
#             self.lookup.move_to_end(key, last=False)
#         else:
#             if len(self.lookup) == self.capacity:
#                 lowest_freq = float('inf')
#                 least_frequently_used_objects = []
#                 for _, obj in self.lookup.items():
#                     if obj['frequency'] < lowest_freq:
#                         least_frequently_used_objects = []
#                         lowest_freq = obj['frequency']
#                         least_frequently_used_objects.append(obj)
#                     elif obj['frequency'] == lowest_freq:
#                         least_frequently_used_objects.append(obj)
#                 if len(least_frequently_used_objects) > 1:
#                     oldest_record = float('inf')
#                     remove_me = None
#                     for obj in least_frequently_used_objects:
#                         if obj['timestamp'] < oldest_record:
#                             oldest_record = obj['timestamp']
#                             remove_me = obj
#                     #breakpoint()
#                     del self.lookup[remove_me['key']]
#                 else:
#                     #breakpoint()
#                     del self.lookup[least_frequently_used_objects[0]['key']]
#             self.lookup[key] = {
#                 'key': key,
#                 'value': value,
#                 'frequency' : 1,
#                 'timestamp' : self.timestamp
#             }
#             self.timestamp += 1
#             self.lookup.move_to_end(key, last=False)
            


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
        self.timestamp = 0
        self.frequencies = defaultdict(set)
        self.lowest_frequency = float('inf')

    def get(self, key: int) -> int:
        
        if key in self.lookup:
            self.frequencies[self.lookup[key]['frequency']].remove(key)
            self.lookup[key]['frequency'] += 1
            self.lowest_frequency = min(self.lowest_frequency, self.lookup[key]['frequency'] )
            
            self.frequencies[self.lookup[key]['frequency']].add(key)
            self.lookup[key]['timestamp'] = self.timestamp
            self.timestamp += 1
            self.lookup.move_to_end(key, last=False)
            return self.lookup[key]['value']
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.lookup:
            self.frequencies[self.lookup[key]['frequency']].remove(key)
            self.lookup[key]['frequency'] += 1
            self.frequencies[self.lookup[key]['frequency']].add(key)
            self.lowest_frequency = min(self.lowest_frequency, self.lookup[key]['frequency'] )
            self.lookup[key]['timestamp'] = self.timestamp
            self.timestamp += 1
            self.lookup[key]['value'] = value
            self.lookup.move_to_end(key, last=False)
        else:
            if len(self.lookup) == self.capacity:
                # need to maintain the lowest item and the lowest frequency as things are added removed. I'm tired
                least_frequent = self.frequencies[self.lowest_frequency]
                if len(least_frequent) > 1:
                    oldest_record = float('inf')
                    remove_this = None
                    #
                    for k, v in least_frequent.items():
                        if v['timestamp'] < oldest_record:
                            oldest_record = v['timestamp']
                            remove_this = v
                    
                    self.frequencies[remove_this['frequency']].remove(remove_this['key'])
                    
                    del self.lookup[remove_this['key']]
                else:
                    #breakpoint()
                    obj = self.lookup[list(least_frequent)[0]]
                    self.frequencies[obj['frequency']].remove(obj['key'])
                    if not self.frequencies[obj['frequency']]:
                        self.lowest_frequency += 1
                    del self.lookup[obj['key']]
            self.lookup[key] = {
                'key': key,
                'value': value,
                'frequency' : 1,
                'timestamp' : self.timestamp
            }
            self.frequencies[self.lookup[key]['frequency']].add(key)
            self.lowest_frequency = self.lookup[key]['frequency']
            self.timestamp += 1
            self.lookup.move_to_end(key, last=False)
            


'''
{1: {2: 2}, 
2: {1: {'key': 1, 'value': 1, 'frequency': 2, 'timestamp': 2}, 
3: {'key': 3, 'value': 3, 'frequency': 2, 'timestamp': 4}}})
'''
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def test_example():
    cache = LFUCache(2)
    input_array = [[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
    answer_array = [None,None,1,None,-1,3,None,-1,3,4]
    for index, val in enumerate(input_array):
        if len(val) == 1:
            
            assert cache.get(val[0]) == answer_array[index]
        else:
            assert cache.put(val[0], val[1]) == answer_array[index]

