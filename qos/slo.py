from dataclasses import dataclass


@dataclass
class SLO:

    availability_target: float = 99.9

    latency_target: float = 300

    error_budget: float = 0.1


def evaluate_slo(sli, slo):

    availability_ok = (
        sli.availability >= slo.availability_target
    )

    latency_ok = (
        sli.p95_latency <= slo.latency_target
    )

    return {

        "availability_ok": availability_ok,

        "latency_ok": latency_ok,

        "status": (
            "PASS"
            if availability_ok and latency_ok
            else "FAIL"
        )
    }