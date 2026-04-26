# THE SHELL

## 2. ls
ls - lists all visible files and folders in the current dir

ls -l on the other hand lists permissions and other info about all files and folders present.

## 3. glob
glob is an expression that lets you specify the return of what you are looking for like finding all zip files

## 4. quoting
Single quotes behave like strings
Double quotes allow commands to be placed within as well
Ansi quoting allow edits to outputs like \n for newline

You have to use the ansi quote $'' to complete the example cd tempdir || ( mkdir tempdir && cd tempdir)

## 5 Redirecting
stdin takes input from keyboard
stdout is successful output
stder is error messages

use the &> to move them to one file.

## 6 Executing if one fails
|| runs if the first command fails
cd tmp/mydir || (mkdir tmp/mydir && cd tmp/mydir)

## 7. CD
cd is built in because the shell is changing directories internally other wise the external cd will change if it was not in built and you'll be stuck in your dir forever.

## 8. testing 
use tesf -f or [ -f ...]
test -d mydir && echo "it exists" 
otherwise it'll run but you'll have no feedback

## 9. saved and run the script
use chmod +x filename to make it executable and ./filename to run it

## 10. adding set -x 
adding set -x to the script prints out each line of commands before they are run.

## 11. Backing up a file
The cp command copies a file.

## 12. $1 or $@
Putting one of these in place of the file name in the script make the argument you pass the basis for the script.

## 13. Finding the top 5 extensions in home dir.
find . -type f | grep -oE '\.[a-zA-Z0-9]+$' | sort | uniq -c | sort -nr | head -n 5

find all files pipe it and grab .extensions of any kind sort them and count them uniquely and sort again in reverse and print first 5

## 14. finding files with spaces in file names
find . -type f -name "*.sh" -print0 | xargs -0 -l

## 15. Curl
curl -s https://missing.csail.mit.edu/ | grep -E "[0-9]{1,2}/[0-9]{1,2}/[0-9]{2,4}"

curl -s removes the progress bar

## 16. Jq
A json data file processor
jq must be installed first.
curl -s https://microsoftedge.github.io/Demos/json-dummy-data/64KB.json | jq '.[] | .name'
to get the list of names

curl -s https://microsoftedge.github.io/Demos/json-dummy-data/64KB.json | jq '.[] | select(.version > 6) | .name, .version'
to get the names of those with versions > 6 
the , and .version adds the accompanying version number.

## 17. Filtering Lines
printf 'a 50 x\nb 150 y\nc 200 z\n' | awk '$2 > 100'
awk takes the data and returns those with middle column > 100:

## 18. Finding my most used commands
cat ~/.bash_history | awk '{print $1}' | sort | 
uniq -c | sort -nr | head -n 5
    672 git
    572 cd
    392 /usr/bin/python3
    115 ts
     72 tt