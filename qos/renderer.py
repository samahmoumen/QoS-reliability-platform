from rich.table import Table
from rich.console import Console


console = Console()


def render(observation):

    table = Table(title="QoS Guardian - Observability Probe")

    table.add_column("Metric")
    table.add_column("Value")

    table.add_row("Service", observation.service_name)
    table.add_row("URL", observation.url)

    status = "UP 🟢" if observation.is_up else "DOWN 🔴"
    table.add_row("Status", status)

    table.add_row("HTTP Code", str(observation.status_code))
    table.add_row("Latency (ms)", str(observation.latency_ms))

    console.print(table)