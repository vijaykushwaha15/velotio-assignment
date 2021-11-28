
def anagramfn(str1,str2):
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))
    if str1 == str2 :
        print("String : ", str1," is an anagram of String " ,str2)
    else :
        print("String : ", str1," is not an anagram of String " ,str2)
s1 = input("Enter your value1: ")
s2 = input("Enter your value2: ")
anagramfn(s1,s2)
   