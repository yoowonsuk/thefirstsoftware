#! /bin/bash

mkdir ./hot-folder

for myfile in * # either ;
do
	if [ -f "$myfile" ]; then
		echo "$myfile"
		grep -in "spo" $myfile
		check=$(grep -ni "spo" "$myfile")
		if [ -z "$check" ]; then
			echo "EMPTY"
		else
			echo "FOUND!"
			cp "$myfile" ./hot-folder
			echo " "" >> hot-folder/"$myfile"

		fi
        else 
		ecoh "$myfile is NOT a file.."
	fi
done


# a=$(grep "spo" new.txt")
