import textwrap


def feedbackReview(feedback, size):
    return textwrap.wrap(feedback, size)


show = "This is an example feedback"
size = 8
print(feedbackReview(show, size))
# 공식 문서 : https://python.flowdas.com/library/textwrap.html?highlight=textwrap
