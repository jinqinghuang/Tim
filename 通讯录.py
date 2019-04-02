telbook={}
print("    您好！请按提示进行操作。")
flag = "a"
while flag == "a" or "b" or "c" or "d" or "e" :
    t = input("\
    1.输入a为通讯录添加联系人和相应手机号. \n\
    2.输入b删除通讯录里的联系人. \n\
    3.输入c修改通讯录里联系人手机号。\n\
    4.输入d查询通讯录里的所有用户。 \n\
    5.输入e根据姓名查找响应联系人手机号  \n")
    if t == "a":
        name = input("请输入联系人姓名：")
        if name in telbook:
            print("名字重复，不能使用！请换用其他名字！")
        else:
            telnum = input("请输入联系人号码：")
            telbook[name] = telnum
            print("存储成功!") 
        w = input("继续操作请输入'y',任意键退出\n")
        if w == "y":
            continue
        else:
            break
    
    elif t == "b":
        name = input("请输入需要删除的姓名：")
        try:
            del telbook[name]
            print("删除成功!")
        except:
            print("联系人不存在")
        w = input("继续操作请输入'y',任意键退出\n")
        if w == "y":
            continue
        else:
            break

    elif t == "c":
        name = input ("请输入需要修改号码的联系人：")
        if name not in telbook:
            print("联系人不存在")
        else:
            telnum = input("请输入手机号：")
            telbook[name] = telnum
            print("修改成功!")
        w = input("继续操作请输入'y',任意键退出\n")
        if w == "y":
            continue
        else:
            break

    elif t == "d":
        print(telbook)
        w = input("继续操作请输入'y',任意键退出\n")
        if w == "y":
            continue
        else:
            break
    elif t =="e":
        name = input("请输入联系人姓名:")
        try:
            print(telbook[name])
        except:
            print("联系人不存在")
        w = input("继续操作请输入'y',任意键退出\n")
        if w == "y":
            continue
        else:
            break
    else:
        print("输入错误，请输入正确字母！")
        continue
