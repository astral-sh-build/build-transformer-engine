# build-transformer-engine

This repository contains build scripts and CI configuration for building the [NVIDIA TransformerEngine](https://github.com/NVIDIA/TransformerEngine) **metapackage** wheels.

The metapackage is a pure Python package that depends on backend-specific packages (like `transformer-engine-torch`, `transformer-engine-jax`, etc.) and provides a unified interface.

## Related Repositories

- [build-transformer-engine-torch](https://github.com/astral-sh-build/build-transformer-engine-torch) - Builds the PyTorch backend for TransformerEngine

## Structure

- `plan-matrix.py` - Generates the build matrix for different Python versions and architectures
- `prepare_for_build.sh` - Prepares the build environment (applies any necessary patches)
- `embed_patches.py` - Embeds SBOM and patch information into built wheels
- `.github/workflows/` - CI configuration for automated builds

## Building

The builds are orchestrated through GitHub Actions. The workflow:

1. Checks out the specified version of TransformerEngine from NVIDIA's repository
2. Builds the metapackage wheel for various Python versions and architectures
3. Embeds SBOM information into the wheel
4. Uploads the wheel as an artifact (for PRs) or to the release (for release builds)

## Supported Versions

See [plan-matrix.py](plan-matrix.py) for the list of supported TransformerEngine versions, Python versions, and architectures.

## License

Apache License 2.0 - See [LICENSE](LICENSE) for details.
