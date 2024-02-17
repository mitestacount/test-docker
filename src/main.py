import time
from functools import lru_cache
from typing import Optional, Annotated


from fastapi import FastAPI, Depends, Query
from pydantic import BaseModel, Field

app = FastAPI()


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


class MultipleQueryParams(BaseModel):
    repeats: str = Field(
        Query(
            description="Delay in seconds between each loop",
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


# route of multiple query params
@app.get("/multiple-query-params")
async def multiple_query_params(query_params: MultipleQueryParams = Depends()):

    print(f"Query: params {query_params=}")
    print(query_params.model_dump(exclude_none=True))
    return query_params.model_dump(exclude_none=True)


# route of multiple query params


@app.get("/items/")
async def read_items(
    required_param: str = Query(..., description="This is a required parameter"),
    optional_param: Optional[str] = Query(
        None, description="This is an optional parameter"
    ),
) -> dict[str, str]:
    return {"required_param": required_param, "optional_param": optional_param}
