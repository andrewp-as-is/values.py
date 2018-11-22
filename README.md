[![](https://img.shields.io/pypi/pyversions/values.svg?longCache=True)](https://pypi.org/pypi/values/)
[![](https://img.shields.io/pypi/v/values.svg?maxAge=3600)](https://pypi.org/pypi/values/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/values.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/values.py/)

#### Install
```bash
$ [sudo] pip install values
```

#### Functions
function|description
-|-
`values.get(input)`|return list with input values or [] if input is None

#### Examples
```python
>>> import values
>>> values.get(1)
[1]

>>> values.get("string")
["string"]

>>> values.get([1,2])
[1,2]

>>> values.get(None)
[]
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>