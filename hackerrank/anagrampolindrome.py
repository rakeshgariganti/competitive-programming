string = raw_input()
 
found = True
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
chars={}
for i in string:
    if i in chars:
        chars[i]+=1
    else:
        chars[i]=1
total=0
for i in chars:
    if chars[i]%2==1:
        total+=1
if total>1:
    found=False
if not found:
    print("NO")
else:
    print("YES")