import sys

input = sys.stdin.readline

N = int(input())
S, M, L, XL, XXL, XXXL = map(int, input().split())
T, P = map(int, input().split())

T_p = 0
for i in [S, M, L, XL, XXL, XXXL]:
    a, b = divmod(i, T)
    if b != T and b != 0:
        T_p += a + 1
    else:
        T_p += a

P_p = divmod(N, P)

print(T_p)
print(P_p[0], P_p[1])

# divmod is pretty good method for this kind of problem,
# as the ways computer calculate division and remainder are related.
