run_dev:
	uvicorn app.main:app --reload

run:
	docker run -it -v $(shell pwd)/app:/app -p 8000:8000 swe_ha

build:
	docker build -t swe_ha .
