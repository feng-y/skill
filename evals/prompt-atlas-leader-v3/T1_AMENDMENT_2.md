# T1 type-boundary amendment, frozen before paired rerun a2

The a1 task removed the overlapping numeric ranges but still used the phrase
“non-numeric input.” Method audit found two plausible interpretations:

- values that cannot be converted to a number;
- values whose runtime type is not a supported numeric type.

The a2 paired rerun freezes the latter:

- accept only `int` and `float`;
- reject `bool` despite Python's `bool` subclassing `int`;
- reject all strings, including numeric-looking strings such as `"20"`;
- reject non-finite floats.

The range, protected files, skill versions, fixture, and all other protocol
conditions remain unchanged. The a1 result is excluded from the final T1
comparison.
