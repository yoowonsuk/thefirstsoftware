#! /bin/bash

echo $?
=> 0

pwd -asdfsdf
echo $?
=> 1


pasdfs
echo $?
=> 127

# man pwd
# man grep

grep "end" $file
echo $?
=> 0 or 1

file not there
=> 2

mydate() {
    echo "function"
}

hello2() {
    echo "hello $1 "
    echo "hello also to $2 "
}

hello2 "Mark" "blabla"

return 35
$?

variable in function is global variable
local var="Eggs"





