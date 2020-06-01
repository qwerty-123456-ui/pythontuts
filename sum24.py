#palindrome
name=input("Enter ur name : ")
def palindrome(n1):
    print(n1==n1[::-1])
palindrome(name)