# -*- coding: utf-8 -*-
f_read = open('menu_file','r',encoding='utf8')
#读取menu_file文件中的字符串，转换成字典类型数据并以对象接收
with f_read as f_read:
    geography_menu = eval(f_read.read().strip())
#测试读取数据是否为字典
# print(type(geography_menu))
# print(geography_menu['华中']['湖北'])
#定义一个动态字典来进行多级选择，并初始化为geography_menu
dynamic_dict = geography_menu
#定义一个用户列表来接收dynamic_dict的父字典的键，以便用户选择返回上级
dynamic_dict_super = []
#增删改查还没有保存在文件中
while True:
    print('欢迎使用'.center(50,'*'))
    for i in dynamic_dict:
        print('>>>',i)
    user_choice = input('请输入选择：输入你要查询的地区省市或新增[add]、修改[revise]、删除[delete]、返回上一级[q]').strip()
    #print(dynamic_dict)#测试当前屋为什么类型
    #查询
    if user_choice in dynamic_dict:
        dynamic_dict_super.append(dynamic_dict)
        if type(dynamic_dict) == list:
            print('你选择的城市为：',user_choice)
            break
        else:
            dynamic_dict = dynamic_dict[user_choice]
    #新增
    elif user_choice == 'add':
        user_add = input('请输入你要添加的省市区:').strip()
        if user_add in dynamic_dict:
            print('此项已存在，请重新输入：')
        else:
            if type(dynamic_dict) == list:
                dynamic_dict.append(user_add)#当类型为list时，需要判断
            else:
                dynamic_dict[user_add] = {}
            continue
    #修改
    elif user_choice == 'revise':
        user_revise = input('请输入你要修改的省市区:').strip()
        if user_revise in dynamic_dict:
            user_revise_after = input('修改为：').strip()
            print(type(dynamic_dict))
            if type(dynamic_dict) == list:#当类型为list时，需要判断
                dynamic_dict[dynamic_dict.index(user_revise)] = user_revise_after
            else:
                dynamic_dict[user_revise_after] = dynamic_dict[user_revise]
                del dynamic_dict[user_revise]
            continue
        else:
            print('此项不存在，请重新输入：')
    #删除
    elif user_choice == 'delete':
        user_delete = input('请输入你要删除的省市区:').strip()
        if user_delete in dynamic_dict:
            dynamic_dict_super.append(dynamic_dict)
            if type(dynamic_dict) == list:#当类型为list时，需要判断
                del dynamic_dict[dynamic_dict.index(user_delete)]
            else:
                del dynamic_dict[user_delete]
            continue
        else:
            print('此项不存在，请重新输入：')
    #返回上一级或退出
    elif user_choice == 'q':
        if dynamic_dict_super:
            dynamic_dict = dynamic_dict_super.pop()
        else:
            print('目前为最上级菜单，输入q后为退出系统！')
            break
    else:
        print("输入非法，请重新输入选择！")
if type(dynamic_dict) != list:
    with open('menu_file','w',encoding='utf8') as f:
        f.write(str(dynamic_dict))
