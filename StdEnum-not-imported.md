# StdEnum not imported (needed for [..] expressions)

Keywords: StdEnum not imported%

This error occurs when you use syntax constructs for enumeration types which
require the functions of `Enum` and `IncDec` classes defined in `_SystemEnum`.
For instance, `[0..]` requires `_from`.

## Solutions

- Add `import _SystemEnum` or `import StdEnum` to your program.

## Examples

```clean
Start = [0..]
```
