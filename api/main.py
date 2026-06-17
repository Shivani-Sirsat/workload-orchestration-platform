from fastapi import FastAPI

from api.routes import router


app = FastAPI(
    title="Workload Orchestration Platform",
    description=(
        "REST APIs for workload execution, "
        "benchmark history, KPI reporting, "
        "and workload comparison."
    ),
    version="1.0.0"
)

app.include_router(
    router
)