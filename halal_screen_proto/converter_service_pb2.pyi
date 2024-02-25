from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConvertContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMAGE: _ClassVar[ConvertContentType]
    VIDEO: _ClassVar[ConvertContentType]
IMAGE: ConvertContentType
VIDEO: ConvertContentType

class ConvertRequest(_message.Message):
    __slots__ = ("content", "type", "blur_percentage")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BLUR_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    type: ConvertContentType
    blur_percentage: int
    def __init__(self, content: _Optional[bytes] = ..., type: _Optional[_Union[ConvertContentType, str]] = ..., blur_percentage: _Optional[int] = ...) -> None: ...

class ConvertResponse(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    def __init__(self, content: _Optional[bytes] = ...) -> None: ...
