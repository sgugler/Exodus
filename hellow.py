import matplotlib.pyplot as plt
import numpy as np
import functools as ft


def cantor(x):
    xb3 = np.base_repr(x, 3)
    # print(xb3)

    string = str(xb3)

    chars = []
    count = 1

    for ch in string:
        if str(ch) == str(1):
            chars.append(str(1))
            break
        else:
            chars.append(str(ch))
            count += 1
            # print(count)

    for i in range(0, len(string) - count):
        chars.append(str(0))

    # print(chars)

    chars2 = []

    for i in range(len(chars)):
        if chars[i] == str(2):
            chars2.append(1)
        if chars[i] == str(1):
            chars2.append(1)
        if chars[i] == str(0):
            chars2.append(0)

    # print(chars2)

    result = ft.reduce(lambda a, b: a + str(b), chars2, '')

    # print(result)
    result2 = int(result, 2)

    # print(result2)

    return result2


x = np.arange(100)
y = []

for i in x:
    # print(cantor(i))
    y.append(cantor(i))
    #
print(y)
plt.plot(x, y)
plt.show()
