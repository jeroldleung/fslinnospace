.PHONY: build-api

DOCKER_REGISTRY = fsl
API_IMAGE = $(DOCKER_REGISTRY)/fslinnospace-api
VERSION = latest

build-api:
		@ docker build -t $(API_IMAGE):$(VERSION) ./api