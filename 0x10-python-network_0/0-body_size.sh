#!/bin/bash
# the size of the body 
curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f2
