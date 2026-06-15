CREATE TABLE IF NOT EXISTS benchmark_runs (
    id SERIAL PRIMARY KEY,

    timestamp VARCHAR(50),

    workload VARCHAR(100),

    target VARCHAR(50),

    host VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS benchmark_metrics (
    id SERIAL PRIMARY KEY,

    run_id INTEGER REFERENCES benchmark_runs(id),

    metric_name VARCHAR(100),

    metric_value DOUBLE PRECISION
);