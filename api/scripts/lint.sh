#!usr/bin/env bash

uv run ruff format .
uv run ruff check . --fix
uv run mypy app tests
