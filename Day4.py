#! /usr/bin/env python
import md5
import os

def md5_calc(key, hash_string):
    
    number = 0
    output = ''
    
    while(not output.startswith(hash_string)):
    
        number += 1 
        test_hash = md5.new()
        test_hash.update(key + str(number))
        output = test_hash.hexdigest()

    return number

if __name__ == "__main__":
    os.system('clear')
    print '\n\n--- Day 4: The Ideal Stocking Stuffer ---\n\n'
    
    key = raw_input('enter secret key:\t')
   
    five_zero_answer = md5_calc(key, '00000')
    print '\n\n---------------------------------------------'
    print '\tPART 1:\n'
    print 'answer: \t\t', five_zero_answer, '\n\n\n'

    six_zero_hash, six_zero_answer = md5_calc(key, '000000')
    print '---------------------------------------------'
    print '\tPART 2:\n'
    print 'answer: \t\t', six_zero_answer, '\n\n\n'
