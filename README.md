# contextutil
Tools for dealing with context managers

## Package Contents

`nullcontext(return_on_enter=None)`

Context manager that does nothing.

`as_context(x)`

Casts a given object as a context manager,
allowing it to be used in a `with` statement.

`ifelse(condition, context1, context2)`

Use one of two context managers depending on whether
`condition` is `True` or `False`.

## Example

The following function will divide two `numpy` vectors
elementwise, optionally ignoring any divide-by-zero 
warnings

    from contextutil import ifelse, nullcontext
    import numpy as np
    import warnings

    def divide(a, b, ignore=False):
        with ifelse(ignore, np.errstate(divide='ignore'), nullcontext()):
            c = a / b
        return c
        
## License
This software is distributed under the [GNU Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). 
        