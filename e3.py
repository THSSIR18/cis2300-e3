# SPECIAL NOTE:
# 1) Do not use python lambdas
# 2) Do not use maps/filters
# 3) If you don't know what the first two items are -- smile, and move on!
# 4) Do not import any other libraries - not even built-in ones, such as math
# 5) Resist the temptation to google up python code and blindly copy/pasting 
# 6) All the best and good luck!
# 7) oh, and don't forget your email and id in lines 4-5 above.

# Change this to your specific 7 letter unique word
MY_WORD = "FERRARI"

# Change this to your specific 5 digit unique number
MY_NUM = 22022

#------------------------------------------------------------------------------
# Question 1: 
# Modify the function such that it works according to the description below:
#
# This function returns a string constructed by appending every Nth letter 
# of word, where N is the largest digit of MY_NUM. You may safely assume that 
# word is of type str and has more than 1 letters. If word is less than N
# characters long, the function returns an empty string.
#
# Jane's example: the largest digit for Jane is 5. So Jane's function
# should return a string that is constructed by appending every 5th letter of 
# word.
#
# So, for Jane:
# question1('1234a1234b1234c1234d1234e') 
# returns: 'abcde'
# 
# question1('1234') 
# returns: ''
#
# question1('****X*') 
# returns: 'X'

def largestdigit(n):
    s = str(n)
    result = []
    for i in s:
        result.append(int(i))
    return max(result)


def question1(word):
    result = ''
    n = largestdigit(MY_NUM)
    for i in range(len(word)):
        if i > 0 and (i+1) % n == 0:
            result += word[i]
    return result

#------------------------------------------------------------------------------
# Question 2:
# Modify the function such that it works according to the description below:
# 
# This function assumes list1 is a list and it contains tuples where each tuple
# is a pair of integers (ints). For e.g. list1 could be: [(1,2), (9,9), (5,1)].
# The function returns the count of tuples whose sum of numbers is greater than
# the sum of all the digits of MY_NUM.
# 
# Jane's example: The sum of all digits if MY_NUM is 15 (1+2+3+4+5)
#
# So, for Jane:
# question2([(1,1),(2,2),(15,1)])
# returns 1 
# (because only 1 pair has a sum is greater than 15)
#
# question2([(15,2),(14,2),(25,-5)])
# returns 3 
# (because all 3 pairs have their sums greater than 15)

def sumdigits(n):
    s = str(n)
    result = 0
    for i in s:
        result += int(i)
    return result


def question2(list1):
    count = 0
    s = sumdigits(MY_NUM)
    for i in list1:
        if sum(i) > s:
            count += 1
    return count


#------------------------------------------------------------------------------
# Question 3:
# Modify the function such that it works according to the description below:
# 
# This function assumes list1 and list2 are lists and have the same number of 
# items and each item is an int. This function returns the total sum of all 
# items from both the lists if ALL these requirements are satisfied:
#
# (a) no item is smaller than the previous item in list1 (e.g. [1,2,2,3,4])
# (b) no item is greater than the previous item in list2 (e.g. [5,4,3,2,2])
# (c) both lists contain an item that is one of the digits of MY_NUM
#
# If these conditions are not met, 0 is returned.
#
# Jane's example: Jane's digits are 1,2,3,4,5
# 
# So, for Jane:
# question3([1,2,3],[9,8,5])
# returns 28 
# (because all conditions are met)
#
# question3([1,2,2],[1,0,0])
# returns 6 
# (because all conditions are met)
#
# question3([1,2,2,4],[1,2,3,4])
# returns 0 
# (because the 2nd list violates conditon(b))

def question3(list1,list2):
    for i in range(len(list1)-1):
        if (list1[i+1] < list1[i]) or (list2[i+1] > list2[i]):
            return 0
    contains1 = False
    contains2 = False
    for i in range(len(list1)):
        if str(list1[i]) in str(MY_NUM):
            contains1 = True
        if str(list2[i]) in str(MY_NUM):
            contains2 = True
    if not (contains1 and contains2):
        return 0 
    return sum(list1)+sum(list2)
    

#------------------------------------------------------------------------------
# Question 4:
# Modify the function such that it works according to the description below:
# 
# This function assumes text is of type str and that text is non-empty.
# The function returns True  if the first 3 letters of MY_WORD appears in 
# the same order within the letters found in text. The function 
# should work for both upper and lower case characters found in text. 
# 
# For this function, we will use John's example: Suppose John's MY_WORD is 
# "hoodies"
# 
# So this function, for John, should return True if text contains the letters
# h (or H) followed by o (or O) followed by another o (or O). There could
# be other letters in between, but as long as an h is followed by an o 
# and then another o, the function returns True. If the condition is not met,
# it returns False
# 
# So, for John:
# question4( 'hoo' )
# returns True
# (the order sequence h,o,o can be seen very clearly)
#
# question4( '..A...C...H...O...O..!' )
# returns True
# (the order sequence h,o,o can be seen very clearly here too (H...O...O..))
# 
# question4( 'Harry must find some odd jobs.' )
# returns True
# (the sequence h,o,o can be seen from the words: [H]arry, s[o]me, [o]dd )
#
# question4( 'oh, no!' )
# returns False
# ( no instance of h followed by two o's)

