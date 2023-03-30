#!/bin/bash
# Display the Content-Length of the site provided as arg

address=$1
curl -sI $address | grep 'Content-Length' | awk '{print $2}'
