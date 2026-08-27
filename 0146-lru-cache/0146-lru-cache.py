class LRUCache:
    class Node:
        def __init__(self, _key, _value):
            self.key = _key
            self.value = _value   #Node address
            self.next = None
            self.prev = None
    def __init__(self, capacity: int):
        self.head = self.Node(-1,-1)    #Dummyhead
        self.tail = self.Node(-1,-1)    #Dummytail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
        self.map = {}
    
    def deleteNode(self, Node): #Function to delete a node
        nextnode = Node.next
        prevnode = Node.prev
        nextnode.prev = prevnode
        prevnode.next = nextnode
    
    def insertafterhead(self, Node):    #Function to insert the node after head
        temp = self.head.next
        Node.next = temp
        Node.prev = self.head
        self.head.next = Node
        temp.prev = Node

    def get(self, key: int) -> int:
        if key in self.map:
            resNode = self.map[key]
            res = resNode.value
            del self.map[key]   #Deletes the entry in the map for that key
            self.deleteNode(resNode)
            self.insertafterhead(resNode)
            self.map[key] = self.head.next  #Updates the map
            return res
        return -1

    def put(self, key: int, value: int) -> None:
        # If key already exists
        if key in self.map:
            existingNode = self.map[key]
            del self.map[key]
            self.deleteNode(existingNode)
        # If capacity reached
        if len(self.map) == self.cap:
            del self.map[self.tail.prev.key]
            self.deleteNode(self.tail.prev)
        # Insert new node at front
        self.insertafterhead(self.Node(key, value))
        self.map[key] = self.head.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)