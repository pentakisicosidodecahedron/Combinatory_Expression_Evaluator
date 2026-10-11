# COMBINATORY EXPRESSION EVALUATOR
# By Hayden Becker for OCCHacks 2026

To use this, cd into the project's directory and run the
following:

$ ./main.py

This will start the GUI frontend for the combinatory expression
evaluator.

# USAGE

Enter a valid combinatory expression in the top text prompt. The
allowed combinators include S, K, I, B, W, and C. For intended
functionality pleace use exclusively these symbols, lowercase
letters for variables, and parentheses. OMIT ALL WHITESPACE.

## Example Expressions to Try:

Ix                      -- Evaluates to x
Kxy                     -- Evaluates to x
Sxyz                    -- Evaluates to (xz(yz))
Bxyz                    -- Evaluates to (x(yz))
Cxyz                    -- Evaluates to (xzy)
Wxy                     -- Evaluates to (xyy)
(S(K(SI))(S(KK)I)xy)    -- Evaluates to (yx)
WKx                     -- Has the same effect as Ix
SKKx                    -- Has the same effect as Ix
B(BW)(BBC)xyz           -- Has the same effect as Sxyz

# CAVEAT

If the front term is a combinator, and the combinator lacks
enough terms to apply to, the evaluator ceases to evaluate any
further. This is an unintented side effect of the implementation
of the evaluator, but shouldn't occur very often.
