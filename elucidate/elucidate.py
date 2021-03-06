#!/usr/bin/python

# Elucidate: A Python script that uses basic methods to crack passwords.
# Based off of a script created by Science Buddies. (http://www.sciencebuddies.org/Files/5549/17/crack2.py)

# This script contains cleaner, improved code and commenting as well as additional functionality.

# See README.md for more information.
# Availiable on Github: https://github.com/DonutDeflector/elucidate

# Go to line 377 to set the passwords you want to crack.

######################################################################################

# extra functions needed
import sys, time, hashlib
from array import *

#################### 
# global variables # 
####################

# password to crack from 0-9
which_password = 0

# passwords we are trying to crack; will get written in
password0 = ""
password1 = ""
password2 = ""
password3 = ""
password4 = ""
password5 = ""
password6 = ""
password7 = ""
password8 = ""
password9 = ""

# total number of guesses to crack the password
totalguesses = 0

##########################
# extra helper functions #
##########################
# These will be needed later by the search methods.
# We'll get these defined and out of the way. The actual search program is called "main" 
# and will be the last one defined. Once it's defined, the last statement in the file runs it.

# Takes a number from 0 on up and the number of digits we want it to have. It uses that
# number of digits to make a string like "0000" if we wanted 4 or "00000" if we wanted
# 5, converts our input number to a character string, sticks them together and then returns
# the number we started with, with extra zeroes stuck on the beginning. 
def leading_zeroes(n, zeroes):
    t=("0"*zeroes)+str(n)
    t=t[-zeroes:]
    return t

# check if the guess of the password was correct
def check_userpass(which_password, password):
    global password0, password1, password2, password3
    global password4, password5, password6, password7
    global password8, password9
    
    result = False

    if (0 == which_password):
        if password == password0:
            result = True

    if (1 == which_password):
        if password == password1:
            result = True

    if (2 == which_password):
        if password == password2:
            result = True

    if (3 == which_password):
        if password == password3:
            result = True

    if (4 == which_password):
        if password == password4:
            result = True
            
    if (5 == which_password):
        if password == password5:
            result = True
            
    if (6 == which_password):
        if password == password6:
            result = True

    if (7 == which_password):
        if password == password7:
            result = True

    if (8 == which_password):
        if password == password8:
            result = True

    if (9 == which_password):
        if password == password9:
            result = True
            
    return result

# displays guess results for each method once it's complete
def report_search_time(tests, seconds):
    if (seconds > 0.000001):
        print ("Seconds: "+make_human_readable(seconds)+" | Tests: "+make_human_readable(tests)+" | Tests/Seconds: "+make_human_readable(tests/seconds)+"")
    else:
        print ("Seconds: "+make_human_readable(seconds)+" | Tests: "+make_human_readable(tests)+"")
    return

##################
# search methods #
##################

# METHOD 1 -
# Guess using numbers. (up to 8 digits)
def search_method_1(num_digits):
    global totalguesses
    result = False
    a=0
    starttime = time.time()
    tests = 0
    still_searching = True
	# inform user about number of digits
    print("")
    if num_digits == 1:
      print("Method 1 -- "+str(num_digits)+" digit")
    else:
      print("Method 1 -- "+str(num_digits)+" digits")
	# guess up to 8 digit numbers
    while still_searching and a<(10**num_digits):
        ourguess = leading_zeroes(a,num_digits)
        tests = tests + 1
        totalguesses = totalguesses + 1
        if (check_userpass(which_password, ourguess)):
            print ("Success! Password "+str(which_password)+" = " + ourguess)
            still_searching = False   # we can stop now - we found it!
            result = True
        a=a+1

	# return guess statistics
    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return result

