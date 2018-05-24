# Common problems with Clean programs

This is a list of problems commonly encountered with Clean programs.
You can search in this list or search for errors and faults on [Cloogle][]
(coming soon).

Please contribute by adding more examples and errors.
Also if you don't know the solution yet, you can create a stub page.
See [below](#contributing) for contribution details.

## The list

### Compile-time errors

- [_SystemArray not imported](/_SystemArray-not-imported.md)
- [_SystemStrictLists not imported](/_SystemStrictLists-not-imported.md)
- [ambiguous selector specified](/record-disambiguation.md)
- [Can't find _SystemDynamic.icl](/_SystemDynamic.md)
- [could not determine the type of this record](/record-disambiguation.md)
- [dynamic used but support for dynamics not enabled](/no-dynamics.md)
- [function body expected](/function-body-expected.md)
- [Linker error, relocation &#8230; cannot be used when making a shared object](/relocation.md)
- [Run time error, rule &#8230; in module 'elf_relocations' does not match](/elf-relocations-does-not-match.md)
- [Start rule cannot be overloaded](/overloading-Start.md)
- [StdEnum not imported](/StdEnum-not-imported.md)
- [TC class undefined](/no-dynamics.md)
- [Unable to get short path name](/short-path-name.md)

### Compile-time warnings

- [alternative will never match](/_alternative_will_never_match.md)

### Run-time errors

- [Floating point exception](/floating-point-exception.md)
- [Heap full](/heap-full.md)
- [Run time error, rule '&#8230;' in module '&#8230;' does not match](/rule-does-not-match.md)
- [Stack overflow](/stack-overflow.md)

## Contributing

To add problems, examples, solutions or edit existing ones, fork this
repository, make your changes and create a pull request. Please make sure to
adhere to the below format. This ensures the files are correctly indexed by
[Cloogle][]. You can use the existing files for examples.

The list above contains links to markdown files in the repository.
Don't forget to update the list.
The list is sorted alphabetically.
We do not use directory structure.

The markdown files should look like:

```markdown
# <Some descriptive title (usually a general form of the error you encounter)>

Keywords: <keyword 1>; <keyword 2>; ...

<Some description>

## Solutions

- <solution 1>
- <solution 2>
- ...

## Examples

<example 1>

---

<example 2>

---

...
```

Be minimal in your use of Markdown. [Cloogle][] does not render Markdown fully.
It is capable of rendering `` `code` `` and multiline code blocks (see under
'Examples'), but don't use extra headings, italics, bold text, etc.

### Keywords

- Keywords are semicolon-separated.
- Don't add a final semicolon.
- Keywords are case-insensitive.
- To match any string, use `%` (e.g. [here](/rule-does-not-match.md)).
- To be found in [Cloogle][], the search query must match at least one of the
  keywords.

### Solutions

- Solutions are optional, but the `## Solutions` header is required.
- Continue solutions with a double space on the next line.

### Examples

- Examples are optional, but the `## Examples` header is required.
- Put code examples between `` ```clean `` and `` ``` ``.
- Put long monospaced text between `` ```text `` and `` ``` ``.

[Cloogle]: https://cloogle.org
