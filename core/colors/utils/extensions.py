from typing import Any
import enum


########################################################################
# ExtendedFlagEnum
########################################################################
class ExtendedFlagEnum(enum.Flag):  # pragma: nocover
    """
    Implements a sort of reflexivity into the ``__and__``, ``__or__``,
    and ``__xor__``,  operations of the enums.

    If Foo implements ``__and__(self, other: ExtendedFlagEnum)``, that allows for
    ``Foo & ExtendedFlagEnum -> ExtendedFlagEnum`` -- but
    ``ExtendedFlagEnum & Foo -> ExtendedFlagEnum`` would raise an error.
    This automatically handles ``ExtendedFlagEnum & Foo`` by reversing the arguments.
    If Foo doesn't handle the operation involving ExtendedFlagEnum, it's errors will be raised.
    """
    # region Bit-Wise Functions
    # NOTE: For bit-wise operations, if the `other` being compared to is another type,
    #  the `other`'s bitwise logic will be leveraged to handle the operation.
    #  If it doesn't exist, or doesn't support the operation, its error will be raised.
    def __and__(self, other: Any):
        _type = type(self)
        if isinstance(other, _type):
            return _type(self.value & other.value)
        else:
            return other & self

    def __or__(self, other: Any):
        _type = type(self)
        if isinstance(other, _type):
            return _type(self.value | other.value)
        else:
            return other | self

    def __xor__(self, other: Any):
        _type = type(self)
        if isinstance(other, _type):
            return _type(self.value ^ other.value)
        else:
            return other ^ self
    # endregion Bit-Wise Functions
