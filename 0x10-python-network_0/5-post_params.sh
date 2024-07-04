#!/bin/bash
# post request to the passed URL, and display the body of the response, and sends a variable email, and subject
curl -s -X POST -d "email:test@gmail.com&subject:I will always be here for PLD" "$1"
