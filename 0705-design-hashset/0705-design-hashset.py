class MyHashSet:

    def __init__(self):
        self.buckets = [[] for _ in range(10 ** 6)]

    def hash(self,key):
        return key % len(self.buckets)
        
    def add(self, key: int) -> None:
        i = self.hash(key)
        if key not in self.buckets[i]:
            self.buckets[i].append(key)
    
    def remove(self, key: int) -> None:
        i = self.hash(key)
        if key in self.buckets[i]:
            self.buckets[i].remove(key)
        
    def contains(self, key: int) -> bool:
         i = self.hash(key)
         return key in self.buckets[i]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)