FROM python
WORKDIR /app
COPY requirements.txt ./
ENV PYTHONDONTWRITTEBYTECODE 1

EXPOSE 8000
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN adduser --disabled-password rushan-user
USER rushan-user
