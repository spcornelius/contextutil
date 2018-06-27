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


class ifelse(contextlib.AbstractContextManager):
    """ If-else, but for "with". Wrap one of two other
    context managers depending on whether a given condition
    is True or False. Works with or without "as" in either case.

    Parameters
    ----------
    condition : bool
        if True:
            Enter/return context1
        if False:
            Enter/return context2
    context1 : object or instance of contextlib.AbstractContextManager
        if instance of contextlib.AbstractContextManager:
            Will be entered if condition is True
        otherwise:
            Enter a null context with context1 as the return value
            if condition is True

    context2 : object or instance of contextlib.AbstractContextManager
        if instance of contextlib.AbstractContextManager:
            Will be entered if condition is False
        otherwise:
            Enter a null context with context2 as the return value
            if condition is False

    Examples
    --------
    # Perform I/O on a file (given by name) or an existing IOBase object,
    # closing afterward in the case of a file name

    with ifelse(isinstance(f, io.IOBase), f, open(f, "rw")) as fh:
        # Do some I/O
    """

    def __init__(self, condition, context1, context2):
        self.condition = condition
        self.context1 = as_context(context1)
        self.context2 = as_context(context2)

    def __enter__(self):
        if self.condition:
            return self.context1.__enter__()
        else:
            return self.context2.__enter__()

    def __exit__(self, *args):
        if self.condition:
            return self.context1.__exit__(*args)
        else:
            return self.context2.__exit__(*args)


class conditional(ifelse):

    def __init__(self, condition, context):
        ifelse.__init__(self, condition, context, nullcontext())