<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/values.svg?longCache=True)](https://pypi.org/project/values/)
[![](https://img.shields.io/pypi/v/values.svg?maxAge=3600)](https://pypi.org/project/values/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/values.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/values.py/)

#### Installation
```bash
$ [sudo] pip install values
```

#### Functions
function|`__doc__`
-|-
`values.get(input)` |return a list with input values or [] if input is None

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

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>