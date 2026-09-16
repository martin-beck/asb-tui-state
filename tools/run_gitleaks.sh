#!/usr/bin/env bash
# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
set -euo pipefail

readonly VERSION=8.30.1
readonly ARCHIVE=gitleaks_8.30.1_linux_x64.tar.gz
readonly DIGEST=551f6fc83ea457d62a0d98237cbad105af8d557003051f41f3e7ca7b3f2470eb
readonly SCRATCH="$(mktemp -d)"
trap 'rm -rf -- "${SCRATCH}"' EXIT HUP INT TERM

curl --fail --location --proto '=https' --tlsv1.2 --silent --show-error \
  --output "${SCRATCH}/${ARCHIVE}" \
  "https://github.com/gitleaks/gitleaks/releases/download/v${VERSION}/${ARCHIVE}"
printf '%s  %s\n' "${DIGEST}" "${SCRATCH}/${ARCHIVE}" | sha256sum --check --status
tar -xzf "${SCRATCH}/${ARCHIVE}" -C "${SCRATCH}" gitleaks
"${SCRATCH}/gitleaks" git --redact --no-banner "$@" .
