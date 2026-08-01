class MyHashMap:

    def __init__(self):
        self.li=[]

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.li)):
            if self.li[i][0] == key :
                self.li[i][1] = value 
                break
        else :
            self.li.append([key,value])

    def get(self, key: int) -> int:
        for i in range(len(self.li)) :
            if self.li[i][0] == key  :
                return self.li[i][1]
        return -1

    def remove(self, key: int) -> None:
        remove_index=-1
        for i in range (len(self.li)):
            if self.li[i][0]==key:
                remove_index=i
        if remove_index!=-1:
            self.li.pop(remove_index)        



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)