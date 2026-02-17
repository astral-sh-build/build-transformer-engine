# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "packaging",
# ]
# ///

import json
import os

from packaging.version import Version

# The minimum Python version supported by TransformerEngine (as of v2.9).
MIN_PYTHON_VERSION = "3.10"

# TransformerEngine versions to build the metapackage for.
TRANSFORMER_ENGINE_VERSIONS = [
    "2.2.1",
    "2.3",
    "2.4",
    "2.5",
    "2.6",
    "2.7",
    "2.8",
    "2.9",
    "2.10",
    "2.11",
]

# Supported Python versions for each TransformerEngine version.
# Based on the minimum Python version in each release.
TRANSFORMER_ENGINE_PYTHON_SUPPORT = {
    "2.2": ["3.10", "3.11", "3.12"],
    "2.3": ["3.10", "3.11", "3.12"],
    "2.4": ["3.10", "3.11", "3.12"],
    "2.5": ["3.10", "3.11", "3.12"],
    "2.6": ["3.10", "3.11", "3.12"],
    "2.7": ["3.10", "3.11", "3.12", "3.13"],
    "2.8": ["3.10", "3.11", "3.12", "3.13"],
    "2.9": ["3.10", "3.11", "3.12", "3.13", "3.14"],
    "2.10": ["3.10", "3.11", "3.12", "3.13", "3.14"],
    "2.11": ["3.10", "3.11", "3.12", "3.13", "3.14"],
}

# Supported architectures.
SUPPORTED_ARCHITECTURES = ["x86_64", "aarch64"]

# Matrix exclusions.
EXCLUSIONS = [
    # No exclusions yet.
]


def main() -> None:
    # Every matrix member is a 3-tuple of:
    # `te-version`: the TransformerEngine version as "X.Y" or "X.Y.Z", e.g. "2.9"
    # `python-version`: the Python version as "3.X", e.g. "3.10"
    # `target-arch`: the target architecture, e.g. "x86_64" or "aarch64"

    rows = []
    for te_version in TRANSFORMER_ENGINE_VERSIONS:
        te_version_parsed = Version(te_version)
        te_x_y = f"{te_version_parsed.major}.{te_version_parsed.minor}"
        
        for python_version in TRANSFORMER_ENGINE_PYTHON_SUPPORT[te_x_y]:
            python_version_parsed = Version(python_version)
            if python_version_parsed < Version(MIN_PYTHON_VERSION):
                continue

            for target_arch in SUPPORTED_ARCHITECTURES:
                row = {
                    "target-arch": target_arch,
                    "te-version": te_version,
                    "python-version": python_version,
                }

                if row not in EXCLUSIONS:
                    rows.append(row)

    # Transform each row to add various nice-to-have representations of fields.
    for row in rows:
        # `CI_*` variables: same as the original ones.
        row["CI_TE_VERSION"] = row["te-version"]
        row["CI_PYTHON_VERSION"] = row["python-version"]

        # `MATRIX_TE_VERSION`: `te-version`, but only X.Y, no patch
        te_version = Version(row["te-version"])
        row["MATRIX_TE_VERSION"] = f"{te_version.major}.{te_version.minor}"

        # `MATRIX_PYTHON_VERSION`: same as `python-version`, but with the dot removed
        row["MATRIX_PYTHON_VERSION"] = row["python-version"].replace(".", "")

        # RUNNER: the GitHub Actions runner to use.
        if row["target-arch"] == "x86_64":
            row["RUNNER"] = "depot-ubuntu-24.04"
        elif row["target-arch"] == "aarch64":
            row["RUNNER"] = "depot-ubuntu-24.04-arm"
        else:
            raise ValueError(f"Unknown target arch: {row['target-arch']}")

    # For PR builds, limit matrix to a single entry for faster CI.
    if os.environ.get("LIMIT_MATRIX") == "1":
        rows = rows[:1]
    print(json.dumps(rows))


if __name__ == "__main__":
    main()
