class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at Head (O(1))
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2. Insert at End (O(n))
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:      # FIXED indentation
            last = last.next

        last.next = new_node  # FIXED indentation

    # 3. Display List
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 4. Delete by Value
    def delete_by_value(self, value):

        # Case 1: List empty
        if not self.head:
            return

        # Case 2: Delete head
        if self.head.data == value:
            self.head = self.head.next
            return

        # Case 3: Delete any middle node
        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next

        # If value not found
        if not temp.next:
            return

        # Skip the node to delete
        temp.next = temp.next.next


# -----------------------------
# TEST CODE
# -----------------------------
my_list = LinkedList()

my_list.insert_at_head(10)
my_list.insert_at_head(20)
my_list.insert_at_end(5)

print("Initial List:")
my_list.display() 

my_list.delete_by_value(15)
print("After Deleting 15:")
my_list.display()  