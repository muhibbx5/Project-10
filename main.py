n = int(input("Enter the number of rows for the mirrored triangle: "))

for i in range(1, n+1):
    print(" " * (n - i), end="")
    print("*" * i)
