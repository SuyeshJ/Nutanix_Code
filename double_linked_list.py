class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class List:
    def __init__(self, data=None):
        self.init_list(data)

    def __str__(self):
        if self.head is None:
            return ''
        this = self.head
        elements = str(this.data)
        this = this.next
        while this:
            elements += '<-->' + str(this.data)
            this = this.next
        return elements

    def init_list(self, data=None):
        if data:
            self.head = self.tail = Node(data)
            self.len = 1
        else:
            self.head = self.tail = None
            self.len = 0

    def insert_at_head(self, data):
        if self.head is None:
            return self.init_list(data)

        node = Node(data, prev=None, next=self.head)
        self.head.prev = node
        self.head = node
        self.len += 1
        return True

    def append(self, data):
        if self.tail is None:
            return self.init_list(data)

        node = Node(data, prev=self.tail, next=None)
        self.tail.next = node
        self.tail = node
        self.len += 1
        return True

    def remove_at_head(self):
        if self.head is None:
            return False

        if self.len == 1:
            del self.head
            return self.init_list()

        this = self.head
        self.head = this.next
        self.head.prev = None
        del this
        self.len -= 1
        return True

    def remove_at_tail(self):
        if self.tail is None:
            return False

        if self.len == 1:
            del self.tail
            return self.init_list()

        this = self.tail
        self.tail = this.prev
        self.tail.next = None
        del this
        self.len -= 1
        return True

    def insert(self, index, data):
        '''
        1. Index starts at 0
        2. Support for zero, positive and negative index
        3. Support for out-of-bound postive and negative index

        Example:

        Consider the following list with 9 nodes.
        5<-->2<-->2<-->3<-->4<-->3<-->1<-->7<-->6

        a. Node 5 is at zero index,  -ve index: -9
        b. Node 2 is at +ve index 1, -ve index: -8
        so on....
        c. Node 6 is at +ve index 8, -ve index: -1

        out-of-bound index support:
        1. If an out-of-bound ( less than -10) -ve index is given, then the insertion will happen at head of the list
        2. if an out-of-bound (greater than 9) +ve index is given, then the insertion will happen at  end of the list
        '''
        if index >= (self.len-1) or index == -1:
            self.append(data)
            
        elif index <= 0-(self.len) or index == 0:
            self.insert_at_head(data)
            
        else:
            this = self.head
            prev = this.prev
            for iter in range(index):
                prev = this
                this = this.next
            node = Node(data, prev=this.prev, next=this)
            prev.next = node
            this.prev = node
            self.len += 1
        return True

    def remove(self, data):
        '''
        Remove the first occurance of the node which contains 'data'
        '''
        if self.head is None:
            return False
            
        elif self.head.data == data:
            self.remove_at_head()
            return True
            
        elif self.tail.data == data:
            self.remove_at_tail()
            return True
            
        this = self.head
        prev = this.prev
        while this:
            if this.data == data:
                prev.next = this.next
                this.next.prev = prev
                del this
                self.len -= 1
                return True
            else:
                prev = this
                this = this.next
                
        print(str(data)+" is not present in list")
        pass

    def remove_at(self, index):
        '''
        Remove the node at the given index.
        Support for zero, positive and negative index
        Support for out-of-bound index
        '''
        if index >= (self.len-1) or index == -1:
            self.remove_at_tail()
            return True
            
        elif index <= 0-(self.len) or index == 0:
            self.remove_at_head()
            return True
            
        else:
            this = self.head
            prev = this.prev
            for iter in range(index):
                prev = this
                this = this.next
            prev.next = this.next
            this.next.prev = prev
            del this
            self.len -= 1
            
        return True
        
dll = List()
dll.insert_at_head(5)
dll.append(2)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(3)
dll.insert(-10,10)
print(dll)
dll.remove(5)
print(dll)
dll.remove_at(10)
print(dll)
