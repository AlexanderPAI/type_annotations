"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
"""
from typing import Callable, TypeVar

sign = TypeVar("sign", bound=Callable)


def decorator(func: sign) -> sign:
    return func
