from common import Node,Linklist





def merge(link_merge,link1,link2):

    currentfirstnode=link1.head
    currentsecondnode=link2.head

    while True:

        if currentfirstnode is None:

            link_merge.insert_at_end(currentsecondnode)
            break
        if currentsecondnode is None:

            link_merge.insert_at_end(currentfirstnode)
            break

        if currentfirstnode.data<currentsecondnode.data:

            firstnextnode=currentfirstnode.next
            currentfirstnode.next=None

            link_merge.insert_at_end(currentfirstnode)
            currentfirstnode=firstnextnode


        else:

            secondnextnode=currentsecondnode.next
            currentsecondnode.next=None
            link_merge.insert_at_end(currentsecondnode)
            currentsecondnode=secondnextnode





firstnode=Node(2)
secondnode=Node(5)
thirdnode=Node(6)
fourthnode=Node(1)
fifthnode=Node(4)
sixthnode=Node(9)

link1=Linklist()
link2=Linklist()
merge_link=Linklist()

link1.insert(firstnode)
link1.insert(secondnode)
link1.insert(thirdnode)

link2.insert(fourthnode)
link2.insert(fifthnode)
link2.insert(sixthnode)

merge(merge_link,link1,link2)
del link1
del link2
merge_link.print_data()



