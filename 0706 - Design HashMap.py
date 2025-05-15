class MyHashMap:

    def __init__(self):
        self.list =  []

    def put(self, key: int, value: int) -> None:
        v = True
        for index, element in enumerate(self.list):
            if element[0] == key:
                self.list[index][1] = value
                v = False
        if v:
            self.list.append([key, value])

    def get(self, key: int) -> int:
        value = -1
        for element in self.list:
            if element[0] == key:
                return element[1]
        return value

    def remove(self, key: int) -> None:
        for index, element in enumerate(self.list):
            if element[0] == key:
                self.list.pop(index)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)