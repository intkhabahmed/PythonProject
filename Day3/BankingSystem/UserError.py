class AccountNumberNotFoundError(RuntimeError):
    pass


class InsufficientBalanceError(RuntimeError):
    pass


class UserNameError(RuntimeError):
    pass


class UserEmailError(RuntimeError):
    pass


class AmountError(RuntimeError):
    pass
