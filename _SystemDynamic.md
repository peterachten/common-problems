# Can't find _SystemDynamic.icl

Keywords: can't find _SystemDynamic.icl; _SystemDynamic%

There is a problem in the build tools that make that dependencies to the
dynamics system are stored in the intermediate ABC files. Because of this,
after compiling a program that uses dynamics, any other program you try to
compile will require `_SystemDynamic.icl` as well, even when it does not use
dynamics itself.

## Solutions

- Remove all ABC files except `_system.abc` (in `StdEnv`) to force
  recompilation of these files.
- Get a fresh Clean installation.

## Examples
