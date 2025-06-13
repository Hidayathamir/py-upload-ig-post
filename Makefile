run:
	python3 main.py

login:
	python3 login_save_session.py

upload-photos:
	python3 upload_photos.py

pip-freeze:
	pip3 freeze > requirements.txt

create-env-example:
	sed -E 's/^\s*([^#][^=]*)=.*/\1=/' .env > .env-example
