COMPOSE=docker-compose
EXEC=$(COMPOSE) exec
BUILD=$(COMPOSE) build
UP=$(COMPOSE) up -d
LOGS=$(COMPOSE) logs
STOP=$(COMPOSE) stop
RM=$(COMPOSE) rm
DOWN=$(COMPOSE) down
NPM=npm
NPMINSTALL=$(NPM) install
NPMBUILD=$(NPM) build
NPMDEV=$(NPM) run-script docker-dev
NUXT=$(EXEC) nuxt
DJANGO=$(EXEC) django
SUBMODULE=git submodule

all: docker/up api/migrate api/run ## develop backend

client: docker/up client/install client/run ## develop client

docker/up: ## docker up
	$(UP)

docker/logs: ## docker logs
	$(LOGS)

docker/stop: ## docker stop
	$(STOP)

docker/clean: ## docker clean
	$(RM)

docker/down: ## docker down
	$(DOWN)

api/migrate: ## Django migrate
	$(DJANGO) ./manage.py migrate

api/run: ## Runserver in django container
	$(DJANGO) ./manage.py runserver 0.0.0.0:8000

client/install: ## npm install
	$(NUXT) $(NPMINSTALL)

client/run: ## npm run-script dev
	$(NUXT) $(NPMDEV)

nuxt/ash: ## nuxt container ash
	$(NUXT) ash

django/bash: ## django container bash
	$(DJANGO) bash

submodule: submodule/init submodule/update ## git submodule init & update

submodule/init: ## git submodule init
	$(SUBMODULE) init

submodule/update: ## git submodule update
	$(SUBMODULE) update --remote

help: ## Display this help screen
	@grep -E '^[a-zA-Z/_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
