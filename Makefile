VERSION=latest
IMAGE=fastapi

build:
	docker build -t ${IMAGE}:${VERSION} .

run:
	docker run -p 80:80 ${IMAGE}:${VERSION}