# -*- coding: utf-8 -*-
#python3  file = f
import os

#定义变量A以及元素个数
i=0
A = ['1，Fastboot -W 压力测试',
'2，休眠唤醒压力测试',
'3，Recovery模式重启测试',
'4，WIFI开关压力测试',
'5，Monkey压力测试',
'6，Python调用shell脚本',
'7，判断文件是否存在',
'100, 其他测试']               

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
	for a in range(1,20000):
		#print("-----1，Fastboot -W 压力测试-----")
		#os.system('cat /proc/cupinfo')
		os.system('adb wait-for-device reboot bootloader')
		os.system('fastboot -w') #os.system 这个方法是直接调用标准C的system() 函数，仅仅在一个子终端运行系统命令，而不能获取命令执行后的返回信息。
		os.system('fastboot reboot')
		print("执行次数 %d"%a) # %字符：标记转换说明符的开始
		os.system('sleep 5')
elif temp == '2':
    for a in range(0,10):
		#print("-----2, 休眠唤醒压力测试-----")
        os.system('adb shell input keyevent 26')
        os.system('sleep 0.5')
        os.system('adb shell input keyevent 26')
        os.system('sleep 0.5')
        print("执行次数 %d"%(a+1))
elif temp == '3':
    for a in range(0,10):
        #print("-----3, Recovery模式重启测试-----")
        os.system('adb reboot recovery')
        os.system('sleep 15')
        os.system('adb reboot')
        print("执行次数 %d"%(a+1))
elif temp == '4':
    for a in range(0,10):
        #print("-----4, WIFI开关压力测试-----")
        os.system('adb shell input keyevent 26')
        os.system('sleep 0.5')
        os.system('adb shell svc wifi enable')
        os.system('sleep 0.5')
        os.system('adb shell svc wifi disable')
        os.system('sleep 0.5')
        os.system('adb shell input keyevent 26')
        print("执行次数 %d"%(a+1))
elif temp == '5':
    for a in range(0,10):
        #print("-----5, Monkey压力测试-----")
        os.system('adb shell monkey --ignore-timeouts --ignore-crashes --ignore-native-crashes --ignore-security-exceptions 10000')
        print("执行次数 %d"%(a+1))
elif temp == '6':
    print("-----6, Python调用shell脚本 开始-----")
#    file = os.popen('. /home/fujinhua/Python学习/test.sh') #绝对路径
#    print(file.read())
    os.system('./test.sh') #绝对路径与相对路径都可以
    print("-----6, Python调用shell脚本 完成-----")
elif temp == '7':
    print("-----7, 判断文件是否存在-----")
#第一种方法
    if os.access('test.sh',os.F_OK): # os.F_OK检查文件是否存在/os.R_OK检查文件是否可读/os.W_OK检查文件是否可以写入/os.X_OK检查文件是否可以执行   注意不能分别是文件还是文件夹
            print("-----文件是存在-----")
    else:
            print("-----文件是不存在-----")
#第二种方法
    try:
        f =open('test.sh')
        f.close()
    except IOError:  # Python3 FileNotFoundError/PersmissionError
        print("File is not found.")
#第三种方法
    path = './test/a/'
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path+' 创建成功')
    else:
        print(path+' 目录已存在')
else:
    print("-----3, 其他测试-----")
    output = os.popen('cat /proc/cpuinfo')  #os.popen 该方法不但执行命令还返回执行后的信息对象，是通过一个管道文件将结果返回。
    print(output.read())
