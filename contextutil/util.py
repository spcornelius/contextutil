import contextlib

__all__ = ['ifelse', 'nullcontext', 'as_context', 'conditional']


class nullcontext(contextlib.AbstractContextManager):
    """ Context manager that does nothing.

    Parameters
    ----------
    return_on_enter : object
        Object to return with "as" clause
    """
    def __init__(self, return_on_enter=None):
        self.return_on_enter = return_on_enter

    def __enter__(self):
        return self.return_on_enter

    def __exit__(self, *excinfo):
        pass


class as_context(contextlib.AbstractContextManager):
    """ Wrap a given object as a context manager (if it
    is not one already), allowing it to be used in a
    with statement.

    Parameters
    ----------
    x : object or instance of contextlib.AbstractContextManager
        if instance of contextlib.AbstractContextManager:
            Return this context manager
        otherwise:
            Return a nullcontext wrapping x
    """
    def __init__(self, x):
        if isinstance(x, contextlib.AbstractContextManager):
            self._x = x
        else:
            self._x = nullcontext(x)

    def __enter__(self):
        return self._x.__enter__()

    def __exit__(self, *excinfo):
        return self._x.__exit__(self, *excinfo)


@contextlib.contextmanager
def optional(self, context, use_cm=False, default=None):
    """ Optionally invoke context manager depending on
        condition

    Parameters
    ----------
    context : instance of contextlib.AbstractContextManager
    use_cm : bool (False)
        if True:
            Enter user-supplied context as normal
        otherwise:
            Enter a nullcontext
    default : object
        If use_cm is False, default will be yielded by the null
        context manager
    """
    with (context if use_cm else nullcontext()):
        yield
