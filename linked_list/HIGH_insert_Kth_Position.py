import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node):
    while node:
        print(str(node.data), end = " -> ")
        node = node.next


def insertNodeAtPosition(llist, data, position):
    reserved = llist
    # skip to the position we want to insert
    while llist and position > 1:
        llist = llist.next
        position -= 1

    tmp = llist.next    # save the next node before we insert
    aNewNode = SinglyLinkedListNode(data)    # create a new node to insert
    llist.next = aNewNode    # target the next node to the newly inserted node
    aNewNode.next = tmp    # then link to the saved node (tmp)
    return reserved


if __name__ == '__main__':
    llist_count = 3
    llist = SinglyLinkedList()

    llist_item = [16, 13, 7]                    #LINKED LIST: 16 -> 13 -> 7
    for i in llist_item:
        llist.insert_node(i)

    data = 1
    position = 2
    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head)        #OUTPUT:  16 -> 13 ->  1  -> 7

