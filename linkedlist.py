class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = Node()

    def append(self, append_element):
        current = self.head
        while current.next:
            current = current.next
        current.next = append_element

    def length(self):
        current = self.head
        total = 0
        while current.next:
            current = current.next
            total += 1
        return total

    def display(self):
        current = self.head
        elements = []
        while current.next:
            current = current.next
            elements.append(current.data)
        print(elements)

    def get(self, index):
        current = self.head
        current_index = 0
        if index >= self.length():
            return None
        while current.next:
            current = current.next
            if current_index == index:
                return current.data
            current_index += 1

    def erase(self, index):
        current = self.head
        current_index = 0
        if index >= self.length():
            return None
        while True:
            previous = current
            current = current.next
            if current_index == index:
                previous.next = current.next
                return
            current_index += 1

#     def insert_first(self, first_element):
#         first_element.next = self.head
#         self.head = first_element

#     def delete_first(self):
#         if self.head:
#             deleted_element = self.head
#             temp = deleted_element.next
#             self.head = temp
#             return deleted_element
#         else:
#             return None

# class Stack(object):
#     def __init__(self, top=None):
#         self.ls = LinkedList()

#     def push(self, first_element):
#         self.ls.insert_first(first_element)

#     def pop(self):
#         self.ls.delete_first()


go = Node("GO")
drink = Node("DRINK")
fly = Node("FLY")
smart = Node("SMART")

ls = LinkedList()
ls.append(go)
ls.append(drink)
ls.append(fly)
ls.append(smart)

print(ls.head.data)
print(ls.head.next.data)
print(ls.head.next.next.data)

print(ls.length())
ls.display()

print(ls.get(0))    # GO
ls.erase(1)         # DRINK ERASED
ls.display()