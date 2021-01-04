import string
import numpy as np
import re
from collections import Counter
import sys
import numbers

#for declaring
lines = []
dict={}
arrIndStart=[]
arrIndEnd=[]
stringRemoved=[]

#for taking input
while True:  
    try:
        line = input()
        if line:
         lines.append(line)
        else:
         break
    except EOFError:
        break
text = '\n'.join(lines)    
final_string=text.replace("\n","")


#for strings
i=0
j=0
endInd=[] 
startInd=[]
L=list(final_string)
arrIndStart=[]
arrIndEnd=[]
#for strings under printf
for i in range(len(L)):
        if( L[i]=="(" and L[i+1]=="\""):
         startInd=i+1      #starting index of double quote
         arrIndStart.append(startInd)
for j in range(len(L)):
     if( L[j]==")" and L[j-1]=="\""):
         endInd=j-1      #ending index of double quote
         arrIndEnd.append(endInd)
for k in range(len(arrIndStart)):
      print("Literal,"+final_string[arrIndStart[k]:arrIndEnd[k]+1])
      stringRemoved.append(final_string[arrIndStart[k]:arrIndEnd[k]+1]) #for removing strings under printf
 
for k in range(len(arrIndStart)):
    final_string=final_string.replace(stringRemoved[k]," ") #strings removed
    
    
#for double operators
dou_ope_dict={}   #dictionary for double operator
dou_ope_dict["++"]=final_string.count("++")
dou_ope_dict["=="]=final_string.count("==")
dou_ope_dict["--"]=final_string.count("--")

for k in dou_ope_dict:
    if(dou_ope_dict[k]==0):
        continue
    else:
         print("Operator,"+k+",",end="")
         print(dou_ope_dict[k])
j=0
while(j<final_string.count("++")):    #for removing double operator ++
    j=j+1
    final_string=final_string.replace("++"," ")
j=0
while(j<final_string.count("==")):     #for removing ==
    j=j+1
    final_string=final_string.replace("=="," ")
j=0 
while(j<final_string.count("--")):    #for removing --
    j=j+1
    final_string=final_string.replace("--"," ")
    
L=list(final_string)
#for operators 
ope_dict={}
chr = np.array(["+","-","=",">", "<","/","%","*","{","}",")","(",";"])
for j in range(len(chr)):
     count=0
     for i in range(len(L)):
              if(L[i]==chr[j]):
                 final_string=final_string.replace(chr[j]," ")    #for removing all the operators
                 count=count+1
                 ope_dict[chr[j]]=count


for k in ope_dict:         #defining dictionary for count of the respective poerators
    if(k==";" or k=="}" or k=="{" or k==")" or k=="("):
         print("Seperator,"+k+",",end="")
         print(ope_dict[k])
    else:
        print("Operator,"+k+",",end="")
        print(ope_dict[k])
      
#for keywords
key_dict={}    #dictionary for keywords
key_dict["for"]=final_string.count("for")
key_dict["while"]=final_string.count("while")
key_dict["if"]=final_string.count("if")
key_dict["else"]=final_string.count("else")
key_dict["print"]=final_string.count("print")

for k in key_dict:
    if(key_dict[k]==0):
        continue
    else:
         print("Keyword"+","+k+",",end="")
         print(key_dict[k])

for k in key_dict:
    while(key_dict[k]):
        final_string=final_string.replace(k," ")    #removing keywords so that only integers and identifiers are left
        key_dict[k]=key_dict[k]-1

#for identifier and integers
new_word_list=final_string.split()    #creating a list of left over tokens
new_dict={}   #defining counts for identifiers and strings
for k in new_word_list:
    new_dict[k]=new_word_list.count(k)   #counting the frequency of each token
regex = '^[A-Za-z_][A-Za-z0-9_]*' #defining the regex

def check(string,count):  
     # pass the regualar expression 
     # and the string in search() method 
    if(re.search(regex, string)):    #using the regex library
        print("Identifier,"+string+",",end="")  
        print(count)  
    else:       #if its not an identifier its an integer
        print("Literal,"+string+",",end="")
        print(count)
for item in new_dict:   #checking for valid identifier
    check(item,new_dict[item])
    