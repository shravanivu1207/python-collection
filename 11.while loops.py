is_failed=True
i=1
while is_failed and i<=100:
    print(f"try {i}")
    i=i+1
print("i gave up")

#OR

is_failed=True
i=1
while is_failed:
    print(f"try {i}")
    i=i+1
    if i>100:
        break
print("i gave up")


is_failed=True
i=1
while is_failed:
    if i%2==0:
       i=i+1
       continue
    print(f"attempt {i}")
    i=i+1
    if i>100:
        break

i = 1
while i<=10:
    print(i)
    i+=1

#nested switch
i=0
while i<=10:
    x=0
    while x<i:
        print("shravani",end="-")
        x+=1
    print("") #it simply print new line and move cursor to next line
    i+=1

