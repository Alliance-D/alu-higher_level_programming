#!/bin/bash
# script that takes URL as arg sends GET request with additional info
curl -sX GET $1 -H "X-HolbertonSchool-User-Id: 98" -L
