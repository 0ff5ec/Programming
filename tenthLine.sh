#!/bin/bash
# Read from the file file.txt and output the tenth line to stdout.
declare -i cnt=1
while read LINE; do
    if [ $cnt -eq 10 ]; then
        echo $LINE
    fi
    cnt=$(($cnt+1))
done < "file.txt"
