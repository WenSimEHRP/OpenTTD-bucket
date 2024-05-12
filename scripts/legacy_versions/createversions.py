import json
import os

bucket = "bucket"
folders = [
    "openttd-jgrpp",
    "openttd",
]


# delete all json files in the desiginated folder
for folder in folders:
    for file in os.listdir(f"{bucket}/{folder}"):
        if file.endswith(".json"):
            os.remove(f"{bucket}/{folder}/{file}")


def create_jsons(name):

    def create_json(template_path, type, version):
        with open(f"{template_path}-{type}.json.template", "r") as f:
            with open(f"{template_path}-{version}.json", "w") as f2:
                f2.write(f.read().replace("$VERSION", version))

    with open(f"scripts/legacy_versions/{name}-versions.json", "r") as f:
        data = json.load(f)
        versions = data["versions"] if "versions" in data else []
        nowin64 = data["nowin64"] if "nowin64" in data else []
        noarm64 = data["noarm64"] if "noarm64" in data else []
        diffname = data["diffname"] if "diffname" in data else []
        nobuild = data["nobuild"] if "nobuild" in data else []

    for index, version in enumerate(versions):
        base_path = f"{bucket}/{name}/{name}"
        if version in nowin64:
            create_json(base_path, "nowin64", version)
        elif version in noarm64:
            create_json(base_path, "noarm64", version)
        elif version in diffname:
            create_json(base_path, "diffname", version)
        elif version not in nobuild:
            create_json(base_path, "normal", version)
        else:
            continue


for folder in folders:
    create_jsons(folder)
