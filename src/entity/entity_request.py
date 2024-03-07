import time
from functools import lru_cache
from pathlib import Path
from typing import Annotated, Optional

import pandas as pd
import requests
from fastapi import Depends, FastAPI, Query, Response
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, Field, field_validator


def relative_where_query(data: any):
    if not data:
        raise HTTPException(
            status_code=409,
            detail=f"Absolute paths are not allowed, {data} is absolute.",
        )

    return data


class MultipleQueryParams(BaseModel):
    repeats: str = Field(
        Query(
            description="Delay in seconds between each loosp",
            example="sas",
            min_length=1,
            format="aa",
        ),
    )
    delay: Annotated[
        int | None,
        Field(
            Query(
                default=None,
                description="Delay in seconds between each loop",
                example=2,
                type="integer",
            ),
        ),
    ]
    delay2: Optional[int] = Field(
        Query(
            default=None,
            description="Delay in seconds between each loop",
            example=2,
            type="integer",
        ),
        type="integer",
    )
    delay3: int | None = Field(
        Query(
            default=None,
            description="Delay in seconds between each loop",
            example=2,
            type="integer",
            format="int32",
        ),
    )

    @field_validator("repeats")
    def check_repeats(cls, v):
        print(f"Se está validando {v=} y todo ok")
        if "a" in v:
            raise HTTPException(
                status_code=420,
                detail=f"Is in in {v=}",
            )

        return v + "========"
