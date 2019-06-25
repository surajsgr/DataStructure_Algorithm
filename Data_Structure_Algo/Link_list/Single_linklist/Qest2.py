"Swap between two nodes if input data is given"

from common import Node,Linklist


def swapnode(link,first_data,second_data):

    currentnode=link.head
    previousfirstnode=None
    previoussecondnode=None

    while True:

        if currentnode.data==first_data:

            firstnode=currentnode
            break


        previousfirstnode=currentnode
        currentnode=currentnode.next

    currentnode=link.head

    while True:

        if currentnode.data==second_data:

            secondnode=currentnode
            break

        previoussecondnode=currentnode

        currentnode=currentnode.next

    if firstnode.data==link.head.data:
        nextsecondnode=secondnode.next
        link.head=secondnode
        secondnode.next=firstnode.next
        previoussecondnode.next=firstnode
        firstnode.next=nextsecondnode

    elif firstnode.next.data==secondnode.data:
        previousfirstnode.next=secondnode
        nextsecondnode=secondnode.next
        secondnode.next=firstnode
        firstnode.next=nextsecondnode



    else:
       previousfirstnode.next=secondnode
       nextsecondnode=secondnode.next
       secondnode.next=firstnode.next
       previoussecondnode.next=firstnode
       firstnode.next=nextsecondnode




firstnode=Node(4)
secondnode=Node(2)
thirdnode=Node(6)
fourthnode=Node(5)
fifthnode=Node(9)
sixthnode=Node(3)

link=Linklist()
link.insert(firstnode)
link.insert(secondnode)
link.insert(thirdnode)
link.insert(fourthnode)
link.insert(fifthnode)
link.insert(sixthnode)

swapnode(link,6,3)
link.print_data()






