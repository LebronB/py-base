import json

file_name = 'favorite_number.json'


def get_favorite_number():
    """提示用户输入最喜欢的数字"""
    favorite_number = input("输入你最喜欢的数字: ")
    with open(file_name, 'w') as f_obj:
        json.dump(favorite_number, f_obj)

    return favorite_number


def get_saved_number():
    """若用户已输入，获取这个数字"""
    try:
        with open(file_name) as f_obj:
            favorite_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_number


def show_number():
    """根据文件是否存在提示用户输入数字或告诉用户"""
    favorite_number = get_saved_number()
    if favorite_number:
        print("你最喜欢的数字是：" + favorite_number + ".")
    else:
        favorite_number = get_favorite_number()
        print("你最喜欢的数字 " + favorite_number + " 会被记录在" + file_name + ".")


show_number()

