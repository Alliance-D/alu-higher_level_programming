#!/usr/bin/python3
# prints alphabetical letter except q and e
for i in range(97, 123):
    if chr(i) not in ['q', 'e']:
        print("".join(chr(i)), end=" ")
