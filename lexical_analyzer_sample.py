import re
import nltk

input_program = input("enter your code: ");
input_program_tokens = nltk.wordpunct_tokenize(input_program);

print(input_program_tokens);


RE_keywords = ""
RE_reserved_words = ""
RE_noise_words = ""
RE_operators = ""
RE_digits = ""
RE_special_characters = "[. , + - * / % < > = " " ' ' , ; | ! ( )[ ] _ ^ &]"
RE_identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
RE_headers = "[a-zA-Z]+\.[h]"

#To categorize the Tokens

for token in input_program_tokens:
    if(re.findall(RE_keywords,token)):
        print(token , "-------> Keyword")
    elif(re.findall(RE_reserved_words,token)):
        print(token , "-------> Reserved Word")
    elif(re.findall(RE_noise_words,token)):
        print(token , "-------> Nosise Word")
    elif(re.findall(RE_digits,token)):
        print(token , "-------> Digit")
    elif(re.findall(RE_special_characters,token)):
        print(token , "-------> Special Character/Symbols")
    elif(re.findall(RE_identifiers,token)):
        print(token , "-------> Identifier")
    elif(re.findall(RE_headers,token)):
        print(token , "-------> Header")
    
    else:
        print("Value Unknown")