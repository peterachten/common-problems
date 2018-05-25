# function body expected

Keywords: %function body expected

This error occurs when the type signature of a function is not followed by a definition of the
function with exactly the same name (often due to a missing character, difference in upper- or
lower-case).

## Solutions

- Make sure that the function name of the function definition following the type signature are
  exactly identical.

## Examples

```clean
my_function :: Int -> Int
my_Function x = x
```
Here, the implementation of `my_function` has a capital `F`, which the Clean
compiler interprets as a new (untyped) function.
