# _SystemArray not imported (needed for array denotations)

Keywords: _SystemArray; _SystemArray not imported; needed for array denotations

This error occurs when you use syntax constructs for arrays which require the
functions of the `Array` class defined in `_SystemArray`. For instance,
`"string".[0]` requires `select`.

## Solutions

- Add `import _SystemArray` or `import StdArray` to your program.

## Examples

```clean
Start = {37}
```

Gives the error: `_SystemArray not imported (needed for array denotations)`

---

```clean
Start = "string".[0]
```

Gives the error: `_SystemArray not imported`.
