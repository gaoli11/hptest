#coding=utf-8
from xml.dom.minidom import parse
dom = parse('info.xml')
a = dom.documentElement
print(a.nodeName)
print(a.nodeValue)
print(a.nodeType)
print(a.ELEMENT_NODE)

# aa = a.getElementsByTagName('maxid')[0]
# print(aa.tagName)
# 
# bb = a.getElementsByTagName('caption')[2]
# print(bb.tagName)
# 
# cc = a.getElementsByTagName('item')[1]
# print(cc.tagName)

# aa = a.getElementsByTagName('login')[0]
# print(aa.getAttribute("username"))
# 
# bb = a.getElementsByTagName('login')[0]
# print(bb.getAttribute("password"))


aa = a.getElementsByTagName('maxid')[0]
print(aa.firstChild.data)

bb = a.getElementsByTagName('caption')[1]
print(bb.firstChild.data)