class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


    def addAtStart(self,data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def insert(self,index,data):
        counter2 = 0
        counter = 0
        front = self.head

        temp = self.head
        new_node = Node(data)

        while front.next:

            if counter2 == index - 1:
                break
            counter2 += 1
            front = front.next


        while temp.next: #circular repetition
            if counter == index - 2:  # temp = 3
                temp.next = new_node
                break
            temp = temp.next

            counter += 1
        temp = temp.next
        temp.next =front

ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.addAtStart(3)
ll.insert(4,4)
ll.display()