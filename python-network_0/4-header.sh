#!/bin/bash
# script that takes URL as arg sends GET request with additional info
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
