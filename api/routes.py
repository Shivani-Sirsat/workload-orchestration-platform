from fastapi import (
    APIRouter,
    HTTPException
)

from api.schemas import (
    HealthResponse,
    WorkloadsResponse,
    HistoryResponse,
    CompareResponse
)

from cli.workload_registry import (
    get_workloads
)

from execution.history_reader_db import (
    load_history
)

from execution.compare_reader_db import (
    load_compare_data
)

from execution.report_reader_db import (
    generate_report
)

router = APIRouter(
    prefix="/api/v1",
    tags=["Workload Platform"]
)


@router.get("/")
def root():

    return {
        "status": "running",
        "service": "Workload Orchestration Platform API"
    }


@router.get("/workloads")
def workloads():

    return {
        "workloads": get_workloads()
    }


@router.get(
    "/history/{workload_name}",
    response_model=list[
        HistoryResponse
    ]
)
def history(
    workload_name: str
):

    data = load_history(
        workload_name
    )

    if not data:

        raise HTTPException(
            status_code=404,
            detail=f"{workload_name} not found"
        )

    return data


@router.get(
    "/compare/{workload_name}",
    response_model=CompareResponse
)
def compare(
    workload_name: str
):

    previous, latest = (
        load_compare_data(
            workload_name
        )
    )

    if not latest:

        raise HTTPException(
            status_code=404,
            detail=f"{workload_name} not found"
        )

    return {
        "previous": previous,
        "latest": latest
    }


@router.get(
    "/report/{workload_name}"
)
def report(
    workload_name: str
):

    data = generate_report(
        workload_name
    )

    if not data:

        raise HTTPException(
            status_code=404,
            detail=f"{workload_name} not found"
        )

    return data


@router.get(
    "/health",
    response_model=HealthResponse
)
def health():

    return {
        "status": "healthy"
    }