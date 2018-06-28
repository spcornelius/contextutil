import contextlib

__all__ = ['nullcontext', 'as_context', 'optional']


@contextlib.contextmanager
def nullcontext(return_on_enter=None):
    """ Context manager that does nothing.

    Parameters
    ----------
    return_on_enter : object
        Object to return with "as" clause
    """
    yield return_on_enter

@contextlib.contextmanager
def as_context(x):
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
    with (x if isinstance(x, contextlib.AbstractContextManager) else nullcontext(x)) as y:
        yield y

@contextlib.contextmanager
def optional(context, use_cm=True, default=None):
    """ Optionally invoke context manager depending on
        condition

    Parameters
    ----------
    context : instance of contextlib.AbstractContextManager
    use_cm : bool (True)
        if True:
            Enter user-supplied context as normal
        otherwise:
            Enter a nullcontext
    """
    with (context if use_cm else nullcontext(default)) as x:
        yield x
