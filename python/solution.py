#Import re module to use regular expression suport
import re

'''
Before the keyword 'SUPERSPY' can be used in the array to come, it must be proccessed to meet the cipher rules

Cipher Rules for the Keyword Include:
1. All characters must be uppercase - as all of our values will be uppercase in the matrix
2. There are no repeating letters in the keyword
3. There are no special characters in the keyword

For the purpose of this application, I will only be needing to process the keyword 'SUPERSPY' but to allow users to process any keyword, a method is written to and a keyword is used as the parameter of this method.
'''

def keyword_processor (keyword):
  #Remove all characters that are not A-Z and a-z (i.e. special characters) within the capitzalized keyword string 
  keyword = re.sub(r'^a-zA-Z]', '', keyword.upper())

  #In the matrix, J is replaced with I, so we must do the same within the keyword. We must do this before removing duplicates in case we create a duplicate as a result of this proccess.
  keyword = keyword.replace('J', 'I')

  #Now we must remove any potential duplicates. This is done by 