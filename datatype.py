def data_type(item = None):
    if item == None:
        return 'No Vlaue'
    elif isinstance(item,str):
        return len(item)
    elif isinstance(item,bool):
        return item
    elif isinstance(item,int):
        if item < 100:
            return 'Less than 100'
        elif item ==100:
            return 'Equal to 100'
        else:
            return 'More than 100'
    elif isinstance(item,list):
        if len(item) >= 3:
            return item[2]
        else:
            return None
