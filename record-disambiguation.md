# Could not determine the type of this record; ambiguous selector specified

Keywords: could not determine the type of this record; %ambiguous selector specified

These errors occur when there is a record expression of which the field names
are ambiguous. Field names need not be unique, so there can be record
expressions that, based on the fields, can be of different types. In this case,
the type needs to be made explicit.

## Solutions

- If the type of the record cannot be determined, make the type explicit by
  adding the name to the record expression. For example,
  `{Time | hour=10, min=30, sec=0}` or `{DateTime | dt & min=0}`.
- If the selector is ambiguous, add the type name to the selector. For example,
  `rec.TypeName.field` instead of `rec.field`.

## Examples

```clean
:: R1 = {x :: Int}
:: R2 = {x :: Int, y :: Int}
Start = {x=5}
```

The set of fields of the unique is not unique to any record type, so the type
cannot be determined. The solution is to use `{R1 | x=5}`.

---

```clean
:: R1 = {x :: Int}
:: R2 = {x :: Int, y :: Int}
Start = {x=5,y=10}.x
```

Here, the type of the record can be determined as `R2` because of the `y`
field. However, the `x` selector may belong to both `R1` and `R2`. Hence, we
need to disambiguate it with `{x=5,y=10}.R2.x`.
