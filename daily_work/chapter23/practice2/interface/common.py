from db.db_handler import select_group_chat,get_group_chat_list


def get_group_dict_interface():
    group_dict = {}
    group_list = get_group_chat_list()
    for group_name in group_list:
        group = select_group_chat(group_name)
        group_dict[group_name] = group.users_list

    return group_dict

if __name__ == '__main__':
    print(get_group_dict_interface())