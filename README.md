# contextutil
Tools for dealing with context managers

## Package Contents

`nullcontext(return_on_enter=None)`

Context manager that does nothing.

`as_context(x)`

Casts a given object as a context manager,
allowing it to be used in a `with` statement.

`optional(context, use_cm=False, default=True)`

Enter context manager optionally according to supplied flag,
otherwise enter a `nullcontext` yielding `default`.

## Examples

The following function will divide two `numpy` vectors
elementwise, optionally ignoring any divide-by-zero 
warnings

    from contextutil import ifelse, nullcontext, conditional
    import numpy as np
    import warnings

    def divide(a, b, ignore=False):
        with optional(np.errstate(divide='ignore'), use_cm=ignore):
            c = a / b
        return c
   
        
## License
This software is distributed under the [GNU Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). 
        