def question4(text):
    a = ''
    for i in text:
        if i.isalpha():
            a += i.lower()
    letter1 = MY_WORD[0].lower()
    letter2 = MY_WORD[1].lower()
    letter3 = MY_WORD[2].lower()
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            for k in range(j+1,len(a)):
                if a[i] == letter1 and a[j] == letter2 and a[k] == letter3:
                    return True
    return False

#------------------------------------------------------------------------------
# Question 5: 
#
# Modify the function such that it works according to the description below:
#
# This function assumes dict1 is of type dictionary. It also assumes
# both the keys and values of dict1 are of type str. Here is an example:
# dict1 = {'sun':'weekend', 'mon':'weekday', 'tue':'weekday'}
# This function returns how many times any of the letters of MY_WORD
# appears in either the key or the value in either upper or lower case
#
# So, for Jane:
# question5({'sun':'weekend'})
# returns 2 
# (because s appears in 'sun' and d appears in 'weekend')
#
# question5({'ORCHIDS':'fly'})
# returns 7
# (because all 7 letters appears in the key, once each)
#
# question5({'ORCHIDS':'fly',  'my':'orchids'})
# returns 14
# (because all 7 letters appears twice, as key in first entry, and as value
# in the second entry)

def question5(dict1):
    keys = list(dict1.keys())
    for i in range(len(keys)):
        keys[i] = keys[i].lower()
    values = list(dict1.values())
    for i in range(len(values)):
        values[i] = values[i].lower()
    count = 0
    word = MY_WORD.lower()
    for i in keys:
        for j in i:
            if j in word:
                count += 1
    for i in values:
        for j in i:
            if j in word:
                count += 1
    return count

#------------------------------------------------------------------------------
# Question 6:(extra credit/challenging problem)
#
# Modify the function such that it works according to the description below:
# 
# This is an extension of Question 4, and is a bit more challenging.
#
# This function assumes text is of type str and that text is non-empty.
# The function returns the number of ways the first 3 letters of MY_WORD 
# appears in the same order within the letters found in text. The function 
# should work for both upper and lower case characters. 
# 
# In Question 4, the function returned True if any instance of the order of
# the first 3 letters of MY_WORD was found in text. This function returns
# the count of possible orders found in text.
#
# So, for Jane: 
# question6('o..r..c')
# returns 1
# (because there is only one possible order)
#
# question6('orcC')
# returns 2
# (because there are two possible orders: orc and orC)
#
# question6('oR..rC...c')
# returns 4
# (because there are 4 possible orders: orc, orC, oRc, and oRC)
#

def question6(text):
    a = ''
    for i in text:
        if i.isalpha():
            a += i.lower()
    letter1 = MY_WORD[0].lower()
    letter2 = MY_WORD[1].lower()
    letter3 = MY_WORD[2].lower()
    count = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            for k in range(j+1, len(a)):
                if a[i] == letter1 and a[j] == letter2 and a[k] == letter3:
                    count += 1
    return count


##########################################
# Sample Test Function
# Test Cases: specific to Jane
#
# Modify to match your own specific tests
#
##########################################
def test_my_functions():
    print('-'*20) # prints a horizontal line
    
    print('q1 test1:',question1('1234a1234b1234c1234d1234e'))
    print('q1 test2:',question1('1234'))
    print('q1 test3:',question1('****X*'))
    print('-'*20) # prints a horizontal line
    
    print('q2 test1:',question2([(1,1),(2,2),(15,1)]))
    print('q2 test2:',question2([(15,2),(14,2),(25,-5)]))
    print('q2 test3:',question2([(15,2),(14,2),(25,-5)]))
    print('-'*20) # prints a horizontal line   

    print('q3 test1:',question3([1,2,3],[9,8,5]))
    print('q3 test2:',question3([1,2,2],[1,0,0]))
    print('q3 test3:',question3([1,2,2,4],[1,2,3,4]))
    print('-'*20) # prints a horizontal line  
    
    print('q4 test1:',question4( 'hoo' ))
    print('q4 test2:',question4( '..A...C...H...O...O..!' ))
    print('q4 test3:',question4( 'Harry must find some odd jobs.' ))
    print('q4 test4:',question4( 'oh, no!' ))
    print('-'*20) # prints a horizontal line 


    print('q5 test1:',question5({'sun':'weekend'}))
    print('q5 test2:',question5({'ORCHIDS':'fly'}))
    print('q5 test3:',question5({'ORCHIDS':'fly',  'my':'orchids'}))
    print('-'*20) # prints a horizontal line 
    
    print('q6 test1:',question6('o..r..c'))
    print('q6 test2:',question6('orcC'))
    print('q6 test3:',question6('oR..rC...c'))
    print('-'*20) # prints a horizontal line 
    

#######################
#### Main Program #####
#######################

# You are free write any test code here
# I am providing one here below, but it needs to be customized to your
# own MY_WORD and MY_NUM
test_my_functions()
