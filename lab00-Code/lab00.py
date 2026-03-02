def twenty_twenty_five():
    """Come up with the most creative expression that evaluates to 2025,
    using only numbers and the +, *, and - operators.

    Expected result:
    >>> twenty_twenty_five()
    2025
    """
    return 80+82+79+71+82+65+77+77+73+78+71+32+73+78+32+80+89+84+72+79+78+32+73+83+32+70+85+78+33+7
'''
本来想用Unicode编码和ord(),但无奈题目要求不允许,以及我实在凑不出来:PROGRAMMING IS FUN! 的编码之和是2018.最后的7是硬加上去的.
'''

def sum(a, b):
    """Compute the sum of a and b.

    Expected result:
    >>> sum(1, 2)
    3
    >>> sum(3, 8)
    11
    """
    return a+b


def diff_square(a, b):
    """Compute the difference of square a and square b.

    Expected result:
    >>> diff_square(3, 2)
    5
    >>> diff_square(3, 4)
    -7
    """
    return a**2 - b** 2
