# -*- coding: utf-8 -*-
"""Pythonbasicpractice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1In29l0o1FxJ2DbXdT2dyRNbHtnN8MVTP
"""

print("sayali")

a = {"name":"sachit"}
print(type(a))
b = ("sac",10)
c={"abc",10}
d=[10,11.5,"sayali"]
print(type(b[0]))
print(type(d[0]))
# print(type(c[0]))

1-2

abz=5

abz+abz

len("hello \n world")

1*85*0

x="hi this is string"

x.split()

c = "atsomestarbigskyinbluecolor"

print("this is a string {}".format("HELLLOO"))

print("this is {} {} {}".format("bag","new","beauty"))

print("this is {t} {n} {b}".format(b="bag",n="new",t="beauty"))

print("this is {1} {2} {0}".format("bag","new","beauty"))

result = 1000/77777
print("the result is {r:1.5f}".format(r=result))

myList = [1,2,3]

myList1=['STRING',100,23.2]
myList1[1:]

myList+myList1

myList1[0]="NewItem"
myList1.append("NewItem")

myList1

6*6

myList1.pop()

myList1.pop(1)

myList1.pop(-1)

numlist = [1,8,45,9,0,7]
numlist.sort()
numlist

numlist.reverse()
numlist

mydict = {'key1':23,'key2':[12,22,33],'key3':['item0','item1']}

mydict["key1"]

mydict["key3"][1].upper()

mydict["key2"].sort()
mydict["key2"]

d={'key1':{'nestkey1':11,'nestkey2':{'subnestkey1':"sayali",'subnestkey2':"sankhe"}},'key2':"dance"}

d["key1"]["nestkey2"]["subnestkey1"]

d.keys()

d.values()

list1=[x for x in 'word']
list1

list2 = [x**2 for x in range(0,12)]
list2