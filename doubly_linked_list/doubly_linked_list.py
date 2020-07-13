"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    def __repr__(self):
        return f'ListNodeValue: {self.value}\nListNodePrev:\
            {self.prev.value if self.prev else None}\n\
                ListNodeNext: {self.next.value if self.next else None}\n'


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return
        else:
            # define new and old head
            new_head = new_node

            new_head.next = self.head
            self.head.prev = new_head
            self.head = new_head

            self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):  # fix
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # define new and old tail
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return
        else:
            # set new_tail pointer first

            new_tail = new_node

            new_tail.prev = self.tail
            self.tail.next = new_tail
            self.tail = new_tail

            self.length += 1

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):  # fix
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):  # fix
        # iterate through list checking nodes until you find it
        # set found_node.prev.next = found_node.next
        # set found_node.next.prev = found_node.prev
        current_node = self.head

        if current_node is None:
            return None

        while current_node is not None:
            if current_node == node:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
            current_node = current_node.next

        self.head.prev = node
        self.head.prev.next = self.head
        self.head = node

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):  # fix
        current_node = self.head

        if current_node is None:
            return None

        while current_node is not None:
            if current_node == node:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
            current_node = current_node.next

        self.tail.next = node
        self.tail.next.prev = self.head
        self.head = node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -= 1

        if self.head is self.tail:
            self.tail = None
            self.head = None

        elif node is self.head:
            self.head = self.head.next
            node.delete()

        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()

        else:
            node.delete()
        # current_node = self.head

        # if current_node is None:
        #     return

        # if self.length == 1 and current_node == node:
        #     self.head = None
        #     self.tail = None
        #     current_node = None

        # if self.length == 2 and current_node == node:
        #     self.head = current_node
        #     self.tail = current_node

        # while current_node is not None:
        #     if current_node is self.head and current_node == node:
        #         self.head = current_node.next
        #         self.head.prev = None
        #         break

        #     elif current_node is self.tail and current_node == node:
        #         self.tail = current_node.prev
        #         self.head.next = None
        #         break

        #     elif current_node == node:
        #         current_node.prev.next = current_node.next
        #         current_node.next.prev = current_node.prev
        #         break

        #     elif current_node.next is None:
        #         raise Exception("This shit is trash.")

        #     current_node = current_node.next

        # self.length -= 1
  
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head is None:
            return None

        current_node = self.head
        current_max = self.head

        while current_node is not None:
            if current_node.value > current_max.value:
                current_max = current_node
            current_node = current_node.next

        return current_max.value


dll = DoublyLinkedList()
dll.add_to_tail(1)
dll.add_to_head(9)
dll.add_to_tail(6)
