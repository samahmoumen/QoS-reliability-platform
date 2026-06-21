import yaml


def load_service_config(path="config/service.yaml"):
    with open(path, "r") as f:
        data = yaml.safe_load(f)

    return data["service"]