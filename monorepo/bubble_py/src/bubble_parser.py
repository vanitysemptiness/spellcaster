
def last_element_of_list(ls: list) -> str:
    '''
    get last element from list and trim white space
    or return empty list
    '''
    if len(ls) >= 1:
        # should always be a singular string
        return [ls[-1]].strip()
    else:
        return ''
    
def extract_commands(ls: list) -> list:
    '''
    get all elements from list but last
    trim extra white space
    or return empty list
    '''
    if len(ls) <= 1:
        return []
    else:
        # all but last entry and stripped white space
        return [string.strip() for string in ls[:-1]]