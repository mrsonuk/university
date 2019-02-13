#!/bin/bash

. "$(dirname "$0")/__init.sh"

if [ -z $1 ]; then
    echo "No name given. Aborting!"
    exit 1
else
    examName=$1
fi


examDir="$mainDir/$examName"
if [ ! -d "$examDir" ]; then
    >&2 echo "Directory \"$examDir\" does not exist!"
    exit 1
fi

inRel=$examName".tex"
outRel=$examName".pdf"
fileIn="$examDir/$inRel"
fileOut="$examDir/$outRel"
if [ ! -f "$fileIn" ]; then
    >&2 echo "Input file \"$fileIn\" does not exist!"
    exit 1
fi


echo "Performing magic. Please wait ..."
cd "$examDir"

pdflatex "$inRel"
# save return code to check
rc=$?
if [[ $rc != 0 ]]; then
    >&2 echo "Whoopsie! Something went wrong!"
    exit $rc
else
    echo "Moving PDF ..."
    cp "$outRel" ../
fi

echo "done!"


