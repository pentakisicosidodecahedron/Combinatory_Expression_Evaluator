#! /bin/bash

echo "$1" | ./evaluator_draft_2.py -v | ./format_output.py
