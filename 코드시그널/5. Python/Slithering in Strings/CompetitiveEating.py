def competitiveEating(t, width, precision):
    return format(t, ".%df" % precision).center(width, ' ')


t = 3.1415
width = 10
precision = 2
print(competitiveEating(t, width, precision))
#"   3.14   "
