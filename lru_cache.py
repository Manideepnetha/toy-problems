import collections

class lru_cache:

    def __init__(self,capacity :int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def put(self,Key:int,Value:int):
        try:
            self.cache.pop(Key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last = False)
        self.cache[Key] = Value
    
    def get(self,Key:int):
        try:
            Value = self.cache.pop(Key)
            self.cache[Key] = Value
            return Value
        except KeyError:
            return 0
    
    def get_cache(self):
        return self.cache