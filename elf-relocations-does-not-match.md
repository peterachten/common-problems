# Run time error, rule &#8230; in module 'elf_relocations' does not match

Keywords: run time error, rule %elf_relocations% does not match; elf_relocations

This is a run time error of the Clean linker, so it is a compile time error
when you try to compile a Clean program.
It is not exactly clear when this error occurs, but Clean programs linking with
C are more sensitive to it (and may be the only programs affected).

## Solutions

- A workaround is to not use the Clean linker, i.e. add `-no-opt-link` to the
  `clm` arguments.

## Examples

N/A