# METHOD 2 -
# Guess using combination of characters. Includes punctuation. (up to 25 characters)
def search_method_2(num_pass_wheels):
    global totalguesses
    result = False
    starttime = time.time()
    tests = 0
    still_searching = True

	# inform user about character limit
    print("")
    print("Method 2 -- "+str(num_pass_wheels)+" character limit")

    # set all of the wheels to the first position
    wheel = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    pass_wheel_array=array('i',[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    while still_searching:
        ourguess_pass = ""
        for i in range(0,num_pass_wheels):  # once for each wheel
            if pass_wheel_array[i] > 0:
                ourguess_pass = wheel[pass_wheel_array[i]] + ourguess_pass
        if (check_userpass(which_password, ourguess_pass)):
            print ("Success! Password  "+str(which_password)+" = " + ourguess_pass)
            still_searching = False   # we can stop now - we found it!
            result = True
        tests = tests + 1
        totalguesses = totalguesses + 1
# spin the rightmost wheel and if it changes, spin the next one over and so on
        carry = 1
        for i in range(0,num_pass_wheels): # once for each wheel
            pass_wheel_array[i] = pass_wheel_array[i] + carry
            carry = 0
            if pass_wheel_array[i] > 62:
                pass_wheel_array[i] = 1
                carry = 1
                if i == (num_pass_wheels-1):
                    still_searching = False

	# return guess statistics
    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return result

#####################################################################################

# This function takes in numbers, rounds them to the nearest integer and puts
# commas in to make it more easily read by humans
def make_human_readable(n):
    if n>=1:
        result = ""
        temp=str(int(n+0.5))
        while temp != "":
            result = temp[-3:] + result
            temp = temp[:-3]
            if temp != "":
                result = "," + result
    else:
        temp = int(n*100)
        temp = temp /100
        result = str(temp)
    return result
        
## A little helper program to remove any weird formatting in the file
def cleanup (s):
    s = s.strip()
    return s

## A little helper program that capitalizes the first letter of a word
def Cap (s):
    s = s.upper()[0]+s[1:]
    return s

####################################################################################

# METHOD 3 -
# Use dictionary of common passwords. Includes capitalization. (uses passwords.txt)
def search_method_3(file_name):
    global totalguesses
    result = False
    
    # access the passwords.txt file
    f = open(file_name)
    words = f.readlines()
    f.close
    # inform user about amount of passwords in file
    number_of_words = len(words)
    print("")
    print("Method 3 -- "+str(number_of_words)+" passwords in list")
    
    ## Depending on the file system, there may be extra characters before
    ## or after the words. 
    for i in range(0, number_of_words):
        words[i] = cleanup(words[i])

    # guesses using the passwords in the file
    starttime = time.time()
    tests = 0
    still_searching = True
    word1count = 0           # Which word we'll try next
    while still_searching:
        ourguess_pass = words[word1count]
        # guess each password in the file as is
        if (check_userpass(which_password, ourguess_pass)):
            print ("Success! Password "+str(which_password)+" = " + ourguess_pass)
            still_searching = False   # we can stop now - we found it!
            result = True
        tests = tests + 1
        totalguesses = totalguesses + 1
        # guess each password in the file with the first character capitalized
        if still_searching:
            ourguess_pass = Cap(ourguess_pass)
            if (check_userpass(which_password, ourguess_pass)):
                print ("Success! Password "+str(which_password)+" = " + ourguess_pass)
                still_searching = False   # we can stop now - we found it!
                result = True
            tests = tests + 1
            totalguesses = totalguesses + 1

        word1count = word1count + 1
        if (word1count >=  number_of_words):
            still_searching = False

	# returns guess statistics
    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return result
            
# METHOD 4 -
# Uses combination of common passwords. Includes punctuation and capitalization.
def search_method_4(file_name):
    global totalguesses
    result = False
    
    # access the passwords.txt file
    f = open(file_name)
    words = f.readlines()
    f.close
    # get number of passwords in list
    number_of_words = len(words)
    
    ## Depending on the file system, there may be extra characters before
    ## or after the words. 
    for i in range(0, number_of_words):
        words[i] = cleanup(words[i])

    # Let's try each one as the password and see what happens
    starttime = time.time()
    tests = 0
    still_searching = True
    word1count = 0           # Which word we'll try next
    punc_count = 0
    word2count = 0

    punctuation="~!@#$%^&*()_-+={}[]:<>,./X"  # X is a special case where we omit
                                              # the punctuation to run the words together

    # inform user about the amount of punctuation characters and passwords in the file
    number_of_puncs = len(punctuation)
    print("")
    print("Method 4 -- "+str(number_of_puncs)+" punctuation characters and "+str(number_of_words)+" passwords in list")

    # guesses passwords using combinations of passwords in the file and punctuation characters
    while still_searching:
        if ("X" == punctuation[punc_count]):
            # If we're at the end of the string and found the 'X', leave it out
            ourguess_pass = words[word1count] + words[word2count]
        else:
            ourguess_pass = words[word1count] + punctuation[punc_count] + words[word2count]
        # try passwords as they are in the file
        if (check_userpass(which_password, ourguess_pass)):
            print ("Success! Password "+str(which_password)+" = " + ourguess_pass)
            still_searching = False   # we can stop now - we found it!
            result = True
        tests = tests + 1
        totalguesses = totalguesses + 1
        # capitalize the first letter of the first word
        if still_searching:
            ourguess_pass = Cap(words[word1count]) + punctuation[punc_count] + words[word2count]
            if (check_userpass(which_password, ourguess_pass)):
                print ("Success! Passwword "+str(which_password)+" = " + ourguess_pass)
                still_searching = False   # we can stop now - we found it!
                result = True
            tests = tests + 1
            totalguesses = totalguesses + 1
        # capitalize the first letter of the second word
        if still_searching:
            ourguess_pass = words[word1count] + punctuation[punc_count] + Cap(words[word2count])
            if (check_userpass(which_password, ourguess_pass)):
                print ("Success! Password "+str(which_password)+" = " + ourguess_pass)
                still_searching = False   # we can stop now - we found it!
                result = True
            tests = tests + 1
            totalguesses = totalguesses + 1
        # capitalize the first letter of both words
        if still_searching:
            ourguess_pass = Cap(words[word1count]) + punctuation[punc_count] + Cap(words[word2count])
            if (check_userpass(which_password, ourguess_pass)):
                print ("Success! Password "+str(which_password)+" = " + ourguess_pass)
                still_searching = False   # we can stop now - we found it!
                result = True
            tests = tests + 1
            totalguesses = totalguesses + 1

        word1count = word1count + 1
        if (word1count >=  number_of_words):
            word1count = 0
            punc_count = punc_count + 1
            if (punc_count >= number_of_puncs):
                punc_count = 0
                word2count = word2count + 1
                if (word2count >= number_of_words):
                    still_searching = False

    # return guess statistics
    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return result

######################
# password variables #
######################

def main(argv=None):
    global password0, password1, password2, password3
    global password4, password5, password6, password7    
    global password8, password9, totalguesses, which_password

    # set the passwords you want to guess here
    password0="123456"
    password1="albert"
    password2="03694816"
    password3="mistress!maxwell"
    password4="phantomscorpion"
    password5="armor"
    password6="frBSD173"
    password7="m0n2t3r2"
    password8="correcthorsebatterystaple"
    password9="Gkgmyf8jNYB2UbVf"

###################
# guess passwords #
###################

    # prompt user to select password to crack
    which_password = 1
    which_password = int(input("Password to Guess (0-9): "))
    overallstart = time.time()
    foundit = False

    # inform user about the password being cracked.
    print("")
    print("Guessing: Password "+str(which_password))

    #  1st - guess common passwords
    if not foundit:
        foundit = search_method_3("passwords.txt")
    #  2nd - guess combination of common passwords
    if not foundit:
        foundit = search_method_4("passwords.txt")
    #  3rd - guess 1 digit numbers
    if not foundit:
        foundit = search_method_1(1)
    #  4th - guess 2 digit numbers
    if not foundit:
        foundit = search_method_1(2)
    #  5th - guess 3 digit numbers
    if not foundit:
        foundit = search_method_1(3)
    #  6th - guess 4 digit numbers
    if not foundit:
        foundit = search_method_1(4)
    #  7th - guess 5 digit numbers
    if not foundit:
        foundit = search_method_1(5) 
    #  8th - guess 6 digit numbers
    if not foundit:
        foundit = search_method_1(6)
    #  9th - guess 7 digit numbers
    if not foundit:
        foundit = search_method_1(7)
	# 10th - guess 8 digit numbers
    if not foundit:
       foundit = search_method_1(8)
    # 11th - guess up to 25 character combinations   
    if not foundit:
        foundit = search_method_2(25)
    seconds = time.time()-overallstart

#################
# result output #
#################

    # print information about the guessing process (total seconds, total guesses, and guesses per second)
    print ("")
    print ("Total Seconds: "+make_human_readable(seconds)+" seconds")
    print ("Total Guesses: "+make_human_readable(totalguesses)+" guesses")
    print ("Guesses/Second: "+make_human_readable(totalguesses/seconds)+" guesses/second")

print ("- Elucidate: Python Password Cracker -")
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
