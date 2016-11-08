#coding=utf-8

#####################################################
#   Written By lsvih                                #
#   2016-11-07                                      #
#   Data structure: Stack&BiTree                    #
#####################################################

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items)==0

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def getTop(self):
        if not self.is_empty():
            return self.items[len(self.items)-1]

    def length(self):
        return len(self.items)

    def clear(self):
        self.__init__()

class BiTree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def clear(self):
        self.__init__()

    def is_empty(self):
        return self.value is None

    def depth(self,node):
        if node.value is None or node is None:
            return 0
        else:
            l_length = self.depth(node.left)
            r_length = self.depth(node.right)
            if l_length>=r_length:
                return l_length+1
            else:
                return r_length+1

    def value(self):
        return self.value

    def per_order_traverse(self, node):
        if node is None or node.value is None:
            return
        print node.value
        self.per_order_traverse(node.left)
        self.per_order_traverse(node.right)

    def in_order_traverse(self, node):
        if node is None or node.value is None:
            return
        self.in_order_traverse(node.left)
        print node.value
        self.in_order_traverse(node.right)

    def post_order_traverse(self, node):
        if node is None or node.value is None:
            return
        self.post_order_traverse(node.left)
        self.post_order_traverse(node.right)
        print node.value
