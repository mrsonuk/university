#!/bin/bash

. "$(dirname "$0")/__init.sh"

function getExamNames() {
    cd "$mainDir"
    find * -maxdepth 0 -type d  ! \( -name "ci" -o -name ".*" \) \
    | sort --numeric-sort --reverse
}

examNames=$(getExamNames)

# print all names
printf "found: %s\n" "$(echo "$examNames" | sed 's/^\|$/"/g' | tr '\n' ' '  | sed 's/ $/\n/')"

# initialize error variables
declare -a errFiles
errCount=0

# try to build every exam
for name in $examNames
do
    echo ""
    echo "Pocessing \"$name\":"
    "$texDir/tex2pdf.sh" "$name" &> >(sed "s/^/  /")

    # keep track of files with errors
    rc=$?
    if [[ $rc != 0 ]]; then
       errFiles[errCount]="\"$name\""
       errCount=$(( $errCount + 1 ))
    fi
done
echo ""

# show a list of files with errors (if there are any)
if [[ $errCount != 0 ]]; then
    >&2 echo "Errors occured while processing the following $errCount exam(s):"
    >&2 echo "${errFiles[*]}"
    >&2 echo "(Detailed error messages should be printed above.)"
    exit 1
fi

echo "Everything is fine! :)"
exit 0

