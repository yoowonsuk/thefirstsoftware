#! /bin/bash


for myfile in  * ; do
	if [ -f "$myfile" ]; then
		echo "this is a file: $myfile"

		grep -ni "spo" "$myfile"
	else
		echo "$myfile  is not a file"
		echo " "
	fi
done

