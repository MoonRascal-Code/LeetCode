class ListNode:
    def __init__(self,key=None, value=None):
        self.key = key 
        self.value = value 
        self.next = None 

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
        
    def put(self, key: int, value: int) -> None:
        index = key % self.size

        if self.table[index].value is None:
            self.table[index] = ListNode(key,value)
            return 
        
        p = self.table[index]
        while p:
            # 업데이트 
            if p.key == key:
                p.value = value
                return 

            # 인덱스만 같고, key값만 다른 경우 1010, 10 
            if p.next is None:
                break 
            
            p = p.next 
        # 키체이닝 방식으로 
        p.next = ListNode(key,value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1 
        
        # 노드가 존재 할 때 
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value 
            
            p = p.next
        # while 문을 끝내고 나왔다면
        # talbe[index]에는 존재 하지만, key에 맞는 것이 없다는 이야기 
        return -1 

    def remove(self, key: int) -> None:
        index = key % self.size 
        if self.table[index].value is None:
            return 
        
        p = self.table[index]
        # 첫 번째 항목에서 바로 나온 경우
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return 
        
        # 두 번째 항목일 경우 
        prev = p 
        while p:
            if p.key == key:
                prev.next = p.next
                return 
            prev,p = p,p.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)