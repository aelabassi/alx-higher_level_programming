#!/bin/bash
# sends a GET request to the URL, and displays the body of the response, and sends a header variable
curl -s -H "X-School-User-Id: 98" "$1"
