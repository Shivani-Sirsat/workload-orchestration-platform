from database.connection import (
    get_connection
)


def save_run(
    timestamp,
    workload,
    target,
    host
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO benchmark_runs
        (
            timestamp,
            workload,
            target,
            host
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s
        )
        RETURNING id
        """,
        (
            timestamp,
            workload,
            target,
            host
        )
    )

    run_id = cursor.fetchone()[0]

    conn.commit()

    cursor.close()
    conn.close()

    return run_id


def save_metric(
    run_id,
    metric_name,
    metric_value
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO benchmark_metrics
        (
            run_id,
            metric_name,
            metric_value
        )
        VALUES
        (
            %s,
            %s,
            %s
        )
        """,
        (
            run_id,
            metric_name,
            metric_value
        )
    )

    conn.commit()

    cursor.close()
    conn.close()


def get_runs(
    workload_name
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            timestamp,
            workload,
            target,
            host
        FROM benchmark_runs
        WHERE workload = %s
        ORDER BY id
        """,
        (
            workload_name,
        )
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def get_metrics(
    run_id
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            metric_name,
            metric_value
        FROM benchmark_metrics
        WHERE run_id = %s
        ORDER BY id
        """,
        (
            run_id,
        )
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def get_recent_runs(
    workload_name
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            timestamp
        FROM benchmark_runs
        WHERE workload = %s
        ORDER BY id DESC
        LIMIT 2
        """,
        (
            workload_name,
        )
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows