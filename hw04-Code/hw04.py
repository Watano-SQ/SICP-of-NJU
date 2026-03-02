"""Homework 4: Data Abstraction and Trees"""

from copy import deepcopy
from ADT import tree, label, branches, is_leaf, print_tree, copy_tree

#####################
# Required Problems #
#####################


# Problem 1.1
def fn_empty():
    """Return an empty function.

    >>> fn_empty()
    []
    """
    "*** YOUR CODE HERE ***"
    return []


def fn_remap(fn, x, y):
    """Return a new function that is the same as fn except that it maps x to y.

    >>> f = fn_remap(fn_empty(), 1, 2)
    >>> f
    [[1, 2]]
    >>> fn_remap(f, 1, 3)
    [[1, 3]]
    >>> fn_remap(f, 2, 3)
    [[1, 2], [2, 3]]
    """
    "*** YOUR CODE HERE ***"
    fnn = deepcopy(fn)
    for i in fnn:
        if i[0] == x:
            index = fnn.index(i)
            fnn.pop(index)
            fnn.insert(index,[x,y])
            return fnn
    fnn.append([x,y])
    return fnn


def fn_domain(fn):
    """Return a sorted list of all the inputs (domain) of fn.
    Note that if fn maps x to None, then x is not in the domain of fn.

    >>> fn_domain(fn_remap(fn_remap(fn_empty(), 1, 2), 2, 3))
    [1, 2]
    >>> fn_domain(fn_remap(fn_remap(fn_empty(), 2, 3), 1, 2))
    [1, 2]
    >>> fn_domain(fn_empty())
    []
    >>> fn_domain(fn_remap(fn_empty(), 1, None))
    []
    """
    "*** YOUR CODE HERE ***"
    res = []
    for i in fn:
        if i[1]:
            res = [i[0]] + res
    res.sort()
    return res


def fn_call(fn, x):
    """Return the result of applying fn to x.
    If fn does not map x to a value, return None.

    >>> fn_call(fn_remap(fn_empty(), 1, 2), 1)
    2
    >>> fn_call(fn_remap(fn_remap(fn_empty(), 1, 2), 2, 3), 2)
    3
    >>> fn_call(fn_remap(fn_remap(fn_empty(), 1, 2), 2, 3), 1)
    2
    >>> fn_call(fn_empty(), 1) is None
    True
    """
    "*** YOUR CODE HERE ***"
    for i in fn:
        if i[0] == x:  #删除了 and i[1] 则变成了满分。
            return i[1]


# Problem 1.2
def fn_ext(fn1, fn2):
    """Return whether fn1 and fn2 represent the same function.
    Two functions are the same if and only if they have the same domain
    and output the same value for each input in the domain.

    >>> f = fn_remap(fn_empty(), 1, 2)
    >>> g = fn_remap(fn_empty(), 2, 3)
    >>> fn_ext(f, g)
    False
    >>> fn_ext(fn_remap(f, 2, 3), g)
    False
    >>> fn_ext(fn_remap(f, 2, 3), fn_remap(g, 1, 2))
    True
    """
    "*** YOUR CODE HERE ***"
    domain1 = fn_domain(fn1)
    domain2 = fn_domain(fn2)
    if domain1 != domain2:
        return False
    else:
        check = 0
        for i in domain1:
            if fn_call(fn1,i) != fn_call(fn2,i):
                check = 1
        if check == 1:
            return False
        else:
            return True
# 50 分
# 100 分

def fn_compose(fn1, fn2):
    """Return a new function that is the composition of fn1 and fn2.
    The composition of two functions fn1 and fn2 is a function fn such that
    fn(x) = fn1(fn2(x)) for every x in the domain of fn2.

    >>> f = fn_remap(fn_empty(), 2, 3)
    >>> g = fn_remap(fn_empty(), 1, 2)
    >>> h = fn_compose(f, g)
    >>> fn_call(h, 1)
    3
    >>> fn_call(h, 2) is None
    True
    """
    "*** YOUR CODE HERE ***"
    #h = fn_empty()
    #for i in fn2:
    #    h = fn_remap(h,i[0],fn_call(fn1,i[1]))
    #return h
    domain = fn_domain(fn2)
    composed = fn_empty()
    for i in domain:
        composed = fn_remap(composed,i,fn_call(fn1,fn_call(fn2,i)))
    return composed
# 50 分
# 50 分
# 100 分


