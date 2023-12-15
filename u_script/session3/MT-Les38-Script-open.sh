#! /bin/bash


read -p "what is your name? " yourname
echo "hello $yourname   nice to meet you"

echo "tell me the path of the file you want to open "
read filepath

xdg-open $filepath

# ************* COMMENT for the Student ***************
# If you are using the command line on a MAC Computer *
# intead of  "xdg-open"   use  the command   "open"   *
# See the lesson in Section 1: "Open, Xdg-open"		  *
# *************Comment for the Student*****************

echo ------------------------*


