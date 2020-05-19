import json


def get_stored_username():
    """若用户名已存在，则获取它"""
    file_name = 'username.json'
    try:
        with open(file_name) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    new_username = input("请输入用户名：")
    file_name = "username.json"
    with open(file_name, 'w') as f_obj:
        json.dump(new_username, f_obj)
    return new_username


def greet_user():
    """问候用户"""
    username = get_stored_username()

    if username:
        answer = input("你的用户名是：" + username + "吗？(yes/no)")
        if answer == 'yes':
            print("你好，" + username.title() + ".")
        else:
            get_new_username()
    else:
        username = get_new_username()
        print("下次我会记住你的名字，" + username.title())


greet_user()