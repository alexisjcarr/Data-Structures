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
        if self.length == 0:
            self.head = ListNode(value)
            self.tail = ListNode(value)
        # define new and old head
        new_head = ListNode(value)
        old_head = self.head

        # make new_head self.head
        self.head = new_head
        # make new_head.next = old_head
        self.head.next = old_head
        # make old_head.prev = new_head
        old_head.prev = self.head

        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self): # fix
        if self.length == 0:
            return
        # save self.head to removed_node
        removed_node = self.head
        # set self.head to self.head_next
        self.head = removed_node.next
        # set new head's prev to none
        removed_node.prev = None

        self.length -= 1

        return removed_node

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # define new and old tail
        if self.length == 0:
            self.head = ListNode(value)
            self.tail = ListNode(value)

        new_tail = ListNode(value)
        old_tail = self.tail

        self.tail = new_tail
        self.tail.prev = old_tail
        old_tail.next = self.tail

        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self): # fix
        # self.tail.prev is new tail
        if self.length == 0:
            return None

        old_tail = self.tail
        self.tail = old_tail.prev
        self.tail.next = None

        self.length -= 1

        return old_tail

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node): # fix
        # iterate through list checking values until you find it
        # set found_node.prev.next = found_node.next
        # set found_node.next.prev = found_node.prev
        current_node = self.head

        if current_node is None:
            return None

        while current_node is not None:
            if current_node.value == node.value:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
            current_node = current_node.next
        
        old_head = self.head
        old_head.prev = node
        self.head = node
        self.head.next = old_head

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node): # fix
        current_node = self.head

        if current_node is None:
            return None

        while current_node is not None:
            if current_node.value == node.value:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
            current_node = current_node.next
        
        old_tail = self.tail
        old_tail.next = node
        self.tail = node
        self.tail.prev = old_tail

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node): # fix
        current_node = self.head

        if current_node is None:
            return

        if self.length == 1 and current_node == node:
            self.head = None
            self.tail = None
            current_node = None

        while current_node is not None:
            if current_node is self.head and current_node == node:
                current_node.prev = None
                self.head = current_node.next

            elif current_node is self.tail and current_node == node:
                current_node.next = None
                self.tail = current_node.prev

            elif current_node == node:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev

            current_node = current_node.next

        self.length -= 1
        
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
