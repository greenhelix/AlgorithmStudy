# https: // www.acmicpc.net / problem / 1152
# 구현 / 문자열
# 대소문자,띄어쓰기 문자열 IN
# 단어 갯수? OUT
# 1. 앞뒤 공백 가능성 없음
# The Curious Case of Benjamin Button -> 6
# Teullinika Teullyeotzi  -> 2

sentence = list(map(str, input().split()))
print(len(sentence))
