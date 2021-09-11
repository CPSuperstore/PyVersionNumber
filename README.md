# PyVersionNumber
A small library for handling Semantic Version Numbers

## Installation
```shell
pip install PyVersionNumber
```

## Usage
The following code sample shows the two ways to instantiate the `VersionNumber` class:
```python
import PyVersionNumber

version = PyVersionNumber.VersionNumber("1.2.6")
```

OR

```python
import PyVersionNumber

version = PyVersionNumber.VersionNumber(1, 2, 6)
```

From there, you can compare version numbers, perform mathematical operations on two version numbers, 
print the number out to the console (or cast to a string), 
or see if the version number indicates the product is in development 
according to Semantic Versioning Standards (the Major number = 0)

It is a very small and simple library which has many uses. Enjoy!

## Contributing
If you wish to contribute, submit a PR and I would be happy to review it!