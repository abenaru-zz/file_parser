class NameLengthError(NameError):
    def __init__(self, *args):
        super(NameLengthError, self).__init__(*args)


class InvalidTypeError(ValueError):
    def __init__(self, *args):
        super(InvalidTypeError, self).__init__(*args)


class ObjectNotFoundError(IndexError):
    def __init__(self, *args):
        super(ObjectNotFoundError, self).__init__(*args)