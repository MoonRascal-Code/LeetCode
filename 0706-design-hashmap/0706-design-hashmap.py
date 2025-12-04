class MyHashMap:
    def __init__(self):
        self.size = 1000 # bucket 
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size 

        if self.table[index].value is None:
            # 이전에 들어온 값이 없다! 
            self.table[index] = ListNode(key,value)
            return 
        # 이전에 들어온 값이 있다면, 
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value # 업데이트 
                return 
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key,value)

    def get(self, key: int) -> int:
        index = key % self.size

        if self.table[index].value is None:
            return -1 
        
        p = self.table[index] 
        while p:
            if p.key == key:
                return p.value 
            p = p.next 
        return -1  # index는 일치하지만, 일치하는 key가 없음 

    def remove(self, key: int) -> None:
        index = key % self.size 
        if self.table[index].value is None:
            return 
        
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return 
        
        prev = p 
        while p:
            if p.key == key:
                prev.next = p.next 
                return 
            
            prev,p=p,p.next 
class ListNode:
    def __init__(self,key=None,value=None):
        self.key = key
        self.value = value 
        self.next = None 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)