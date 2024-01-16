BINARY_NAME := python-rest-api
PORT := 8000
TAG := latest
# only for mac m1
DOCKER_ARG := --platform linux/amd64 
VOLUME := src:/app_src

build-docker: 
	docker build ${DOCKER_ARG} -t $(BINARY_NAME) .
	
run-docker:
	docker run ${DOCKER_ARG} -d -p $(PORT):$(PORT) $(BINARY_NAME)

push-dockerhub:
	docker tag $(BINARY_NAME) tvuong/$(BINARY_NAME):$(TAG)
	docker push tvuong/$(BINARY_NAME):$(TAG)

push-gcr:
	docker tag $(BINARY_NAME) asia-southeast1-docker.pkg.dev/vertical-realm-410004/trung-repo/$(BINARY_NAME):$(TAG_DEV)
	docker push asia-southeast1-docker.pkg.dev/vertical-realm-410004/trung-repo/$(BINARY_NAME):$(TAG_DEV)
