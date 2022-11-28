import operation
import view
import logger

def button_click():
    value = view._input()
    logger.log(value)
    if type(value) == str:
        operation.find_contact(value)
    elif type(value) == list:
        operation.add_contact(value)
    else:
        print('ValueError')