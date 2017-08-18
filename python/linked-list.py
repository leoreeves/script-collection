
class Node:

    next = None
    prev = None

    def __init__(self, data):
        self.data = data

class LinkedList:

    next = None

    def append(self, item):
        end = self
        while end.next:
            end = end.next

        node = Node(item)
        end.next = node
        node.prev = end

    def prepend(self, item):
        node = Node(item)
        node.next = self.next
        self.next = node

        if node.next:
            node.next.prev = node

        node.prev = self

    def add(self, item):
        current = self

        while current.next and current.next.data < item:
            current = current.next

        node = Node(item)
        node.next = current.next
        current.next = node

        if node.next:
            node.next.prev = node

        node.prev = current


    def has(self, item):
        current = self.next
        while current:
            if current.data == item:
                return True
            current = current.next

        return False

    def remove(self, item):
        current = self.next
        while current:
            if current.data == item:
                break
            current = current.next

        if current == None:
            return False

        if current.next:
            current.next.prev = current.prev

        if current.prev:
            current.prev.next = current.next

        return True

    def print_list(self):
        x = ''
        current = self.next
        while current:
            x += '->[' + str(current.data) + ']'
            current = current.next
        print('next:' + x)

        x = ''
        current = self.next
        while current and current.next:
            current = current.next
        while current and current != self:
            x += '->[' + str(current.data) + ']'
            current = current.prev
        print('prev:' + x)


ll = LinkedList()

ll.add(3)
ll.add(2)
ll.add(1)
ll.print_list()
print(ll.has(1))
ll.remove(2)
ll.remove(1)
ll.print_list()
ll.remove(4)