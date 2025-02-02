# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from connector_builder.generated.models.log_message import LogMessage
from connector_builder.generated.models.stream_read_slices_inner import StreamReadSlicesInner


class StreamRead(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    StreamRead - a model defined in OpenAPI

        logs: The logs of this StreamRead.
        slices: The slices of this StreamRead.
        test_read_limit_reached: The test_read_limit_reached of this StreamRead.
        inferred_schema: The inferred_schema of this StreamRead [Optional].
    """

    logs: List[LogMessage] = Field(alias="logs")
    slices: List[StreamReadSlicesInner] = Field(alias="slices")
    test_read_limit_reached: bool = Field(alias="test_read_limit_reached")
    inferred_schema: Optional[Dict[str, Any]] = Field(alias="inferred_schema", default=None)

StreamRead.update_forward_refs()
