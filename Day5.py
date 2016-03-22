#! /usr/bin/env python


def vowel_check(text):
    vowel = 'a', 'e', 'i', 'o', 'u'
    check = False
    vowel_count = 0

    for i in text:
        for j in vowel:
            if i == j:
                check = True
                vowel_count += 1

    if vowel_count < 3:
        check = False

    return check

def twice_check(text):
    j = ''
    check = False

    for i in text:
        if i == j:
            check = True
        j = i

    return check

def naughty_check(text):
    naughty = 'ab', 'cd', 'pq', 'xy'
    check = True
    old_val = ''

    for idx, new_val in enumerate(text):
        for j in naughty:
            if old_val + new_val == j:
                check = False
        old_val = new_val
   
    
    return check

def nice_string(text):

    return vowel_check(text) and  twice_check(text) and naughty_check(text)
#-------doesn't work ----------------------------------
def overlap_check(text):
    match_array = [] 
    check = False
    
    for idx, value in enumerate(text):
        match_array.append(text[idx - 1] + value)
    match_array.pop(0) #first value is throwaway   
    
    for idx, value1 in match_array:
        for idy, value2 in match_array:
            if value1 == value2 and idx is not idy:
                check == True
                print value1, value2

    print match_array       
          
    
    return check
#-------------------------------------------------------


def main():
    #test_string = "haegwjzuvuyypxyu"
    test_string = open('Day5_input.txt','r')
    total_strings = 0

    for line in test_string: 
        if nice_string(line) == True:
            total_strings += 1
    #o_result = overlap_check(test_string)

    print "\n\nnumber of nice strings : %i" % total_strings
    
    
if __name__ == "__main__":
    main()
