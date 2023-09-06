func (f MyFloat) Abs() float64 {
	if f < 0 {
		return float64(-f)
	}
	return float64(f)
}

/*
Gofmt formats Go programs.
It uses tabs for indentation and blanks for alignment.
Alignment assumes that an editor is using a fixed-width font.

Without an explicit path, it processes the standard input. Given a file,
it operates on that file; given a directory, it operates on all .go files in
that directory, recursively. (Files starting with a period are ignored.)
By default, gofmt prints the reformatted sources to standard output.

Usage:

gofmt [flags] [path ...]

The flags are:

-d
Do not print reformatted sources to standard output.
If a file's formatting is different than gofmt's, print diffs
to standard output.
. . .
*/
