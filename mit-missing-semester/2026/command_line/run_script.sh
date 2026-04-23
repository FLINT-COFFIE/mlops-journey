#!/usr/bin/env bash

count=1

# While the script returns a 0 (success), keep going
while ./your_script.sh; do
    count=$((count + 1))
done

echo "The script finally failed on run #$count"