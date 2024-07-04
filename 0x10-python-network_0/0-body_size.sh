#!/bin/bash
# script that takes in URL, sends request to URL, and displays size of body of response
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
