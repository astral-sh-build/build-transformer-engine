# build-transformer-engine

This repository contains build scripts and CI configuration for building the [NVIDIA TransformerEngine](https://github.com/NVIDIA/TransformerEngine) **metapackage** wheels.

The metapackage is a pure Python package that depends on backend-specific packages (like `transformer-engine-torch`, `transformer-engine-jax`, etc.) and provides a unified interface.

## Related Repositories

- [build-transformer-engine-torch](https://github.com/astral-sh-build/build-transformer-engine-torch) - Builds the PyTorch backend for TransformerEngine

## Structure

- `prepare_for_build.sh` - Prepares the build environment (applies any necessary patches)
- `embed_patches.py` - Embeds SBOM and patch information into built wheels
- `.github/workflows/` - CI configuration for automated builds

## Building

The builds are orchestrated through GitHub Actions. The workflow:

1. Checks out the specified version of TransformerEngine from NVIDIA's repository
2. Builds one `py3-none-any` metapackage wheel for the release version
3. Embeds SBOM information into the wheel
4. Uploads the wheel as an artifact (for PRs) or to the release (for release builds)

## Supported Versions

The metapackage is pure Python: each TransformerEngine release needs one wheel,
which can be shared by every supported Python version, architecture, and CUDA
index. Version-specific patches are maintained under `patches/`.

## License

Apache License 2.0 - See [LICENSE](LICENSE) for details.
