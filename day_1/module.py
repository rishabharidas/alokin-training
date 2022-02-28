str_list = []
def join_list(list_for_join):
    """function to join values of list."""
    for list_value in list_for_join:
        str_list.append(str(list_value)) 
    joined_value = int("".join(str_list)) # join function Usage
    return joined_value