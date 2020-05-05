F = int(input("Enter how many numbers to output of the fibonacci series:\n"))
One = 0
Two = 1

for i in range(F):
    print(One)
    store = One
    One = Two
    Two = store+Two
