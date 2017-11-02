# Common problems with Clean programs

This is a list of problems commonly encountered with Clean programs.
You can search in this list or search for errors and faults on [Cloogle][]
(coming soon).

Please contribute by adding more examples and errors.
Also if you don't know the solution yet, you can create a stub page.
See [below](#contributing) for contribution details.

## The list

### Compile-time errors

- None yet ([contribute!](#contributing))

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
- Keywords are case-insensitive.
- To match any string, use `%` (e.g. [here](/rule-does-not-match.md)).
- To be found in [Cloogle][], the search query must match at least one of the
  keywords.

### Solutions

- Continue solutions with a double space on the next line.

### Examples

- Put code examples between `` ```clean `` and `` ``` ``.
- Put long monospaced text between `` ```text `` and `` ``` ``.

[Cloogle]: https://cloogle.org
