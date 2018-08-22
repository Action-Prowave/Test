# -*- coding: utf-8 -*-
#python3  file = f

#定义变量A，默认有3个元素
i=0
A = ['1，完整升级',
'2，升级AP',
'3, 升级MP',
'4，boot',
'5，system',
'6，userdata',
'7，recovery',
'8，splash6',
'9，cache',
'a，persist',
'b，emmc',
'q，退出']               

print("-----请选择你要进行的操作，然后按回车-----")
print("")
for tempName in A:
    print(tempName)

#提示、并选择操作
temp = raw_input('        请选择：')   #python2  raw_input ==>python3 input
	#import getpass
	#temp = getpass.getpass("        请选择：")
	#print(temp)
if temp == '1':
    print("-----1，完整升级-----")
elif temp == '2':
    print("-----2, 升级AP-----")
else:
    print("-----3, 升级MP-----")
