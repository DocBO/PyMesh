# syntax=docker/dockerfile:1.7
ARG UBUNTU_VERSION=22.04

FROM ubuntu:${UBUNTU_VERSION} AS builder
ARG DEBIAN_FRONTEND=noninteractive
ARG NUM_CORES=0
ARG RUN_TESTS=0
ARG PYTHON_BIN=python3.13

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
WORKDIR /opt/pymesh
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"
ENV CFLAGS="-fcommon"
ENV CXXFLAGS="-fpermissive -fcommon"

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    build-essential \
    ca-certificates \
    cmake \
    curl \
    dirmngr \
    git \
    gnupg \
    libboost-dev \
    libboost-thread-dev \
    libeigen3-dev \
    libgmp-dev \
    libgmpxx4ldbl \
    libmpfr-dev \
    libtbb-dev \
    ninja-build \
    patchelf \
    pkg-config \
    software-properties-common \
    python3 \
    python3-dev \
    python3-pip \
    python3-venv \
    unzip \
    zip && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update && apt-get install -y --no-install-recommends \
    python3.13 \
    python3.13-dev \
    python3.13-venv && \
    rm -rf /var/lib/apt/lists/*

COPY . /opt/pymesh

RUN if [ -d .git ]; then git submodule update --init --recursive; fi

RUN if [ -f third_party/draco/src/draco/core/hash_utils.h ] && \
      ! grep -q '^#include <cstddef>$' third_party/draco/src/draco/core/hash_utils.h; then \
      sed -i '/^#include <functional>$/a #include <cstddef>' \
        third_party/draco/src/draco/core/hash_utils.h; \
    fi

RUN if [ -f third_party/draco/src/draco/io/parser_utils.cc ] && \
      ! grep -q '^#include <limits>$' third_party/draco/src/draco/io/parser_utils.cc; then \
      sed -i '/^#include <cmath>$/a #include <limits>' \
        third_party/draco/src/draco/io/parser_utils.cc && \
      if ! grep -q '^#include <limits>$' third_party/draco/src/draco/io/parser_utils.cc; then \
        sed -i '/^#include "draco\\/io\\/parser_utils.h"$/a #include <limits>' \
          third_party/draco/src/draco/io/parser_utils.cc; \
      fi; \
    fi

RUN ${PYTHON_BIN} -m venv "${VIRTUAL_ENV}" && \
    python -m pip install --upgrade pip setuptools wheel && \
    python -m pip install --no-cache-dir -r python/requirements.txt

RUN if [ "${NUM_CORES}" = "0" ]; then \
      NUM_CORES=$(nproc); \
    fi && \
    export NUM_CORES && \
    ./setup.py bdist_wheel

RUN python -m pip install --no-cache-dir dist/*.whl

RUN if [ "${RUN_TESTS}" = "1" ]; then \
      python -c "import pymesh; r=pymesh.test(verbosity=1); import sys; sys.exit(0 if r.wasSuccessful() else 1)"; \
    fi

FROM ubuntu:${UBUNTU_VERSION} AS runtime
ARG DEBIAN_FRONTEND=noninteractive
ARG PYTHON_BIN=python3.13

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
WORKDIR /workspace
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    ca-certificates \
    curl \
    file \
    dirmngr \
    less \
    libgcc-s1 \
    libgmp10 \
    libgmpxx4ldbl \
    libgomp1 \
    libmpfr6 \
    libstdc++6 \
    libtbb12 \
    procps \
    gnupg \
    software-properties-common \
    python3 \
    python3-pip && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update && apt-get install -y --no-install-recommends \
    python3.13 \
    python3.13-venv && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /opt/pymesh/dist/*.whl /tmp/
RUN ${PYTHON_BIN} -m venv "${VIRTUAL_ENV}" && \
    python -m pip install --upgrade pip setuptools wheel && \
    python -m pip install --no-cache-dir numpy scipy /tmp/*.whl && \
    rm -f /tmp/*.whl && \
    rm -rf /root/.cache/pip

# Keep only runtime-relevant installed module artifacts in the final image.
ENV PYTHONDONTWRITEBYTECODE=1

CMD ["bash"]
