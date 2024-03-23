#!/bin/bash
# script that takes URL as arg sends GET request with additional info
curl -sSL -H "X-HolbertonSchool-User-Id: 98" "$1"
