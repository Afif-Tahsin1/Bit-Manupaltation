input("Parity - last bit = 0 even,  last bit = 1 odd.  Press Enter ")
for n in [2, 3, 4, 5, 8, 9]:
    if n & 1:
        print(f"  {n} -> odd")
    else:
        print(f"  {n} -> even")
n = int(input("Enter a number (try 13 or 7): "))
input("Count to 1s - watch bits drop off.  Press Enter ")
temp = n
while temp > 0:
    print(f"  binary {bin(temp)[2:]}  last bit: {temp & 1}")
    temp >>= 1
print(f"  total 1s in {n} = {bin(n).count('1')}")