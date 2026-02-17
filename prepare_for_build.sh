#!/bin/bash
# Script to prepare the build environment for Transformer Engine (metapackage).
#
# Example usage:
#   ./prepare_for_build.sh v2.11

set -euxo pipefail

export ROOT=`pwd`

if [ $# -ne 1 ]; then
    echo "Usage: $0 <transformer_engine_version>"
    echo "Example: $0 v2.11"
    exit 1
fi

TRANSFORMER_ENGINE_VERSION=$1

# The metapackage typically doesn't require patches, but we keep this structure
# for consistency and in case patches are needed in the future.
patch_dir="${ROOT}/build_scripts/patches/${TRANSFORMER_ENGINE_VERSION}"

if [ ! -d "${patch_dir}" ]; then
    echo "Info: No patches directory found for ${TRANSFORMER_ENGINE_VERSION}"
else
    for patch in "${patch_dir}"/*.patch; do
        # Skip if no patch files exist
        if [ -f "${patch}" ]; then
            patch -p1 -d "${ROOT}" -i "${patch}"
        fi
    done
fi
