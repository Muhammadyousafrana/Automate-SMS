def add_num(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return "please enter a value"
    except ValueError as err:
        return err
