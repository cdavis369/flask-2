import re

def validate_form(input):
    res = {"errors":{}}
    valid_colors = ["red", "green", "orange", "blue"]
    
    for field in input:
        if input[field] == "":
            res['errors'][field] = f"{field} is required."    
    
    if res['errors']:
        return res
    
    year = int(input['year'])
    
    if input['color'] not in valid_colors and input['color'] != "":
        res['errors']['color'] = f"{input['color']} is invalid. Must be one of: orange, green, red, blue."
        
    if year < 1900 or year > 2000:
        res['errors']['year'] = "year must be 1900 through 2000."
    
    if not validate_email(input["email"]):
        res['errors']["email"] = "invalid email address."
    
    return res


# Code taken from geeks for geeks
# -> https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    
    if(re.fullmatch(regex, email)):
         return True
    else:
      return False