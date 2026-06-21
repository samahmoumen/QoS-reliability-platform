import typer

from qos.config import load_service_config
from qos.probe import probe_service
from qos.renderer import render


app = typer.Typer()


@app.command()
def monitor():
    """
    Run a single QoS probe on configured service
    """

    service = load_service_config()

    observation = probe_service(service)

    render(observation)

@app.command()
def placeholder():
    """Future command placeholder"""
    pass

if __name__ == "__main__":
    app()