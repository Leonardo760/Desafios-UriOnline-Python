a,b,c = input().split(" ")
A = int(a)
B = int(b)
C = int(c)
if A > B and A > C:
    print ("{} eh o maior".format(A,))
if B > A and B > C:
    print ("{} eh o maior".format(B,))
if C > A and C > B:
    print ("{} eh o maior".format(C,))


