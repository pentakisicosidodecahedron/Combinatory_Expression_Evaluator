#! /usr/bin/env python3

import sys

ev_out = list(map(lambda x : x[:-1], sys.stdin.readlines()))
exprs = ev_out[:ev_out.index("EXPLANATION START")]
expln = ev_out[ev_out.index("EXPLANATION START") + 1:]

SPACING = max(map(len, exprs))

exprs_index = 0

for ex in expln:
    if ex[0] != " ":
        print(exprs[exprs_index] + (" " * (SPACING - len(exprs[exprs_index]) + 1) + ex))
        exprs_index += 1
    else:
        print(" " * SPACING + ex)
