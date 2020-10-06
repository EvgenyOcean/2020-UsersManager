FROM python:alpine3.7 

ENV SECRET_KEY=SomethingSuperSecret123Hushhhh
ENV FLASK_APP=main.py

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt 

ENTRYPOINT [ "flask" ] 

CMD [ "run", "-h", "0.0.0.0", "-p", "5000" ] 

EXPOSE 5000