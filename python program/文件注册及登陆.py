# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:52:16 2020

@author: lenovo
"""
import os
def is_first_start():     #判断是否为首次使用系统
    flag=open('D:\桌面\新建文件夹\我在这里！！.txt')
    word=flag.read()
    if word== "0":
        print("首次启动")
        flag.close()      #关闭文件
        c_flag()    #更改标志为1
        init()      #初始化资源
        print_login_menu() #打印登陆菜单
        user_select()      #选择用户
    elif word=="1":
        print("欢迎回来！")
        print_login_menu()
        user_select()
    else:
        print("初始化参数错误！")
#更改标志位
def c_flag():
    f= open("D:\桌面\新建文件夹\我在这里！！.txt","w")
    f.write("1")
    f.close()
#初始化管理用户
def init():
    file=open("u_root","w")
    root={"rnum":"管理员","rpwd":"123456"}
    file.write(str(root))
    file.close()
    os.mkdir("users")
#打印登陆菜单
def print_login_menu():
    print("------用户选择------")
    print("1--管理员登录")
    print("2--普通用户登录")
    print("--------------------")
#用户选择
def user_select():
    while True:
        user_type_select = input("请选择用户类型")
        if user_type_select=="1": #管理员登陆验证
            root_login()
            break
        elif user_type_select=="2":
            while True:
                select= input("是否需要注册？（y/n）:")
                if select=="y" or select=="Y":
                    print("------用户注册------") 
                    user_register()   #用户注册
                    break
                elif select =="n"or select=="N":
                    print("------用户登录------")
                    user_login()  #用户登录
                    break
                else:
                    print("输入有误，请重新选择")
                break
        else:
            print("输入有误，请重新选择")
#管理员登陆
def root_login():
    while True:
        print("------管理员登陆------")
        root_number = input("请输入账户名：")
        root_password= input("请输入密码：")
        file_root=open("u_root")        #只读打开root账户文件
        root=eval(file_root.read())   #读取账户信息
        #信息匹配
        if root_number ==root["rnum"] and root_password==root["rpwd"]:
            print("登陆成功！")
            break
        else:
            print("验证失败！")
#用户注册
def user_register():
    user_id = input ("请输入账户名：")
    user_pwd = input("请输入密码：")
    user_name= input("请输入昵称：")
    user={"u_id":user_id,"u_pwd":user_pwd,"u_name":user_name}
    user_path="./users/"+user_id
    file_user=open (user_path,"w")    #创建用户文件
    file_user.write(str(user))     #写入
    file_user.close()   #保存并关闭
#普通用户登录
def user_login():
    while True :
        print("------普通用户登录------")
        user_id=input("请输入账户名：")
        user_pwd=input("请输入密码：")
        #获取user目录中的所有的文件名
        user_list=os.listdir("./users")
        #遍历元组，判断user_id 是否在元组中
        flag=0
        for user in user_list:
            flag=1
            print("登陆中…………")
            #打开文件
            file_name="./users/"+user_id
            file_user=open(file_name)
            #获取文件内容
            user_info=eval(file_user.read())
            if user_pwd == user_info["u_pwd"]:
                print("登陆成功！")
                break
        if flag==1:
            break
        elif flag==0:
            print("查无此人！请检查账户名以及密码，新用户请重新注册")
            break
is_first_start()
            
            
            
            
            
            
            