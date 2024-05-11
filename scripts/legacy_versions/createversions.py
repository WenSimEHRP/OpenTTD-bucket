import json


jgrpp_versions = []
jgrpp_noarm64_versions = []
jgrpp_diffname_versions = []
jgrpp_nobuild_versions = []
with open("scripts/jgrpp_versions.json", "r") as f:
    data = json.load(f)
    jgrpp_versions = data["jgrpp_versions"]
    jgrpp_noarm64_versions = data["noarm64"]
    jgrpp_diffname_versions = data["diffname"]
    jgrpp_nobuild_versions = data["nobuild"]


def create_json(base_path, version):
    with open(f"{base_path}.json.template", "r") as f:
        with open(f"bucket/jgrpp/openttd-jgrpp-{version}.json", "w") as f2:
            f2.write(f.read().replace("$VERSION", version))

for version in jgrpp_versions:
    if version in jgrpp_noarm64_versions:
        create_json("bucket/jgrpp/openttd-jgrpp-noarm64", version)
    elif version in jgrpp_diffname_versions:
        create_json("bucket/jgrpp/openttd-jgrpp-diffname", version)
    elif version in jgrpp_nobuild_versions:
        pass
    else:
        create_json("bucket/jgrpp/openttd-jgrpp", version)
