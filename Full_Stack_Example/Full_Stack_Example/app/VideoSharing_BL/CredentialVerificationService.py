def validate_username(name):
    return True

def validate_password(name: str, pwd: str) -> bool:
    
    #Return False if the substring of the username is in the string password
    #Return False if the length of the password is less than 8
    #if there is no number in the string return false
    #If the number of unique characters in the string is fewer than 4 return False
    if name in pwd:
        return False
    if len(pwd) < 8:
        return False
    if not number_in_string(pwd):
        return False
    if len(set(pwd))< 4:
        return False
    return True



def number_in_string(string: str) -> bool:
    #Converts The string into a list, then keeps only the numbers in the string and makes a new list
    #If the length of the string with the numbers is less than one then there are no numbers in the string
    number_list = [x for x in list(string) if x.isdigit()]
    if len(number_list) < 1:
        return False
    return True
