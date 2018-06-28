v0.1.0, June 27 2018
======
Initial release

v0.1.1, June 27 2018
======
Added documentation to README.md

v0.2.0, June 27 2018
======
-Added conditional function
-Fleshed out README with additional example

v0.3.0, June 28 2018
======
-changed ``conditional`` to ``optional``. Syntax is non-backwards compatible
-Removed ``ifelse`` as largely superfluous. Most common use cases can be done with ``optional``
-Changed all managers to use contextlib decorators rather than inheritance from AbstractContextManager