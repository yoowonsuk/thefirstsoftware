#! /bin/bash

echo "***** Calculator Script *****"

if [ "$1" == "-p" ]; then
	precision=$2
	shift 2
else
	precision=3
fi

bc << _EOF_
scale=$precision
$@ # not $1
_EOF_
