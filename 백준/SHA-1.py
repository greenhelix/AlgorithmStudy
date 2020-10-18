# 백준 10928번
import hashlib
a = input()
print(hashlib.sha1(a.encode()).hexdigest())
