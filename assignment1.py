from libs import get_data, get_data_list


# write unittest for this function
def show_square():
    return_data = get_data()
    if not return_data:
        return False

    data_list_data = get_data_list()
    for data_object in data_list_data:
        print(data_object.get('number') ** 2)
        if data_object.get('number') == 1:
            print("Found")
    return True

