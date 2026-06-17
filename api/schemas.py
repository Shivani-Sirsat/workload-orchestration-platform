from pydantic import BaseModel

from typing import Any


class HealthResponse(
    BaseModel
):

    status: str


class WorkloadsResponse(
    BaseModel
):

    workloads: list[str]


class HistoryResponse(
    BaseModel
):

    run: str

    kpis: dict[
        str,
        Any
    ]


class CompareResponse(
    BaseModel
):

    previous: dict[
        str,
        Any
    ]

    latest: dict[
        str,
        Any
    ]