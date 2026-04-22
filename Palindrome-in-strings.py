# Type - I
word = input("Enter Word to be checked: ")
if word = word[::-1]:
  print("It's a palindrome")
else:
  print("It's not a palindrome")

#Type - II
a = input("Enter the word to be checked: ")
c = []
for i in range(len(a)):
    c.append(a[len(a) - 1 - i])
count = 0
for i in range(0,len(a)):
    if c[i] == a[i]:
        count += 1
if count == len(a):
    print("It's a palindrome")
else:
    print("It isn't a palindrome")

#Type - III
a = input("Enter the word to be checked: ")
c = []
if len(a)%2 == 0:
    count = 0
    for i in range(0,int(len(a)/2)):
        if a[i] == a[len(a) - i -1]:
            count += 1
    if count == i+1:
        print(f"{a} is a palindrome")
    else:
        print(f"{a} isn't a palindrome")
else:
    count = 0
    for i in range(0,int((len(a)-1)/2)):
        if a[i] == a[len(a) - i -1]:
            count += 1
    if count == i+1:
        print(f"{a} is a palindrome")
    else:
        print(f"{a} isn't a palindrome")
