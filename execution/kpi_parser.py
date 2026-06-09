import re


def parse_redis_kpi(output):

    kpis = {}

    patterns = {
        "get_rps": r"GET:\s+([\d\.]+)\s+requests per second",
        "set_rps": r"SET:\s+([\d\.]+)\s+requests per second",
        "incr_rps": r"INCR:\s+([\d\.]+)\s+requests per second",
        "hset_rps": r"HSET:\s+([\d\.]+)\s+requests per second",
    }

    for key, pattern in patterns.items():

        match = re.search(pattern, output)

        if match:

            kpis[key] = float(
                match.group(1)
            )

    return kpis