# Runtime error, rule '&#8230;' in module '&#8230;' does not match

Keywords: runtime error; rule does not match; rule % does not match; rule % in module % does not match

This happens when you evaluate the undefined part of a partial function.
In particular, this happens when you have a function of which the patterns are
non-exhaustive.

## Solutions

- Make the function total (implement all possible patterns).
- Make sure you call the function only with values for which it is defined.

## Examples

```clean
:: Letter = A | B | C

next :: Letter -> Letter
next A = B
next B = C

Start = next C
```

This yields:

```text
Run time error, rule 'next' in module 'test' does not match
```

The solution is to either implement `next` for `C` or not call it with `C`.
