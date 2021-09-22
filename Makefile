.PHONY: build
build:
	docker-compose -f docker-compose.yml build

.PHONY: up
up:
	find . -name "*.pyc" -exec rm -rf {} \;
	docker-compose -f docker-compose.yml up

.PHONY: bash
bash:
	docker exec -it poste-auction-notify bash