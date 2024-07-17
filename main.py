
def __main__(self, head, tail):
    head = self.head
    tail = self.tail
    
LL = LinkedList()
LL.insert(10)
LL.insert(25)
LL.insert(8)
LL.insert(12)
LL.insert(40)

# for traversal and printing linked list
def traverse_LL_and_print(head):
    temp = head
    
    while temp is not None:
        temp = temp.data, end=" "
        print(temp)
        temp = temp.next
    

#  for searching and printing number in linked list
def search_number(head, k):
    temp = head
    
    while head == 0 or head.next == 0:
        return False
        
    for i in range:
        if(temp[i] == k):
            return True
        else:
            return False
            
    traverse_LL_and_print(k)
    
# for ascending sort in linked list

def ascending_sort(LL, head):
    LL.sort()
    
    traverse_LL_and_print(LL)
    
# for descending sort in linked list

def descending_sort(LL, head):
    ascending_sort(LL)
    temp = head
    prev = None
    
    # reversing the ascending linked list
    while temp is not None:
        new_node = temp
        temp.next = prev
        prev = new_node
        temp = prev
        
    traverse_LL_and_print()
    
    
        
    
