from common import Node,Linklist



def remove_duplicate(link):
    currentnode=link.head

    while currentnode.next is not None:
        if currentnode.data==currentnode.next.data:
            newnode=currentnode.next.next
            currentnode.next=None
            currentnode.next=newnode
        else:
            currentnode=currentnode.next
    return link.head


firstnode=Node(2)
secondnode=Node(2)
thirdnode=Node(6)
fourthnode=Node(6)
fifthnode=Node(6)
sixthnode=Node(3)

link=Linklist()
link.insert(firstnode)
link.insert(secondnode)
link.insert(thirdnode)
link.insert(fourthnode)
link.insert(fifthnode)
link.insert(sixthnode)
remove_duplicate(link)
link.print_data()