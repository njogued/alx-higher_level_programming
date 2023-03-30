#!/bin/bash
# Display the Content-Length of the site provided as arg
curl -sI $1 | grep 'Content-Length' | awk '{print $2}'
