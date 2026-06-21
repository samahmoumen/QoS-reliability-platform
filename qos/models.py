from dataclasses import dataclass


@dataclass
class Observation:
    service_name: str
    url: str
    status_code: int | None
    latency_ms: float | None
    is_up: bool