class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.stack = []
        self.dict = {}

    def get(self, key: int) -> int:
        if key in self.dict:
            if self.stack:                  # if it is found in the stack
                self.stack.pop(0)           # remove it
                self.stack.append(key)      # then re-add, b/c we need to renew its position in the stack
            print(f'GET: {self.dict[key]}')
            return self.dict[key]
        else:
            print(f'GET: -1')
            return -1                       # if can't be found, return -1

    def put(self, key: int, value: int) -> None:
        if len(self.stack) < self.cap:      # if it still has capacity
            self.stack.append(key)          # append the data
            self.dict[key] = value
        else:                               # if it reaches its capacity
            lru = self.stack.pop(0)         # remove the oldest data in the stack
            self.stack.append(key)          # append the new data in the stack
            self.dict.pop(lru)              # don't forget to remove the data from dict
            self.dict[key] = value          # and re-add the new data into the dict



###
###TEST

capacity = 2

lru = LRUCache(capacity)
lru.put(1,1)
print(f'DICT: {lru.dict}')
lru.put(2,2)
print(f'DICT: {lru.dict}')
lru.get(1)
print(f'DICT: {lru.dict}')
lru.put(3,3)
print(f'DICT: {lru.dict}')
lru.get(2)
print(f'DICT: {lru.dict}')
lru.put(4,4)
print(f'DICT: {lru.dict}')
lru.get(1)
print(f'DICT: {lru.dict}')
lru.get(3)
print(f'DICT: {lru.dict}')
lru.get(4)
print(f'DICT: {lru.dict}')