def fn_inverse(fn):
    """Return a new function that is the inverse of fn.
    The inverse of a function fn is a function fn_inv such that
    fn_inv(y) = x if and only if fn(x) = y.
    If fn is not invertible, return None.

    >>> f = fn_remap(fn_remap(fn_empty(), 1, 2), 2, 3)
    >>> fn_call(fn_inverse(f), 3)
    2
    >>> g = fn_remap(fn_remap(fn_empty(), 1, 2), 2, 2)
    >>> fn_inverse(g) is None
    True
    """
    "*** YOUR CODE HERE ***"
    domain1 = fn_domain(fn)
    for i in domain1:
        if fn_call(fn,i) is None:
            return None
    inverse = fn_empty()
    for i in domain1:
        inverse = fn_remap(inverse,fn_call(fn,i),i)
    if len(domain1) == len(fn_domain(inverse)):
        return inverse
    else:
        return None
# 50 


# Problem 2.1
def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    new_label = label(t1) + label(t2)
    new_branches = []
    br1 = branches(t1)
    br2 = branches(t2)
    max_len = max(len(br1),len(br2))
    
    for i in range(0,max_len):
        t1_yes = i < len(br1)
        t2_yes = i < len(br2)

        if t1_yes and t2_yes:
            new_branches.append(add_trees(br1[i],br2[i]))
        elif t1_yes:
            new_branches.append(copy_tree(br1[i]))
        elif t2_yes:
            new_branches.append(copy_tree(br2[i]))
    return tree(new_label,new_branches)     


# Problem 2.2
def bigpath(t, n):
    """Return the number of rooted paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigpath(t, 3)
    4
    >>> bigpath(t, 6)
    2
    >>> bigpath(t, 9)
    1
    """
    "*** YOUR CODE HERE ***"
    def count_paths(t):
        if is_leaf(t):
            return 1
        return 1 + sum([count_paths(b) for b in branches(t)])
    
    if label(t) >= n:
        return count_paths(t)
    else:
        count = 0
        for b in branches(t):
            count += bigpath(b,n-label(t))
        return count
    



# Problem 2.3
def bigger_path(t, n):
    """Return the number of general rooted paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigger_path(t, 3)
    9
    >>> bigger_path(t, 6)
    4
    >>> bigger_path(t, 9)
    1
    """
    "*** YOUR CODE HERE ***"
    count = 0
    if is_leaf(t):
        if label(t) >= n:
            return 1
        else:
            return 0
    for b in branches(t):
        count += bigger_path(b,n)
    count += bigpath(t,n)
    return count 

# Problem 2.4
def has_path(t, word):
    """Return whether there is a rooted path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    """
    assert len(word) > 0, "no path for empty word."
    "*** YOUR CODE HERE ***"
    words = list(word)
    if len(words) == 1:
        if words[0] == label(t):
            return True
        else:
            return False
    res = False
    if label(t) == words[0]:
        word = word[1:]
        br = branches(t)
        for b in br:
            res = (has_path(b,word) or res)
        return res
    else:
        return False


##########################
# Just for fun Questions #
##########################


# Problem 3
def fold_tree(t, base_func, merge_func):
    """Fold tree into a value according to base_func and merge_func"""
    "*** YOUR CODE HERE ***"


def count_leaves(t):
    """Count the leaves of a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> count_leaves(t)
    3
    """
    return fold_tree(t, "YOUR EXPRESSION HERE", "YOUR EXPRESSION HERE")


def label_sum(t):
    """Sum up the labels of all nodes in a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> label_sum(t)
    15
    """
    return fold_tree(t, "YOUR EXPRESSION HERE", "YOUR EXPRESSION HERE")


def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> preorder(t)
    [1, 2, 3, 4, 5]
    """
    return fold_tree(t, "YOUR EXPRESSION HERE", "YOUR EXPRESSION HERE")


def has_path_fold(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path_fold(greetings, 'h')
    True
    >>> has_path_fold(greetings, 'i')
    False
    >>> has_path_fold(greetings, 'hi')
    True
    >>> has_path_fold(greetings, 'hello')
    True
    >>> has_path_fold(greetings, 'hey')
    True
    >>> has_path_fold(greetings, 'bye')
    False
    """
    assert len(word) > 0, "no path for empty word."

    def base_func(l):
        return "YOUR EXPRESSION HERE"
    def merge_func(l, bs):
        return "YOUR EXPRESSION HERE"

    return fold_tree(t, base_func, merge_func)(word)
