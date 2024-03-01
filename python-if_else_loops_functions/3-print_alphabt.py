#!/usr/bin/python3
#prints alphabetical letter except q and e
print("".join(chr(x) for x in range(97, 123) if chr(x) not in ['q', 'e']), end="")
