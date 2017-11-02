# Start rule cannot be overloaded

Keywords: Start rule cannot be overloaded

This errors occurs when a program uses overloaded functions in the `Start` rule
to the extent that its type cannot be derived.

## Solutions

- Explicitly specify the type of `Start`.

## Examples

```clean
Start = zero
```

Here, it is unclear which instance of `zero` is meant (for `Int`, `Real`,
etc.). Explicitly specifying the type (e.g. `Start :: Int`) resolves the issue.
