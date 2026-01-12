## over the wire 
# Bandit 
## level 0
connecting over port
used ssh bandit0@bandit.labs.overthewire.org -p 2220.
-p for port 2220
ssh username@remote_host -p 2222
username bandit0
password bandit0

## level 0-1
used ls to view files in the directory 
and cat readme to view the contents of the file 
with password for level one being ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

## level 1-2
use ssh with username - bandit1
ls , cd , cat , file , du , find >> helpful commands 
used ls to see a file called - and used cat ./- to read the file
263JGJPfgU6LtdEvgfWU1XP5yac29mFx

## level 2-3
there is a file with the name --spaces in this filename--

so with a dash infront, use ./ to execute and since it has spaces use "quotes to signify one file name"
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

## level 3-4
there is a directory named inhere. It looks empty on the surface (ls) but with (ls - a) you see the hidden file >> ...Hiding-From-You
2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

## level 4-5
within the folder (inhere), there are 10 files.using file ./(to counter the dash), with the file name, you can see the type of data within. eg. "file ./-file00"
using "file ./*" will return data type for all
finally a filtered version will be 'file ./* | grep "text"'
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

## level 5-6
when looking for a file you need to use find 
so find . looks inside the directory
find . -type f -size 1033c ! -executable
type f is file 
if name -name "fjijfo" 
and c 1033 c is for 1033 characters. 
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

## level 6-7
so it is on the server but you dont know where.
switch to root cd /
find -user bandit7 -group bandit6 -size 33c
since the noise is too much, take outputs category 2 (errors) and send them to ./dev/null
2 > ./dev/null
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

## level 7-8
Commands needed
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

solution 
cat data.txt | grep "millionth"
print out the contents of data.txt and find millionth
dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
print out data.txt and find millionth.
or find the line with millionth in data.txt
grep "millionth" data.txt

## level 8-9
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
with tldr sort and uniq
the best comination of commands is sort data.txt | uniq -u from tldr uniq.
sort the data first then return the unique one.

## level 9-10
FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
we use strings here to print out all strings 
since the password is preceded by a "=" use | grep "="

## level 10-11
dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

tldr base64 you'll see the command for decoding
base64 -d data.txt 

## level 11-12
7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

using cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m' so A-Z is 26 and the to written twice is 13 + 13

## level 12-13
Commands you may need to solve this level
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd, mkdir, cp, mv, file
so use cd $(mktemp -d) to create a temp dir in /tmp
cp to tmp folder
Use file along the way to check for file-type.
use xxd -r mystery for the file
use gzip -d to further decompress
use bz2 -d to further decompresss
use tar xvf to further decompresss reveling data5.bin
use tar xf to reveal data6.bin
use tar xvf to reveal data8.bin
file again
use gzip -d to unzip it and reveal data8
file it and if its ascii text, cat data8 and you get;
The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn

## level 13-14
commands needed
ssh, scp, umask, chmod, cat, nc, install
so you can choose to ssh download the file or cat the contents when you ls and copy and echo it to a file on your machine.
so ssh bandit14@bandit.labs.overthewire.org -p 2220 -i private.key then cat/etc/bandit_pass/bandit14
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS


