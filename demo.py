import yaml


with open("date.yaml", "r") as f:
    print(yaml.load(f, Loader=yaml.FullLoader))
