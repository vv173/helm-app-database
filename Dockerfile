FROM python:3.8-slim-buster

RUN useradd -m frun
USER frun
WORKDIR /home/frun/webpage/

COPY --chown=frun:frun requirements.txt /home/frun/webpage/requirements.txt
COPY --chown=frun:frun flask-app.py /home/frun/webpage/flask-app.py

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    chmod +x flask-app.py

CMD [ "python3", "flask-app.py"]