#  John Daggs

#  10/22/2021

#  Purpose of DoublyLinkedList.py:
#  The purpose of this file is to contain a class named Doubly Linked List and Node.
#  This class will be designed and contain methods so that objects may be created from it and act in the nature of a
#  doubly linked list, containing nodes (elements of the doubly linked list that contain a data, next, and previous
#  pointer) where each node points to the next item in the list as well as the previous item in the list and the data of
#  the node.

#  collaborators/resources -
#  Class Notes/Powerpoint/Code Examples on Linked Lists and Doubly Linked Lists


class Node(object):
    def __init__(self):
        '''   the class constructor; initializes self.data, self.next, and self.previous variables. '''

        self.data = None
        self.next = None
        self.previous = None

    def __str__(self):
        ''' The __str__ function presents the Node object as a string.
        returns self.data of the object. '''

        return str(self.data)  # ? str()Node.


class DoublyLinkedList(object):
    def __init__(self):
        ''' the class constructor. Initializes self.head, which keeps track of the Node at the head of the list
            , and self.tail, which keeps track of the Node at the end of the list '''
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):  # this built-in method will allow you to loop over your list with a for or while loop. Note
        # that this method assumes the head of your list is stored in self.head and that each of your Nodes has a next
        # class variable that points to the subsequent Node.
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def is_empty(self):
        ''' returns True if the list is empty, False otherwise '''
        if self.length == 0:  # will be true if is empty
            return True
        else:               # not empty
            return False

    def size(self):
        '''  returns the number of items in the list, the size, using the length variable '''
        return self.length  # length is updated in other methods as items are added and removed form the list, returning
                            # it will give the size of the doubly linked list

    def add(self, item):
        ''' Adds item to the head of the list. Assuming that the item is not already in the list.
        This method does not return anything. '''
        newNode = Node()   # creating node
        newNode.data = item  # setting data of the new node equal to the item being added
        if self.is_empty():  # if list is empty
            self.head = newNode  # head and tail both equal to same newNode
            self.tail = newNode
        else:              # list not empty
            newNode.next = self.head  # newNode.next pointer will point to head
            self.head.previous = newNode  # head.previous pointer will point to newNode
            self.head = newNode  # the new node is the new head of the list
        self.length += 1  # update length

    def append(self, item):
        ''' adds item to the tail of the list. This method does not return anything and Assumes the item is not already
        in the list. '''
        newNode = Node()  # creating new Node
        newNode.data = item  # setting data of new node equal to item being added
        if self.length == 0:   # if list is empty
            self.head = newNode  # tail and head will be same, both set to newNode
            self.tail = newNode
        else:   # if list if not empty, append to end of list
            newNode.previous = self.tail  # newNode.previous pointer points to the tail
            self.tail.next = newNode   # current tail.next pointer now points to newNode
            self.tail = newNode    # newNode is now the tail
        self.length += 1    # updating length

    def pop(self, pos=None):
        ''' removes the last node from the list and returns its data, Assuming the list has at least one item. '''
        # pop(pos) can be called because of the default argument value, pos.
        # removing the node in the doubly linked list at the position value passed to pos
        target = pos
        if self.head is None:
            return None
        if pos is not None and (not isinstance(pos, int) or pos < 0 or pos > self.length - 1):  # if the position . . .
            return None  # . . . given is not an integer . . . returning None
        if pos is None:  # if no value passed to pos
            target = self.length - 1  # calling pop() is the same as pop(list.size() - 1)
        if pos is None:  # popping if no position given, popping the tail by default
            data = self.tail.data  # data variable set equal to tail,data
            # if self.tail.next is None:  # this is true when we are popping the tail of the list
            #     self.tail = self.tail.previous
            # else:
            #     self.tail = self.tail.previous  # 'snip' out the node to pop
            self.remove(self.tail.data)  # removing tail
            # self.length -= 1
            return data    #returning data
        else:  # if a position is given
            current = self.head  # setting current
            i = 0   # iterator
            while i != target:  # move current until it is at the index we want to pop
                self.head.previous = current
                current = current.next
                i += 1  # add to iterator
            data = current.data  # setting data being popped to the data of current.data
            self.remove(current.data)   # remove node with current.data from list
            return data  # returning the data that was popped

    def remove(self, item):
        '''removes the item from the list. This method does not return anything.
        Assuming the item is present in the list.'''
        self.length -= 1  # decreasing the length b/c are removing
        if not self.head and not self.tail:  # no head or tail, list is empty
            return
        # if type(item) is str:
        #     if item == self.head.data:
        #         self.head = self.head.next
        #         self.head.previous = None
        #         return
        #     if item == self.tail.data:
        #         self.tail = self.tail.previous
        #         self.tail.next = None
        #         return
        if self.head == self.tail:  # only one element, removes by setting equal to None
            self.head = None
            self.tail = None
        elif self.head.data == item:   # if item matches the data in head
            self.head = self.head.next  # removing head node, 1. setting head to the node being pointed to by
            self.head.previous = None   # self.head.next and 2. setting self.head.previous to None
        elif self.tail.data == item:  # if the item matches self.tail.data
            self.tail = self.tail.previous  # removing tail node by 1. setting the tail equal to what is being pointed
            self.tail.next = None          # to previously by the tail and 2. making sure tail.next points to none
        else:
            current = self.head
            while current.data is not item:  # move current until it is at the index we want to pop
                self.head.previous = current
                current = current.next
            current.previous.next = current.next
            current.next.previous = current. previous

    def search(self, item):
        ''' searches for the item in the list. This method returns True if the item is in the list, and False otherwise.
        The list may be empty.'''
        searchNode = Node()  # creating a node
        searchNode.data = item  # using item and setting the data of the node equal to it so it can be searched for
        if not self.head and not self.tail:
            return None
        if self.head.data == searchNode.data:  # data matches head.data, True
            return True
        elif self.tail.data == searchNode.data:  # data matches tail.tat, True
            return True
        else:               # if not at head or tail and have to search
            current = self.head  # setting a current variable
            i = 0  # iterator
            while current is not item and i < self.length:  # move current until it is at the index we are searching
                current = current.next
                i += 1
            if current == item:  # will be true if the item was found in the list
                return True
            else:                  # item was not found
                return False




