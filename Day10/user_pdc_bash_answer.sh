#!/bin/bash

# THIS IS NOT MY CODE!!
# this is a solution to todays problem
# written up by /u/_pdc_
# I thought it was cool so I've stored it here
# uniq -c does all the work

in="1113222113";
for f in {1..40}; do
    # takes "$in" | splits into separate characters | counts how many of each | replaces paragraphs with spaces | removes spaces
    in=$(echo "$in" | fold -w1 | uniq -c | tr '\n' ' ' | tr -d ' ')
    # prints: new $in | removes paragraph at eol | counts characters
    echo $in | tr -d '\n' | wc -c
done