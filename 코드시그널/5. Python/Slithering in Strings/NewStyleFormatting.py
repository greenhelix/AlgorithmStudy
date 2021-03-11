import re


def newStyleFormatting(s):
    res = s.split("%%")
    for item in res:
        if item.find("%") != -1:
            print(item.find('%'))
            res[res.index(item)] = re.sub(
                "%[ofdtscxg]", '{}', res[res.index(item)])
    return '%'.join(res)


s = "We expect the %f%% growth this week"
s2 = "Much %%s we have here!"

print(newStyleFormatting(s))
print(newStyleFormatting(s2))
