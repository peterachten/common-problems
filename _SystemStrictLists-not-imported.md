# _SystemStrictLists not imported (needed for strict lists)

Keywords: _SystemStrictLists not imported%

This error occurs when you use syntax constructs for lists which require the
functions of the `List`, `UList` and `UTSList` classes defined in
`_SystemStrictLists`. For instance, `[#37]` requires `_cons` and `_nil`.

## Solutions

- Add `import _SystemStrictLists` to your program.

## Examples

```clean
Start = [#37]
```
