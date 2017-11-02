# Heap full

Keywords: heap full

This happens when there is not enough space for the Clean program to create new
nodes in the rewrite graph.

## Solutions

- In some cases, you just need a little bit more heap.
  You can add heap space with `-h 10M` (for instance) on the command line or by
  changing the `HeapSize` setting in your project file. In the IDE you can
  enlarge the heap from the application settings.

- You can optimise the space usage of your program by removing space leaks.
  These are constructions where data cannot be garbage collected because some
  node still requires it. See the example below.

## Examples

```clean
Start = reverse (repeat 0)
```

This creates an infinitely large graph.

---

```clean
Start = reverse (repeatn 100000 0)
```

This does not work with the default 2MB heap, but does work with a 4MB heap.

---

```clean
Start = (length xs, hd xs)
where xs = [0..100000]
```

This is a space leak: the head of the list is still needed, so the entire list
cannot be garbage collected (since Clean lists are linked lists). But to
compute the length of the list, the whole list needs to be evaluated and
stored. To solve this problem, you can use:

```clean
import StdEnv, Data.Func, Data.Tuple
Start = swap (hyperstrict (hd xs, length xs))
where xs = [0..100000]
```

When the head and length are swapped, the list can be garbage-collected while
computing the length. The tuple is then swapped to give the same end result.
This needs to be done hyperstrict in this case, to avoid optimisations causing
the length to be evaluated first.

There is however no general best solution to space leaks.
