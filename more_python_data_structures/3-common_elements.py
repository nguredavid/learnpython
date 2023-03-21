#!/usr/bin/python3

def common_elements(set_1, set_2):

    c_set = set_1 - set_2


    
    return c_set

st_1 = { "Python", "C", "Javascript" }
st_2 = { "Bash", "C", "Ruby", "Perl" }

result = common_elements(st_1, st_2)
print(result)
