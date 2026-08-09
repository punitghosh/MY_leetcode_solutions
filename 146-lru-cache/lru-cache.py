class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):

        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):

        node.prev = self.right.prev
        node.next = self.right

        self.right.prev.next = node
        self.right.prev = node

    def get(self, key):

        if key in self.cache:

            node = self.cache[key]

            self.remove(node)
            self.insert(node)

            return node.value

        return -1

    def put(self, key, value):

        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)

        self.cache[key] = node

        self.insert(node)

        if len(self.cache) > self.capacity:

            node = self.left.next

            self.remove(node)

            del self.cache[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)