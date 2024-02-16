
def last_element_of_list(ls: list) -> str:
    '''
    get last element from list or return 
    empty list
    '''
    if len(ls) >= 1:
        return [ls[-1]]
    else:
        return ''
    
def extract_commands(ls: list) -> list:
    '''
    get all elements from list but last
    or return empty list
    '''
    if len(ls) <= 1:
        return []
    else:
        return ls[:-1]