import yaml

with open('x00_yaml_file.yaml', 'r') as stream:
    try:
        parsed_yaml=yaml.safe_load(stream)
        print(parsed_yaml)
    except yaml.YAMLError as exc:
        print(exc)