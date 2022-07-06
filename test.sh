#!/bin/bash

read line

a=`echo "$line" | cut -d' ' -f1`
b=`echo "$line" | cut -d' ' -f2`

let c=a+b
echo $c
