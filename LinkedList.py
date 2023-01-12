#  John Daggs

#  10/22/2021

#  Purpose of LinkedList.py:
#  The purpose of this file is to contain a class named Doubly Linked List and Node.
#  This class will be designed and contain methods so that objects may be created from it and act in the nature of a
#  linked list, containing nodes (elements of the list with a data and a next pointer) where each node points to the
#  next item in the list as well as the data of the node.

#  collaborators/resources -
#  Class Notes/Powerpoint/Code Examples on Linked Lists and Doubly Linked Lists
#  LinkedList.py file given through Canvas

class Node:

    def __init__(self):
        ''' Class constructor. The function takes setdata as
        input and sets data and next. '''

        self.data = None
        self.next = None

    def __str__(self):
        ''' The __str__ function presents the Node object as a string.
        The function returns the data of the object. '''

        return str(self.data) # ? str()


class LinkedList:

    def __init__(self):
        ''' Class constructor. The function sets the head
        to None. The function also has a variable that keeps track of the
        size of the DoublyLinkedList. '''

        self.head = None
        self.list_size = 0

    # return True or False to indicate whether the linked list is empty or not
    def is_empty(self):
        ''' The function checks to see if the LinkedList object is empty.
        If it is empty, the function returns True. If not, the function
        returns False. '''

        return self.head is None

    # insert a new item at the front (head) of the list
    def add(self, item):
        ''' The function takes an item as input and adds that item to the
        head of the list. The function does not return a value. '''

        new = Node()
        new.data = item
        new.next = self.head
        self.head = new
        self.list_size += 1

    # add a new item to the end (tail) of the list
    def append(self, item):
        ''' The function takes an item as input and appends that item to the end of the
        LinkedList. The function has no return value. '''

        new = Node()
        new.data = item
        new.next = None
        if self.head is None:                           # handle the case where the list is empty
            self.head = new
        else:
            current = self.head
            while current.next is not None:             # walk to the end of the list
                current = current.next
            current.next = new
        self.list_size += 1

    # return a count of the number of items in the linked list
    def size(self):
        return self.list_size

    # return True or False to indicate whether 'item' exists in the linked list
    def search(self, item):
        ''' The function takes an item as input and searches the DoublyLinkedList for that
        item. If the function finds the item, then the function returns True. If not,
        it returns False. '''

        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next

        return found

    # remove 'item' from the linked list if it is in the list
    def remove(self, item):
        ''' The function takes an item as input and removes that item from the DoublyLinkedList.
        The function has no return value. If the item is not in the list, the function returns
        a string that tells the user. '''

        if self.head is not None:
            previous = None
            current = self.head
            found = False

            while current is not None and not found:
                if current.data == item:                # we found the node containing item we want to remove
                    found = True
                    self.list_size -= 1
                    if previous is None:                # handle the case where the item is at the head of the list
                        self.head = current.next
                    else:
                        previous.next = current.next    # in other cases, 'snip' out the node containing the item
                else:
                    previous = current
                    current = current.next

            if found == False: # The purpose of this if statement is to notify the user that the item was not removed.
                print('Item not found in LinkedList.')

    # remove an item from the list and return it.
    #   If pos=None, remove the last item from the list and return it
    #   If 0 <= pos <= list.size() -1, remove the item at pos and return it
    #   else, pos is invalid, so return None
    def pop(self, pos=None):
        ''' The function takes a number as input and pops that Node and returns
        the data in that Node. The default argument for the input is 0. The function
        finds the item in the list and removes that item. If an invalid position is
        passed, the function returns None. '''

        if self.head is None:
            return None

        if pos is not None and (not isinstance(pos, int) or pos < 0 or pos > self.list_size - 1):
            return None

        target = pos
        if pos is None:                     # calling pop() is the same as pop(list.size() - 1)
            target = self.list_size - 1

        previous = None
        current = self.head
        i = 0

        while i != target:                  # move current until it is at the index we want to pop
            previous = current
            current = current.next
            i += 1

        result = current.data
        if previous is None:                # this is true when we are popping the head of the list
            self.head = current.next
        else:
            previous.next = current.next    # 'snip' out the node to pop

        self.list_size -= 1
        return result

    # support iteration of the LinkedList class using while or for loops.
    def __iter__(self):
        ''' The function iterates over a LinkedList. The function works by starting at the
        head of the list and yields each item in the LinkedList as the function traverses
        the LinkedList. '''

        current = self.head
        while current is not None:
            yield current
            current = current.next
