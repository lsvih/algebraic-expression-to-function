#coding=utf-8

#####################################################
#   Written By lsvih                                #
#   2016-11-07                                      #
#   Convert algebraic expression                    #
#       to functional expression                    #
#####################################################

from data import Stack
from data import BiTree
import sys

operators = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
operators_name = {'+':'add','-':'mius','*':'muilt','/':'divide','^':'power'}
def break_word(Exp):
    for op in operators:
        Exp = Exp.replace(op,'|'+op+'|')
    Exp = Exp.split('|')
    return [item for item in Exp if not item is ""]

def clear_brackets(exp):
    exp = break_word(exp)
    temp = Stack()
    result = Stack()
    for elem in exp:
        if elem not in operators:
            result.push(elem)
        else:
            if temp.length() is 0 or elem is '(':
                temp.push(elem)
            else:
                if elem is ')':
                    while temp.getTop() is not '(':
                        result.push(temp.pop())
                    temp.pop()
                elif operators[elem] < operators[temp.getTop()]:
                    while temp.length() is not 0:
                        if temp.getTop() is '(':
                            break
                        result.push(temp.pop())
                    temp.push(elem)
                else:
                    temp.push(elem)
    while temp.length() is not 0:
        result.push(temp.pop())
    return result

def expression_tree(Exp):
    origin = clear_brackets(Exp)
    temp = Stack()
    stack = Stack()
    while origin.length() is not 0: stack.push(origin.pop())
    while stack.length() is not 0:
        if stack.getTop() in operators:
            node = BiTree(stack.pop())
            node.right = temp.pop()
            node.left = temp.pop()
        else:
            node = BiTree(stack.pop())
        temp.push(node)
    return temp.pop()

def create_function_expression(Tree):
    if Tree.value in operators_name:
        Tree.value = operators_name[Tree.value] +'('+ create_function_expression(Tree.left) +','+ create_function_expression(Tree.right) +')'
    return Tree.value

if len(sys.argv) is 1:
    print "Usage:f2f.py {your expression}"
    print 'example:f2f.py "A+b-x*(12.13+51^y)^1.4121"'
else:
    print "input:"+sys.argv[1]
    print "output:"+create_function_expression(expression_tree(sys.argv[1]))

