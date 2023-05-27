a = [ 0, 1, 2, 3, 4, 5, 6, 7]
N = len(a)
for i in range(N):
    a[i] = a[(i+4) % N]
print(a)

print(0110 ^ 1100) AND (3 || 5) XOR (NOT 0111))