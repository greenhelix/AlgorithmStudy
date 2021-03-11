def convertTabs(code, x):
    return code.replace('\t', ' '*x)


code = "\treturn False"
x = 4
print(convertTabs(code, x))
