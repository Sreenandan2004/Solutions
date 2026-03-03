def count_bits(n):
    if n==0:
        return 0
    return 1 + count_bits(bin(n) &bin(n-1))

n=int(input("Enter a number: "))
print(count_bits(n))
