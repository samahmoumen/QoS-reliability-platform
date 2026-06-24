from dataclasses import dataclass

from qos.metrics import percentile


@dataclass
class SLI:
    availability: float
    avg_latency: float
    p50_latency: float
    p95_latency: float
    p99_latency: float
    error_rate: float


def calculate_sli(records):

    total = len(records)

    if total == 0:
        return SLI(
            availability=0,
            avg_latency=0,
            p50_latency=0,
            p95_latency=0,
            p99_latency=0,
            error_rate=0
        )

    successes = sum(
        1
        for success, _ in records
        if success == 1
    )

    failures = total - successes

    availability = (successes / total) * 100

    error_rate = (failures / total) * 100

    latencies = [
        latency
        for _, latency in records
        if latency is not None
    ]

    avg_latency = (
        sum(latencies) / len(latencies)
        if latencies
        else 0
    )

    return SLI(
        availability=round(availability, 2),

        avg_latency=round(avg_latency, 2),

        p50_latency=round(percentile(latencies, 50), 2),

        p95_latency=round(percentile(latencies, 95), 2),

        p99_latency=round(percentile(latencies, 99), 2),

        error_rate=round(error_rate, 2)
    )