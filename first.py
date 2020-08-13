class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item


    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next


    def find(self, val):
        if (self.head == None):
            return
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None


    def find_all(self, val):
        if (self.head == None):
            return
        current = self.head
        element_list = []
        while (current is not None):
            if current.value == val:
                element_list.append(current.value)
                prev = current
                current = current.next
            else:
                current = current.next
        return element_list


    def delete_Node(self, val, all=False):
        if (self.head == None):
            return
        head_node = self.head
        if head_node is not None:
            if head_node.value==val:
                self.head = head_node.next
                head_node = None
                return
        while head_node is not None:
            if head_node.value==val:
                break
            last_value = head_node
            head_node = head_node.next
        if head_node == None:
            return
        last_value.next = head_node.next
        head_node = None


    def clean(self):
        node = self.head
        while node != None:
            self.__init__()
        else:
            pass 


    def len(self):
        self.length =0
        if self.head != None:
            self.length +=1
            current = self.head
            while current.next != None:
                current = current.next
                self.length +=1
        return self.length


    def insert(self, afterNode, newNode):
        if (self.head == None):
            return
        after_Node = self.head
        while after_Node is not None:
            if after_Node.value == afterNode:
                new_Node = Node(newNode)
                new_Node.next = after_Node.next
                after_Node.next = new_Node
                if new_Node.next == None:
                    self.last = new_Node.next
                break
            after_Node = after_Node.next
        else:
            after_Node = Node(newNode)
            after_Node.next = self.head
            self.head = after_Node
        return


    def add(self, x):
        if self.head == None:
            self.last = self.head = Node(x)
        else:
            self.last.next = self.last = Node(x)

print ('Тестирование Связанного списка')

l = LinkedList()

l.add(10)
l.add(20)
l.add(30)
l.add(40)
l.add(50)
l.add(60)
l.add(30)
l.add(60)
l.add(60)
l.add(20)

l.print_all_nodes( )

#print ('Связанный список после удаления узла со значением 20:')
l.delete_Node(20)
l.print_all_nodes( ) 


#print ('Связанный список - длина:')
length_ll = l.len()
#print(length_ll) 


#print ('Связанный список после вставки узла со значением 100:')
l.insert(30, 100)
l.print_all_nodes( )


#print ('Найдены все узлы со значением 60:')
find_value = l.find_all(60)
print(find_value)

#print ('Связанный список очищен:')
l.clean()
l.print_all_nodes( )
