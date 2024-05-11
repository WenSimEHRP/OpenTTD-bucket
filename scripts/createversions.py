import json


jgrpp_versions = []
with open("scripts/jgrpp_versions.json", "r") as f:
    jgrpp_versions = json.load(f)["jgrpp_versions"]


def create_json(base_path, version):
    with open(f"{base_path}.json.template", "r") as f:
        with open(f"{base_path}-{version}.json", "w") as f2:
            f2.write(f.read().replace("$VERSION", version))

for version in jgrpp_versions:
    create_json("bucket/jgrpp/openttd-jgrpp", version)
