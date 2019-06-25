


class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.length=0


class Linklist():
    def __init__(self):
        self.head=None


    def insert(self,newNode):

        if self.head==None:
            self.head=newNode
        else:

            lastnode=self.head
            while True:
                if lastnode.next is None:
                    lastnode.next=newNode
                    break
                else:
                    lastnode=lastnode.next

            lastnode.next=newNode
    def insert_at_begining(self,newNode):

        if self.head is None:
            self.head=newNode
        else:

            first_node=self.head
            self.head=newNode
            newNode.next=first_node

    def insert_at_end(self,newNode):

        if self.head is None:
            self.head=newNode
        else:
            lastnode=self.head
            while True:
                if lastnode.next==None:
                    previousnode=lastnode
                    previousnode.next=newNode
                    break
                else:
                    lastnode=lastnode.next
    def insert_at_pos(self,pos,newNode):

        currentnode=self.head

        self.length=1
        while True:

            if self.length==pos-1:

                currentnode.next=newNode
                newNode.next=nextnode
                break
            else:
                # previousnode = currentnode
                currentnode=currentnode.next
                nextnode=currentnode.next

                self.length+=1




    def delete_at_begin(self):

        if self.head is None:
            print("Nothing to be deleted")
        else:

            currentnode=self.head
            nextnode=currentnode.next
            self.head=nextnode

    def delete_at_end(self):

        currentnode=self.head

        while True:

            if currentnode.next is None:
                previousnode.next=None
                break
            else:
                previousnode=currentnode
                currentnode=currentnode.next

    def delete_at_pos(self,pos):

        currentnode=self.head
        self.length=0
        while True:
            if self.length==pos-1:

                previousnode.next=currentnode.next
                break
            else:
                previousnode=currentnode
                currentnode=currentnode.next
                self.length+=1

    def print_data(self):

        if self.head is None:
            print("List is empty")
        else:
            currentnode=self.head
            while True:
                if currentnode==None:
                    break
                print(currentnode.data)
                currentnode=currentnode.next

    def length_linklist(self):

        currentnode=self.head

        self.length=1

        while True:

            if currentnode.next==None:

                break
            else:

                currentnode=currentnode.next
                self.length+=1

        return self.length




# #
# firstnode=Node("john")
# # secondnode=Node("Mary")
# # thirdnode=Node("Tom")
# # begining_node=Node("Rock")
# # last_node=Node("Ryan")
# # third_node=Node("Sam")
# #
# link=Linklist()
# #
# # link.insert(firstnode)
# # link.insert(secondnode)
# # link.insert(thirdnode)
# # link.insert_at_begining(begining_node)
# link.insert_at_end(firstnode)
# # link.insert_at_pos(3,third_node)
# # # # link.delete_at_begin()
# # # # link.delete_at_end()
# # # link.delete_at_pos(4)
# link.print_data()
# print(link.length_linklist())