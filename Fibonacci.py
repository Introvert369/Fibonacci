num = int(input("How long?: "))
prev = 0
curr = 1
for i in range(num):
    next = prev + curr
    print(next)
    prev = curr
    curr = next