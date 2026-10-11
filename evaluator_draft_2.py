#! /usr/bin/env python3

# Combinator Expression Evaluator
#
# This program takes an expression of combinators (S, K, I, B,
# C, W) and variables (a, b, c, ..., x, y, z) through stdin. It
# outputs a series of reductions which ends on the expression's
# irreducible form.
#
# Expressions consist of the previously mentioned symbols as
# well as parentheses for precedence (really, inserting
# expressions WITHIN expressions). So a valid expression may
# look like this: "B(BW)(BBC)KKx". Note that outermost
# parentheses may be omitted.
#
# By Hayden Becker for OCCHacks 2026.

# TODO
# Make this more "educational"?

import sys

S = "S"
K = "K"
I = "I"
B = "B"
C = "C"
W = "W"

# Number of parameters required per combinator
C_PARS = {
    S: 3,
    K: 2,
    I: 1,
    B: 3,
    C: 3,
    W: 2
}

COMBINATORS = [S, K, I, B, C, W]

verbose_output = []

# Helper function for comb_format
def append_at_level(arr, depth, elem):
    access_level = arr
    for i in range(depth):
        access_level = access_level[-1]
    access_level.append(elem)
    return arr

# Convert the expression into a more useful format
def comb_format(expr):
    if expr[0] == "(" and expr[-1] == ")":
        expr = expr[1:-1]
    depth = 0
    acc = []
    for c in expr:
        if c == "(":
            acc = append_at_level(acc, depth, [])
            depth += 1
            continue
        if c == ")":
            depth -= 1
            continue
        acc = append_at_level(acc, depth, c)
    return acc

# Convert the expression into human-readable format
def comb_unformat(expr):
    unfo = "("
    for c in expr:
        if type(c) == list:
            unfo += comb_unformat(c)
        else:
            unfo += c
    unfo += ")"
    return unfo

# Determine if an expression is irreducible
def only_variables(expr):
    for c in expr:
        if c in COMBINATORS:
            return False
        if type(c) == list and not only_variables(c):
            return False
    return True

# Perform a singular reduction according to a given combinator and following sequence of terms
# A helper function for comb_eval
def comb_step(c, expr):
    newexpr = []
    if c == S: # Sxyz = xz(yz)
        verbose_output.append("Apply the S combinator to the next three terms.")
        newexpr.extend([expr[0], expr[2], [expr[1], expr[2]]])
        newexpr.extend(expr[3:])
    elif c == K: # Kxy = x
        verbose_output.append("Apply the K combinator to the next two terms.")
        newexpr.extend([expr[0]])
        newexpr.extend(expr[2:])
    elif c == I: # Ix = x
        verbose_output.append("Apply the I combinator to the next term.")
        newexpr.extend(expr[0])
        newexpr.extend(expr[1:])
    elif c == B: # Bxyz = x(yz)
        verbose_output.append("Apply the B combinator to the next three terms.")
        newexpr.extend([expr[0], [expr[1], expr[2]]])
        newexpr.extend(expr[3:])
    elif c == C: # Cxyz = xzy
        verbose_output.append("Apply the C combinator to the next three terms.")
        newexpr.extend([expr[0], expr[2], expr[1]])
        newexpr.extend(expr[3:])
    elif c == W: # Wxy = xyy
        verbose_output.append("Apply the W combinator to the next two terms.")
        newexpr.extend([expr[0], expr[1], expr[1]])
        newexpr.extend(expr[2:])
    else:
        pass
    return newexpr

def comb_eval(expr, depth):
    print("\"   " * depth + comb_unformat(expr))
    
    # Case: the expression is definitively irreducible (contains no combinators nor sub-expressions)
    if only_variables(expr):
        verbose_output.append("The expression is irreducible.")
        return expr
    
    # Case: the first element is a variable, but the rest of the expression may be reducible
    if (expr[0] not in COMBINATORS and type(expr[0]) == str):
        verbose_output.append("The front term is not a specified combinator, so we focus on the rest of the expression to the right.")
        newexpr = [expr[0]]
        newexpr.extend(comb_eval(expr[1:], depth + 1))
        return comb_eval(newexpr, depth)

    # Case: the first element is a combinator and there are not enough arguments
    if type(expr[0]) == str and C_PARS[expr[0]] >= len(expr):
        verbose_output.append("There are not enough arguments for the combinator in the front to apply.")
        return expr
    
    # Case: there are enough arguments for the first element, which is a combinator
    if expr[0] in COMBINATORS:
        return comb_eval(comb_step(expr[0], expr[1:]), depth)

    # Catch-all Case: the current expression is a sub-expression (not a lone combinator or variable)
    verbose_output.append("The front term is a sub-expression which we will now focus on.")
    newexpr = comb_eval(expr[0], depth + 1)
    newexpr.extend(expr[1:])
    return comb_eval(newexpr, depth)

comb_eval(comb_format(sys.stdin.readlines()[0][:-1]), 0)

if "-v" in sys.argv or "--verbose" in sys.argv:
    print("EXPLANATION START")
    for line in verbose_output:
        print(line)
