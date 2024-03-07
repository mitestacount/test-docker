import time
from functools import lru_cache
from typing import Annotated, Optional

import pandas as pd
from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel, Field, field_validator

from src.entity.entity_request import MultipleQueryParams, relative_where_query
from src.tests.time import Person

app = FastAPI()

person = Person()
new_pandas = pd.DataFrame
print(person.name, new_pandas)


@lru_cache
def loop_with_delay(repeats: int, delay: int) -> str:
    # loop through each item in the list
    for item in range(repeats):
        time.sleep(delay)
    return f"Done! {repeats=}, {delay=}"


@app.get("/exec/{num}")
async def read_root(num: int = 1):
    start_time = time.time()
    message = loop_with_delay(2, num)
    end_time = time.time()
    execution_time = end_time - start_time
    return {
        "message": f"Execution {message=}",
        "execution_time": f"{round(execution_time*1000)} ms",
    }


@app.get("/clear-cache")
async def clear_cache():
    loop_with_delay.cache_clear()
    return {"message": "Cache cleared!"}


# route of multiple query params
@app.get("/multiple-query-params")
async def multiple_query_params(
    query_params: MultipleQueryParams = Depends(),
):
    print(f"Query: params {query_params=}")
    print(query_params.model_dump(exclude_none=True))
    return query_params.model_dump(exclude_none=True)
