#!/bin/bash
#show the methods
curl -s -I $1 | grep "Allow" | cut -d ' ' -f2-
