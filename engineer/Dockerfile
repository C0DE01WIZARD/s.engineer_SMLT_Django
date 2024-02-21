FROM python

COPY ./requirements.txt/ engineer/
COPY ./ engineer/
WORKDIR ./engineer
EXPOSE 8000



ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install --upgrade pip
#RUN apk add postgresql-client build-base postgresql-dev
RUN pip install -r requirements.txt
RUN adduser --disabled-password rushan-user
USER rushan-user