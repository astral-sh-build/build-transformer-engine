# build-transformer-engine

Pre-built pure Python wheels for the metapackage from
[NVIDIA Transformer Engine](https://github.com/NVIDIA/TransformerEngine), across
Python, CUDA, and CPU architectures.

## Installation

Following the PyTorch convention, artifacts are published to a separate index
for each CUDA version. Unlike the PyTorch extension, the Transformer Engine
metapackage is independent of CUDA, PyTorch, and CPU architecture: the same
`transformer_engine-2.16.0-py3-none-any.whl` is published to each compatible
CUDA index.

Once released, pre-built wheels will be available on
[Astral's GPU indexes](https://wheels.astral.sh/index.html).
For example, to install the PyTorch extension from the CUDA 12.8 index:

```console
$ uv add 'transformer-engine[pytorch]' --index astral-cu128=https://wheels.astral.sh/simple/cu128/
```

This configures the index and uses it as the source for the metapackage,
matching CUDA core, and PyTorch extension:

```toml
[tool.uv.sources]
transformer-engine = { index = "astral-cu128" }
transformer-engine-cu12 = { index = "astral-cu128" }
transformer-engine-torch = { index = "astral-cu128" }

[[tool.uv.index]]
name = "astral-cu128"
url = "https://wheels.astral.sh/simple/cu128/"
```

Or, with `uv pip`:

```console
$ uv pip install --index https://wheels.astral.sh/simple/cu128/ 'transformer-engine[pytorch]'
```

The matching CUDA core is installed from the same Astral GPU index. Both the
metapackage and core include the same local-version compatibility patch, so the
patched files remain correct regardless of wheel installation order. The
metapackage can be installed from any compatible CUDA index; it does not need a
CUDA-specific local version or a separate build for each Python version or
architecture.

## Supported versions

Wheels can be built for the following NVIDIA Transformer Engine version:

- [`2.16.0`](https://github.com/NVIDIA/TransformerEngine/releases/tag/v2.16)

Transformer Engine 2.16.0 supports Python 3.10 and later. Its pure Python wheel
is shared across CUDA 12.1, 12.4, 12.6, 12.8, 12.9, 13.0, and 13.2 indexes.

## License

build-transformer-engine is licensed under the
[Apache License, Version 2.0](LICENSE).

<div align="center">
  <a target="_blank" href="https://astral.sh" style="background:none">
    <img src="https://raw.githubusercontent.com/astral-sh/ruff/main/assets/svg/Astral.svg" alt="Made by Astral">
  </a>
</div>
