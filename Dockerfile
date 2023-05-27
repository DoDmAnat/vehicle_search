FROM python:3.11
WORKDIR /vehicle_app
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .
RUN chmod a+x docker/*.sh
CMD ["gunicorn", "vehicle_app.wsgi:application", "--bind", "0:8000" ]