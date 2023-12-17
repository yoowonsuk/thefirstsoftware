#! /bin/bash


# Change the name of the folder that you want to search
for myfile in * ; 
do
	if [ -f "$myfile" ]; then

		#echo "$myfile"

		check=$(grep -ni "spo" "$myfile")

		if [ -z "$check" ]; then
			echo "EMPTY"
		else
			echo "FOUND !"
		fi
	else
		echo "this is a directory: $myfile"
	fi
		echo "----------------------------"
done
