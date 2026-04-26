set -x
find . -type f | grep -oE '\.[a-zA-Z0-9]+$' | sort | uniq -c | sort -nr | head -n 5
