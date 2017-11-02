# Stack overflow

Keywords: stack overflow

This can happen when there is some infinite recursion in your program and the
stack becomes too large.

## Solutions

- If there is an infinite recursion, you need to change the program to remove
  it.

- Otherwise, it may be that you just need a little bit more stack.
  You can add stack with `-s 2M` (for instance) on the command line or by
  changing the `StackSize` setting in your project file. In the IDE you can
  enlarge the stack from the application settings.

## Examples

```clean
import StdEnv
Start = foldr (+) 0 (repeat 0)
```

This is an endless recursion, since `repeat` generates an infinite list.
