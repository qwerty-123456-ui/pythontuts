name,sc=input("Enter ur name and a single  character ").split(",")
print(f"Name is {name} and no of counts is {name.lower().count(sc.lower())}")
#to remove spaces
name ="  isha   "
dots="..."
print(name.lstrip()+dots)
print(name.rstrip()+dots)
print(name.strip()+dots)
print(name.replace(" ","")+dots)
print(name.strip())
# above exercise
#  "   Harshit"  -> "  harshit"  -> "harshit"
# "  H " or "   h"->"   h"->"h"
print(f"Name length is {len(name.strip())} and no of counts is {name.lower().count(sc.strip().lower())}")
print(f"Name is {name} and no of counts is {name.lower().count(sc.lower())}")
print(f"Name is {name.strip()} and no of counts is {name.lower().count(sc.strip().lower())}")