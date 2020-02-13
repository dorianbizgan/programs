def queue_with_linked_list():
    
    # queue using linked list 
    
    class node:
        def __init__(self, data, next):
            self.data = data
            self.next = next
        def __repr__(self):
            return(str(self.data))
            
    class queue:
        
        def __init__(self):
            self.first = None
            self.last = None
        
        def enqueue(self, data):
            temp = node(data, None)
            
            if self.first == None:
                self.first = temp
            
            else:
                if self.last == None:
                    self.last = temp
                    self.first.next = temp
                else:
                    self.last.next = temp
                    self.last = temp
        def dequeue(self):
            if self.first == None:
                self.last = None
                return(None)
            else:
                temp = self.first
                self.first = self.first.next
                return(temp)
            

            
        def __str__(self):
            temp = ""
            cur_node = self.first
            
            while cur_node != None:
                temp += str(cur_node.data) + " "
                cur_node = cur_node.next
            return(temp)
    
    
    # Initializations
    user_in = None
    mode = "enqueue"
    q = queue()
    
    print("Enter value use want to add. \nEnter 'shift' to change mode from enqueue or dequeue. \nEnter 'Exit' to exit program.")
    while user_in != "Exit":
        print(q)
        user_in = input()
        if user_in == "shift":
            if mode == "enqueue":
                mode = "dequeue"
            else:
                mode = "enqueue"
            print("Current mode is:",mode)
        
        elif user_in == "Exit":
            break
            
        else:
            if mode == "enqueue":
                q.enqueue(user_in)
            else:
                q.dequeue()
        
        
                
            
 

queue_with_linked_list()