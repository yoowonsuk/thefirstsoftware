#! /bin/bash

echo "$1"
echo "$2"
echo "${12}"
echo "$#"

echo "$@"
echo "$*"

for $@ $* same
for "$@" "$*" difference

shift
$1 $2 => $2 $3
a b c d => b c d
$# 4 => 3

shift 3 => $4 -> $1
$0 => absoulte path

calc 3+4
calc -p 10 (12/7)   # -p decimal point
