#!/bin/bash
# script that sends a DELETE request to the URL as the first argument and displays the body of the message
curl -sX DELETE "$1"
