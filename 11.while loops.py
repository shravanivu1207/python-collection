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
