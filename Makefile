.PHONY: install run ui ui-logs docker-up docker-down clean

install:
	pip install -r requirements.txt

run:
	cd src && python main.py

ui:
	cd src && streamlit run app.py --server.port=8501

ui-logs:
	cd src && streamlit run app_with_logs.py --server.port=8501

docker-up:
	docker compose up --build -d

docker-down:
	docker compose down

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null; true
	rm -rf db/ dist/ build/ *.egg-info
