#!/usr/bin/env python
import values


assert values.get(1) == [1]                         # list from non iterable
assert values.get("string") == ["string"]           # list from string
assert values.get([1, 2]) == [1, 2]                 # list from list
assert values.get(filter(None, [1, 2])) == [1, 2]   # list from filter
assert values.get(map(int, [1, 2])) == [1, 2]       # list from map

assert values.get(None) == []                       # list from None
assert values.get("") == [""]                       # list from empty string
