BINARY_NAME := python_rest_api
PORT := 8001
TAG_DEV := dev
# only for mac m1
DOCKER_ARG := --platform linux/amd64 
VOLUME := src:/app_src

build-docker: 
	docker build ${DOCKER_ARG} -t $(BINARY_NAME) .
	
run-docker:
	docker run ${DOCKER_ARG} -d -p $(PORT):$(PORT) -v $(VOLUME) $(BINARY_NAME)

push-gcr:
	docker tag $(BINARY_NAME) asia-southeast1-docker.pkg.dev/vertical-realm-410004/trung-repo/$(BINARY_NAME):$(TAG_DEV)
	docker push asia-southeast1-docker.pkg.dev/vertical-realm-410004/trung-repo/$(BINARY_NAME):$(TAG_DEV)
