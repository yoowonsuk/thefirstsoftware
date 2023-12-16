#! /bin/bash

echo "hello ..."

if [ 3 -eq 3 ]; then
	echo "yes they are the same"
fi

echo "continue with our program"
echo "bye"

-ne
-gt  >
-lt  <

-ge  >= greater or equal
-le



read -p "How old are you?" age
if [ $age -gt 100 ]; then #space is needed
	echo "you are not very young"
else
	echo "you are still very young"
fi

if [ $num == "1" ]; then
	echo "typed 1"
elif [ $num == "2" ]; then
	echo "typed 2"
else
	echo "none of the above"
fi

echo "line 1"
echo "line 2"
exit
echo "line 3"
echo "line 4"
echo "line 5"
echo "line 6"


or => -o
and => -a


string == !=

if [ -z $str ]; then
	echo "this is an empty string"
	exit
fi

if [ -z "$str" ]; then  # accept space
fi

myfile=nex.txt
if [ -e $myfile ]; then
	echo " $myfile EXISTS "
fi

if [ ! -e $myfile ]; then
	echo " $myfile Does Not EXISTS"
fi

if [ -d $myfile ]; then
fi

if [ -r $myfile ]; then # readable 
fi
# writeable -w
# excutable -x
# not empty -s
# file -f 




