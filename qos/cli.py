import typer

from qos.config import load_service_config
from qos.probe import probe_service
from qos.renderer import render
from qos.reliability import ReliabilityAnalyzer


app = typer.Typer()


from qos.storage import MetricsRepository


repository = MetricsRepository()


@app.command()

def monitor():

    service = load_service_config()


    observation = probe_service(service)


    repository.save(observation)


    render(observation)



@app.command()

def slo(service_name: str):


    repository = MetricsRepository()


    records = repository.get_all(service_name)


    analyzer = ReliabilityAnalyzer()


    result = analyzer.analyze(records)


    sli = result["sli"]


    evaluation = result["evaluation"]


    print()

    print("SERVICE:", service_name)

    print()

    print("Availability:", sli.availability)

    print("Average Latency:", sli.avg_latency)

    print("P95:", sli.p95_latency)

    print("Error Rate:", sli.error_rate)

    print()

    print("STATUS:", evaluation["status"])

@app.command()
def placeholder():
    """Future command placeholder"""
    pass

if __name__ == "__main__":
    app()