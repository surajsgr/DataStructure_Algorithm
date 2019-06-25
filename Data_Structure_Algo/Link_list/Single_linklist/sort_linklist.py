'''
Sort a linklist
'''


from common import Node,Linklist


def swap_nodes(link,previousnode,firstnode,nextnode):

    firstnode.next=nextnode.next
    nextnode.next=firstnode
    if firstnode is link.head:
        link.head=nextnode
        nextnode.next=firstnode
        return
    previousnode.next=nextnode


    # while True:
    #
    #     if currentnode==firstnode:
    #         previousfirstnode.next=nextnode
    #         afternextnode=nextnode.next
    #         nextnode.next=firstnode
    #         firstnode.next=afternextnode
    #         break
    #     else:
    #         previousfirstnode=currentnode
    #         currentnode=currentnode.next
    #



def sort_linklist(link):

    execution=link.length_linklist()-1


    i=0
    while execution!=0:
        currentnode = link.head
        previousnode=None
        iteration=execution
        while iteration!=0:
            if currentnode.data>currentnode.next.data:
               swap_nodes(link,previousnode,currentnode,currentnode.next)
               break
            else:
                previousnode=currentnode
                currentnode=currentnode.next
                iteration-=1
        execution-=1


firstnode=Node(4)
secondnode=Node(2)
thirdnode=Node(6)
fourthnode=Node(5)
# fifthnode=Node(9)
# sixthnode=Node(3)

link=Linklist()
link.insert(firstnode)
link.insert(secondnode)
link.insert(thirdnode)
link.insert(fourthnode)
# link.insert(fifthnode)
# link.insert(sixthnode)


sort_linklist(link)
link.print_data()
