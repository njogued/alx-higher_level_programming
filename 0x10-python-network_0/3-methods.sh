#!/bin/bash
# Display all HTTP methods in Allow
curl -sI $1 | grep "^Allow" | cut -d ' ' -f 2-
