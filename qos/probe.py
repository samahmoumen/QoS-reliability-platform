import requests
import time
from qos.models import Observation


def probe_service(service: dict) -> Observation:
    url = service["url"]
    name = service["name"]
    timeout = service.get("timeout", 5)

    start = time.perf_counter()

    try:
        response = requests.get(url, timeout=timeout)
        latency = (time.perf_counter() - start) * 1000

        return Observation(
            service_name=name,
            url=url,
            status_code=response.status_code,
            latency_ms=round(latency, 2),
            is_up=response.ok
        )

    except requests.RequestException:
        return Observation(
            service_name=name,
            url=url,
            status_code=None,
            latency_ms=None,
            is_up=False
        )