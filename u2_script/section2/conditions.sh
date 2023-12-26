#! /bin/bash

d="hello";

if [ "$d" == "hello" ]; then
	echo "hello to you!"
else
	echo "NOT helllo..."
fi

echo -e "\n the program continue"

# read d
# elif
if [ -z "$d" ]; then
	echo "Empty String"
fi

if [ -n "$d" ]; then
	echo "NON Empty String"
fi

# != different


if [ ! -z "$d" ]; then
	echo "NON Empty String"
fi
