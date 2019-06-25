'''
Sort a linklist
'''


from common import Node,Link_list


def swap_nodes(link,firstnode,nextnode):

    currentnode=link.head

    if link.head==firstnode:
        link.head=nextnode
        afternextnode=nextnode.next
        nextnode.next=firstnode


    while True:

        if currentnode==firstnode:
            previousfirstnode.next=nextnode
            afternextnode=nextnode.next
            nextnode.next=firstnode
            firstnode.next=afternextnode
            break
        else:
            previousfirstnode=currentnode
            currentnode=currentnode.next




def sort_linklist(link):
    currentnode=link.head
    execution=Link_list.length_linklist()
    exchange=execution-1
    i=0
    while i<=execution-1:
        j=0
        while j<=exchange-1:
            if currentnode>currentnode.next:
               swap_nodes(currentnode,currentnode.next)
               break
            else:
                currentnode=currentnode.next

