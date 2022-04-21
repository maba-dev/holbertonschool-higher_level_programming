#!/bin/bash
# the size of the body 
curl -sI "$s1" | grep -i Content-Length
