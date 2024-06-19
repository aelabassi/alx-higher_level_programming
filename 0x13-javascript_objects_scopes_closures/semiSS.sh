#!/bin/bash
file="$1"
echo "Checking $file code with semistandard..."
semistandard "$file"
if [ $? -eq 0 ]; then
    echo "No semistandard errors!"
else
    echo "Semistandard errors!"
fi


