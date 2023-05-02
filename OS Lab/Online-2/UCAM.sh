#!/bin/bash

# Functions
function new_dept() {
    dept_name="$1.txt"

    if [ -f $dept_name ]; then
        echo "Department already exists!"
    else
        echo "">$dept_name
    fi
}

function del_dept() {
    dept_name="$1.txt"

    if [ -f $dept_name ]; then
        rm -rf $dept_name
    else
        echo "Department doesn't exists!"
    fi
}

function new_student() {
    name=$1
    id=$2
    dept=$3
    dept_file="$3.txt"
    empty=""

    result=`find -type f -name $dept_file 2>/dev/null`

    if [ $result == $empty ] 2>/dev/null; then
        echo "Department not found!"
    else
        str="$name $id $dept"
        st_search=`cat *.txt | grep -c "$name $id $dept"`

        if [ $st_search == 0 ] 2>/dev/null; then
            echo $str>>$dept_file
        else
            echo "Student already exists in db!"
        fi
    fi
}

function del_student() {
    name=$1 # or id
    files=`grep -l "$name" *.txt`
    tmp="temp.txt"

    for file in $files
    do
        grep -v "$name" $file >$tmp
        mv "$tmp" "$file"
    done
}

# Main
function main() {
    cmd=$1
    if [ $cmd == "dept_new" ]; then
        new_dept $2
    elif [ $cmd == "dept_del" ]; then
        del_dept $2
    elif [ $cmd == "student_new" ]; then
        new_student $2 $3 $4
    elif [ $cmd == "student_del" ]; then
        del_student $2
    fi
}


# Driver
main $@