class NewNode():
    def __init__(self,data,next= None):
        self.data = data
        self.next = next


class SingleLinkedList():

    """

    ---> head variable is used to refer the head_node of Linked list
    ---> data variable is used to store the data that need to be stored
    ---> val variable is used store the data of  particular node
    ---> ptr variable is used for traversing Linked List
    ---> preptr and temp is used to point before node and after node respectively
    ---> flag is used as check_pointer to check for a particular node

    """

    head = None

    @classmethod
    def display_linked_list(cls):
        ptr = cls.head

        if ptr is None:
            print("\n--------> Linked List is Empty <--------\n")
        else:
            while(ptr):
                print(ptr.data,end=" --> ")
                ptr = ptr.next
            print("None")


    @classmethod
    def add_at_ending(cls,data):   
        ptr = cls.head

        if ptr is None :
            node = NewNode(data)
            cls.head = node
        else:
            while(ptr.next != None):
                ptr = ptr.next
            node = NewNode(data)
            ptr.next = node
        

    @classmethod
    def add_at_beginning(cls,data):
        ptr = cls.head

        if ptr is None :
            node = NewNode(data)
            cls.head = node
        else:
            node = NewNode(data,cls.head)
            cls.head = node


    @classmethod
    def add_after_particular_node(cls,data,val):     
        ptr = cls.head

        if ptr is None:
            print("\n--------> Linked List is Empty <--------\n")
        else:
            flag = 0
            while(ptr.data != val):
                if ptr.next is None:
                    flag = 1
                    break
                ptr = ptr.next
            
            if flag == 1 :
                print(f"\n--------> No such node as {val} in Linked List <--------\n")
            else:
                temp = ptr.next
                node = NewNode(data,temp)
                ptr.next = node
                

    @classmethod
    def add_before_particular_node(cls,data,val):     
        ptr = cls.head

        if ptr is None :
            print("\n--------> Linked List is Empty <--------\n")
        else:

            if ptr.data == val :
                cls.add_at_beginning(data)
            else:
                flag = 0
                preptr = ptr
                while(ptr.data != val):
                    if ptr.next is None :
                        flag = 1
                        break
                    preptr = ptr
                    ptr = ptr.next

                if flag == 1 :
                    print(f"\n--------> No such node as {val} in Linked List <--------\n")
                else:
                    print(ptr.data)
                    node = NewNode(data,ptr)
                    preptr.next = node

    
    @classmethod
    def delete_at_beginning(cls):
        ptr = cls.head

        if ptr is None:
            print("\n--------> Linked List is Empty. So, we cant delete any node<--------\n")
        else:
            cls.head = ptr.next


    @classmethod
    def delete_at_ending(cls):
        ptr = cls.head
        
        if ptr is None:
            print("\n--------> Linked List is Empty. So, we cant delete any node<--------\n")
        else:
            if ptr.next is None:
                cls.head = None
            else:
                preptr = ptr
                while(ptr.next):
                    preptr=ptr
                    ptr = ptr.next
                preptr.next = None

    @classmethod
    def delete_particular_node(cls,val):
        ptr = cls.head

        if ptr is None:
            print("\n--------> Linked List is Empty. So, we cant delete any node<--------\n")
        else:
            if ptr.data == val:
                cls.head = ptr.next
            else:
                flag = 0
                preptr = ptr
                while(ptr.data != val):
                    if ptr.next == None:
                        flag = 1
                        break
                    preptr = ptr
                    ptr = ptr.next
                if flag == 1:
                    print(f"\n--------> No such node as {val} in Linked List to Delete <--------\n")
                else:
                    preptr.next = ptr.next


while(True):
    print("\n\n =====================================================================")
    print("1. Add an node \n2. Delete an node \n3. Display Linked List \n4. Exit or Stop")
    op = int(input("Select any one Option : "))

    match op :
        case 1 :
            print("\n\n ====================================================")
            print("1. Add at Beginning \n2. Add at Ending \n3. Add after a particular node \n4. Add before a particular node")
            op2 = int(input("Select any one option given above to add an node : "))
            print("\n\n ===============================")
            match op2 :
                case 1 :
                    data = input("\nEnter the data to be stored in the Linked List : ")
                    SingleLinkedList.add_at_beginning(data)
                case 2 :
                    data = input("\nEnter the data to be stored in the Linked List: ")
                    SingleLinkedList.add_at_ending(data)
                case 3 :
                    data = input("\nEnter the data to be stored in the Node : ")
                    val = input("After which particular node the data need to be stored in the Linked List : ")
                    SingleLinkedList.add_after_particular_node(data,val)
                case 4 :
                    data = input("\nEnter the data to be stored in the Node : ")
                    val = input("Before which particular node the data need to be stored in the Linked List : ")
                    SingleLinkedList.add_before_particular_node(data,val)
                case _ :
                    print("\n\n ================================        INVALID OPTION ---- SELECT CORRECT OPTION          =====================================\n\n")
        case 2 :
            print("\n\n ====================================================")
            print("1. Delete at Beginning \n2. Delete at Ending \n3. Delete a particular node")
            op2 = int(input("Select any one option given above to add an node : "))
            print("\n\n ===============================")
            match op2 :
                case 1 :
                    SingleLinkedList.delete_at_beginning()
                case 2 :
                    SingleLinkedList.delete_at_ending()
                case 3 :
                    val = input("which particular node need to be deleted from the Linked List : ")
                    SingleLinkedList.delete_particular_node(val)
                case _ :
                    print("\n\n ================================        INVALID OPTION ---- SELECT CORRECT OPTION         =====================================\n\n")
        case 3 :
            print("\n\n ================================        Linked List         =====================================\n\n",end = "\t\t\t")
            SingleLinkedList.display_linked_list()
        case 4 :
            break
        case _ :
            print("\n\n ================================        INVALID OPTION ---- SELECT CORRECT OPTION          =====================================\n\n")

