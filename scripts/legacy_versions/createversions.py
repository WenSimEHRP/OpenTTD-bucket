import toml
import os

bucket = "bucket"
folders = [
    "openttd-jgrpp",
    "openttd",
]

# delete all toml files in the designated folder
for folder in folders:
    for file in os.listdir(f"{bucket}/{folder}"):
        if file.endswith(".toml"):
            os.remove(f"{bucket}/{folder}/{file}")

def create_tomls(name):

    def create_toml(template_path, type, version):
        with open(f"{template_path}-{type}.toml.template", "r") as f:
            with open(f"{template_path}-{version}.toml", "w") as f2:
                f2.write(f.read().replace("$VERSION", version))

    with open(f"scripts/legacy_versions/{name}-versions.toml", "r") as f:
        data = toml.load(f)
        versions = data["versions"] if "versions" in data else []
        nowin64 = data["nowin64"] if "nowin64" in data else []
        noarm64 = data["noarm64"] if "noarm64" in data else []
        diffname = data["diffname"] if "diffname" in data else []
        nobuild = data["nobuild"] if "nobuild" in data else []

    for index, version in enumerate(versions):
        base_path = f"{bucket}/{name}/{name}"
        if version in nowin64:
            create_toml(base_path, "nowin64", version)
        elif version in noarm64:
            create_toml(base_path, "noarm64", version)
        elif version in diffname:
            create_toml(base_path, "diffname", version)
        elif version not in nobuild:
            create_toml(base_path, "normal", version)
        else:
            continue

for folder in folders:
    create_tomls(folder)
