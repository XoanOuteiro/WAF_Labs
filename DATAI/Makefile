.PHONY: build up down clean db-reset

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

clean:
	docker-compose down -v
	rm -f app/database.db

db-reset:
	rm -f app/database.db
	sqlite3 app/database.db < app/schema.sql

