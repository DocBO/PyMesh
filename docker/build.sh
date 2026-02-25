#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

IMAGE_NAME="${IMAGE_NAME:-pymesh/pymesh:latest}"
UBUNTU_VERSION="${UBUNTU_VERSION:-22.04}"
NUM_CORES="${NUM_CORES:-0}"
RUN_TESTS="${RUN_TESTS:-0}"

cd "${REPO_ROOT}"

docker build \
  -f docker/Dockerfile \
  --build-arg UBUNTU_VERSION="${UBUNTU_VERSION}" \
  --build-arg NUM_CORES="${NUM_CORES}" \
  --build-arg RUN_TESTS="${RUN_TESTS}" \
  -t "${IMAGE_NAME}" \
  .
