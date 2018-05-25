# incorrect module header

Keywords: %incorrect module header

This error occurs when the start of your implementation or definition module is not correct. 

## Solutions

- An implementation module is a text file with file name <filename>.icl. Except for comments,
  the first line in the text file must be:

```clean
implementation module filename
```

  If the implementation module happens to be the main module (it contains the Start function),
  then the keyword `implementation` is allowed to be omitted.

- A definition module is a text file with file name <filename>.dcl. Except for comments,
  the first line in the text file must be:

```clean
definition module filename
```

## Examples
