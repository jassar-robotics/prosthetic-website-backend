
# For Development Pipeline

build:
	DJANGO_ENV=development docker-compose -f docker-compose.dev.yaml build --no-cache
up: 
	docker-compose -f docker-compose.dev.yaml up
down:
	docker-compose -f docker-compose.dev.yaml down
frontend: 
	docker exec -it compass-frontend-dev bash

backend: 
	docker exec -it compass-backend-dev bash

db:
	docker exec -it compass-db-dev bash

superuser:
	docker exec -it compass-backend-dev python manage.py createsuperuser

makemigrations:
	docker exec -it compass-backend-dev  python manage.py makemigrations

showmigrations:
	docker exec -it compass-backend-dev  python manage.py showmigrations

makemigrationsmerge:
	docker exec -it compass-backend-dev  python manage.py makemigrations --merge

migrate:
	docker exec -it compass-backend-dev  python manage.py migrate

loaddata:
	docker exec -it compass-backend-dev python manage.py loaddata fixtures/$(f).json

dumpdata: 
	docker exec -it compass-backend-dev python manage.py dumpdata $(f) --output=fixtures/$(f).json





# For Production Pipeline

prod-build:
	DJANGO_ENV=production docker-compose -f docker-compose.production.yaml  build --no-cache
prod-up: 
	docker-compose -f  docker-compose.production.yaml  up
prod-down:
	docker-compose -f docker-compose.production.yaml down
prod-frontend: 
	docker exec -it compass-frontend-production bash

prod-backend: 
	docker exec -it compass-backend-production bash

prod-db:
	docker exec -it compass-db-production bash

prod-superuser:
	docker exec -it compass-backend-production python manage.py createsuperuser

prod-makemigrations:
	docker exec -it compass-backend-production  python manage.py makemigrations

prod-showmigrations:
	docker exec -it compass-backend-production  python manage.py showmigrations

prod-makemigrationsmerge:
	docker exec -it compass-backend-production  python manage.py makemigrations --merge

prod-migrate:
	docker exec -it compass-backend-production  python manage.py migrate
