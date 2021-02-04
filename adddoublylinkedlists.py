class ListNode:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next
        if prev is not None:
            self.prev.next = self
        if next is not None:
            self.next.prev = self

class DoublyLinkedList:
    def __init__(self, string = ''):
        self.string = string
        self.isReversed = False
        self.head = None
        self.tail = None
        self._length = 0
        if string is not None:
            for x in string:
                self.addLast(int (x))

    def addFirst(self, item):
        if self.isReversed == True:
            node1 = ListNode(item)
            node2 = ListNode(item, self.head)
            if self._length == 0:
                self.head = node1
                self.tail = node1
            else:
                node1.prev = self.head
                self.head = node2
        else:
            node1 = ListNode(item)
            node2 = ListNode(item, None, self.head)
            if self._length == 0:
                self.head = node1
                self.tail = self.head
            else:
                node2.next = self.head
                self.head = node2
        self._length += 1
        
    def addLast(self, item):
        if self.isReversed == True:
            node1 = ListNode(item)
            node2 = ListNode(item, None, self.tail)
            if self._length == 0:
                self.head = node1
                self.tail = self.head
            else:
                self.tail.prev = node2
                self.tail = node2
        else:
            node1 = ListNode(item)
            node2 = ListNode(item,self.tail)
            if self._length == 0:
                self.head = node1
                self.tail = self.head
            else:
                self.tail.next = node2
                self.tail = node2
        self._length += 1

    def reverse(self):
        if self.isReversed == True:
            node = self.head
            hold = node.next
            x = 0
            while x < self._length:
                if node.next == None:
                    node.next = node.next
                    node.prev = None
                    self.tail = node
                    node = node.next
                if node.prev == None:
                    hold = node.next
                    node.next = node.prev
                    node.prev = hold
                    self.head = node
                    break
                else:
                    hold = node.next
                    node.next = node.prev
                    node.prev = hold
                    node = node.next
        else:
            node = self.head
            hold = node.prev
            x = 0
            while x < self._length:
                if node.prev == None:
                    node.prev = node.next
                    node.next = None
                    self.tail = node
                    node = node.prev
                if node.next == None:
                    hold = node.prev
                    node.prev = node.next
                    node.next = hold
                    self.head = node
                    break
                else:
                    hold = node.prev
                    node.prev = node.next
                    node.next = hold
                    node = node.prev
        

    def fastReverse(self):
        hold = self.head
        self.head = self.tail
        self.tail = hold
        self.isReversed = True
        
    def __str__(self):
        prinstr = []
        while self.head != None:
            if self.head.value == 0:
                if self.isReversed == True:
                    self.head = self.head.prev
                else:
                    self.head = self.head.next
            else:
                prinstr.append(str(self.head.value))
                if self.isReversed == True:
                    self.head = self.head.prev
                else:
                    self.head = self.head.next
        final = "".join(prinstr)
        return final
    
    def __len__(self):
        return self._length

def sumlinkednumbers(dll1, dll2):
    sumlist = DoublyLinkedList()
    cur1 = dll1.tail
    cur2 = dll2.tail
    carry = 0
    while cur1 != None and cur2 != None:
        sumlist.addFirst((cur1.value+cur2.value+carry) % 10)
        carry = int((cur1.value+cur2.value)/10)
        if dll1.isReversed == True:
            cur1 = cur1.next
        else:
            cur1 = cur1.prev
        if dll2.isReversed ==True:
            cur2 = cur2.next
        else:
            cur2 = cur2.prev
    if cur1 == None and cur2 != None:
        while cur2 != None:
            sumlist.addFirst((carry + cur2.value) % 10)
            carry = int((cur2.value + carry) / 10)
            if dll2.isReversed == True:
                cur2 = cur2.next
            else:
                cur2 = cur2.prev
    elif cur2 == None and cur1 != None:
        while cur1 != None:
            sumlist.addFirst((carry + cur1.value) % 10)
            carry = int((cur1.value + carry) / 10)
            if dll1.isReversed == True:
                cur1 = cur1.next
            else:
                cur1 = cur1.prev
            
    return sumlist
