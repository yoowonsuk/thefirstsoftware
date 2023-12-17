#! /bin/bash

f=$(find . -type d)

#for i in $f;
for i in $(find . -type d);
do
if [ $i != "./hot-folder" ]; then
	echo "****************this is the folder: $i"
	for myfile in $i/*;
	do
		if [ -f $myfile ]; then
			echo "the file inside is: $myfile"
			check=$(grep -ni "spo" "$myfile")
			if [ -z "$check" ]; then
				echo "EMPTY"
			else
				echo "FOUND!"
			fi
		fi
	done
fi
done

# basename ./Mydir/anotherfold/salt.txt => salt.txt
