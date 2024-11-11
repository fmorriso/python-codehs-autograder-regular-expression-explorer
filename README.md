# python-regular-expression-explorer
 project to test possible CodeHS Autograder logic for use in projects involving a Parallelogram.

## Regular Expressions
```python
pattern = r'\b\w+\s*=\s*Parallelogram\s*\(\s*\)'
```
The above regular expression pattern breaks down as follows:

*    \b asserts a word boundary, ensuring that the match starts at the beginning of a word.
*    \w+ matches one or more word characters.
*    \s*=\s* matches an equal sign surrounded by zero or more spaces.
*    Parallelogram matches the literal word "Parallelogram".
*    \s* matches zero or more spaces.
*    \(\s* matches a left parenthesis followed by zero or more spaces.
*    \s*\) matches zero or more spaces followed by a right parenthesis.
## Tools Used

| Tool    |  Version |
|:--------|---------:|
| Python  |   3.13.0 |
| PyCharm | 2024.2.3 |
| VSCode  |   1.95.2 |
## References
* [Creating CodeHS Autograders](https://help.codehs.com/en/articles/2119075-creating-autograders-to-check-student-code)
* [pythex](https://pythex.org/)
* [RegEx 101](https://regex101.com/)
* [How to use Python to write a text file](https://datagy.io/python-write-text-file/)
## Change History

| Date       | Description                       |
|:-----------|:----------------------------------|
| 2024-11-10 | Change from GitLab back to GitHub |