import re
n = int(input())
for i in range(n):
    num=input().strip()
    if re.match(r'^[789]\d{9}$',num):
        print("YES")
    else:
        print("NO")
