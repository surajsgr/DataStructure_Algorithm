"Identify Circular linklist"

from .common import Node,Linklist


class NewNode(Node):

    def __init__(self,data):
        super().__init__(data)
        self.is_visited=False


def check_circular(link):

    currentnode=link.head
    link.is_visited=True

    while True:

        if currentnode.next.is_visited==True:
            currentnode.next=None
            break

        else:

            currentnode=currentnode.next
            currentnode.is_visited=True


    # def check_circular(self):
    #
    #     currentnode=self.head
    #     count=0
    #
    #     while True:
    #
    #         if currentnode.next is None:
    #
    #
    #             break
    #
    #         else:
    #             # previousnode=currentnode
    #             currentnode=currentnode.next
    #             # nextnode=currentnode.next
    #             self.is_visited=True
    #
    #             if currentnode.is_vistied==True:
    #
    #                 count+=1
    #                 print("Link list is circular")
    #                 currentnode.next=None
    #
    #
    #
    #     return count


firstnode=NewNode("john")
secondnode=NewNode("Mary")
thirdnode=NewNode("Tom")


linked=Linklist()

linked.insert(firstnode)
linked.insert(secondnode)
linked.insert(thirdnode)
thirdnode.next=secondnode
check_circular(linked)
linked.print_data()

