# input 말고 sys.stdin 의 함수로 입력을 받아 올 수 있다. 더 빠르다.
import math
import sys
import time
start = time.time()
a = sys.stdin.readline()
print(a, type(a))
# python3 부터 한글 변수명 사용이 가능해졌다.

이름 = '익환'
print(이름)

print('time: ', time.time() - start)

print('A', 'B')
print('A', 'B', end='')
print('A', 'B')
print('Python is [{:10}]'.format('good'))
print('Python is [{:<10}]'.format('good'))
print('Python is [{:>10}]'.format('good'))
print('Python is [{:^10}]'.format('good'))
print('[{0:★<5d}] [{1:★<5d}] [{2:★<5d}]'.format(1, -2, 3))
print('[{0:★>5d}] [{1:★>5d}] [{2:★>5d}]'.format(1, -2, 3))
print('[{0:★^5d}] [{1:★^5d}] [{2:★^5d}]'.format(1, -2, 3))
print('원주율 [{0:.3f}]'.format(math.pi))
print('원주율 [{0:.7f}]'.format(math.pi))
print('원주율 [{0:10.3f}]'.format(math.pi))
print('원주율 [{0:20.7f}]'.format(math.pi))
print('원주율 [{0:0.5f}]'.format(math.pi))
print('[{0:5b}] [{1:5b}] [{2:5b}]'.format(11, -22, 33))    # 2진수
print('[{0:5o}] [{1:5o}] [{2:5o}]'.format(11, -22, 33))    # 8진수
print('[{0:5x}] [{1:5x}] [{2:5x}]'.format(11, -22, 33))    # 16진수 소문자
print('[{0:5X}] [{1:5X}] [{2:5X}]'.format(11, -22, 33))  # 16진수 대문자

# 표준 입력
print('이름을 입력하세요', end="")
name = input()
print("이름 : {0}, type : {1}".format(name, type(name)))
name = input('이름을 입력하세요 ')
print("이름 : {0}, type : {1}".format(name, type(name)))
name = input('아무것도 입력하지 말고 EOF(Ctrl+D 또는 Ctrl+Z+Enter)를 입력해보세요')
