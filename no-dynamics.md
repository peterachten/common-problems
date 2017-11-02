# Support for dynamics not enabled

Keywords: %support for dynamics%; TC class; TC class undefined

Two errors, `dynamic used but support for dynamics not enabled` and `TC class
undefined` arise when you compile a program that uses dynamics without enabling
support for dynamics in the compiler.

## Solutions

- Add `-dynamics` to the `clm` arguments.
- Set `Application/Profile/Dynamics` to true in your `cpm` project file.
- Enable dynamic support in the application settings in the IDE.

## Examples

```clean
Start = dynamic 37
```

The `dynamic` builtin is only supported when support for dynamics is enabled.

---

```clean
Start = f 5
where
	f :: a -> a | TC a
	f x = x
```

`TC` is a builtin class that is only defined when dynamics support is enabled.
