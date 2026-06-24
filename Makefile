test:
	coverage run -m pytest
coverage:
	coverage html
deploy:
	docker-compose -f deploy.yaml up -d
clean:
	rm -rf __pycache__ build *.egg-info