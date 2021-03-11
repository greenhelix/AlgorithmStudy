def permutationCipher(password, key):
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz", key)
    return password.translate(table)


def elitePermutationCipher(pw, key):
    table = str.maketrans(string.ascii_lowercase, key)
    return pw.translate(table)


sample1 = "iamthebest"
key1 = "zabcdefghijklmnopqrstuvwxy"
sample2 = "codesignalrocks"
key2 = "ebtyfkudagizxmvcnojqwlsrhp"

print(permutationCipher(sample1, key1))
print(permutationCipher(sample2, key2))
