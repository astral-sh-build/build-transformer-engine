# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import json
import os

# TransformerEngine versions to build the metapackage for.
# Since the metapackage is pure Python, we only need one build per version.
TRANSFORMER_ENGINE_VERSIONS = [
    "2.4",
    "2.5",
    "2.6",
    "2.7",
    "2.8",
    "2.9",
    "2.10",
    "2.11",
]

# Matrix exclusions.
EXCLUSIONS = [
    # No exclusions yet.
]


def main() -> None:
    # For a pure Python metapackage, we only need one build per TransformerEngine version.
    # The wheel is platform-independent (pure Python).
    
    rows = []
    for te_version in TRANSFORMER_ENGINE_VERSIONS:
        row = {
            "te-version": te_version,
        }
        
        if row not in EXCLUSIONS:
            rows.append(row)

    # Transform each row to add helpful representations.
    for row in rows:
        # `CI_TE_VERSION`: same as te-version
        row["CI_TE_VERSION"] = row["te-version"]
        
        # `MATRIX_TE_VERSION`: same as te-version
        row["MATRIX_TE_VERSION"] = row["te-version"]
        
        # RUNNER: use a standard Linux runner (pure Python build)
        row["RUNNER"] = "ubuntu-latest"

    # For PR builds, limit matrix to a single entry for faster CI.
    if os.environ.get("LIMIT_MATRIX") == "1":
        rows = rows[:1]
    print(json.dumps(rows))


if __name__ == "__main__":
    main()
