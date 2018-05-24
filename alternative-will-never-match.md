# alternative will never match

Keywords: %alternative will never match

This warning occurs when you have defined a function alternative that
is unreachable because its preceding alternatives (often due to identical
patterns or having a 'narrowed down' pattern following a more general one).

## Solutions

- Make sure that the more specific patterns of your function precede
  the more general patterns.

## Examples
```clean
module test
import StdEnv

:: Letter = A | B | C

instance toString Letter
   where toString A = "A"
         toString b = "B"  // accidently wrote b instead B, b is a pattern variable and matches anything
         toString C = "C"

Start = toString C
```

This yields:

```text
Warning [test.icl,7,toString]:   alternative will never match

```

The solution is to alter b to B in the second alternative of toString.
