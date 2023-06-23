import json
import os
import re


VERSION_RE = re.compile(r"""comfortable_panda-(\d+)\.(\d+)\.(\d+)(?:-fx)?.xpi""")


def gen_version(xpi_name) -> dict:
    m = VERSION_RE.match(xpi_name)
    if not m:
        raise ValueError(f"Invalid xpi name: {xpi_name}")

    version = f"{m.group(1)}.{m.group(2)}.{m.group(3)}"
    v1 = int(m.group(1))
    v2 = int(m.group(2))
    v3 = int(m.group(3))
    vs = (v1, v2, v3)

    if vs <= (3, 0, 0):
        update_link = f"https://das82.com/downloads/comfortable_panda-{version}-fx.xpi"
    elif vs <= (5, 0, 0):
        update_link = f"https://tinaxd.github.io/comfortable-panda-firefox-updates/comfortable_panda-{version}-fx.xpi"
    else:
        update_link = f"https://tinaxd.github.io/comfortable-panda-firefox-updates/comfortable_panda-{version}.xpi"

    return {"version": version, "update_link": update_link}


def main() -> None:
    files = os.listdir(".")
    xpis = []
    for file in files:
        if file.endswith(".xpi"):
            xpis.append(file)

    xpis.sort()

    j = {
        "addons": {
            "comfortable.panda@das08": {"updates": [gen_version(xpi) for xpi in xpis]}
        }
    }

    with open("updates.json", "w") as f:
        json.dump(j, f, indent=2)


if __name__ == "__main__":
    main()
