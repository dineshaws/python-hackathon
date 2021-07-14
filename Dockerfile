FROM python:3.6-slim

COPY . /app/

WORKDIR /app/

# temp folders for files
RUN mkdir -p /tmp/input
RUN mkdir -p /tmp/output

RUN pip3 install -r requirements.txt

ARG ENV
ENV ENV=$ENV

EXPOSE 5001
CMD [ "uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "5001" ]

