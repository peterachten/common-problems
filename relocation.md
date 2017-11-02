# Linker error, relocation '&#8230;' against \`.data' can not be used when making a shared object

Keywords: linker error; relocation; Nonrepresentable section on output;

Using some newer versions of gcc cause the linking of the Clean program to
return an error.

## Solutions

- Pass `-l -no-pie` to `clm`
- Ensure that `cpm` calls the linker (`ld`) with the `-no-pie` flag enabled

## Examples

```clean
module hello_world

Start = "Hello, World!"
```

And compiling with:
```text
clm hello_world
```

Returns the following error:
```text
/usr/bin/ld: /tmp/linkerXXXXXX: relocation R_X86_64_32S against `.data' can not be used when making a shared object; recompile with -fPIC
/usr/bin/ld: final link failed: Nonrepresentable section on output
collect2: error: ld returned 1 exit status
```

Compiling with:
```text
clm -l -no-pie hello_world
```
Compiles fine.
