#FROM python:3.9.7
#WORKDIR /sf3-accounts-module
#RUN pip install poetry
#COPY ./pyproject.toml /sf3-accounts-module/pyproject.toml
#RUN poetry config virtualenvs.create false && poetry install --no-root --no-dev
#COPY ./src /sf3-accounts-module/src
#COPY ./main.py /sf3-accounts-module/main.py
#RUN mkdir -p /sf3-accounts-module/log
#COPY ./deployments/entrypoint.sh /sf3-accounts-module/entrypoint.sh
#RUN chmod +x /sf3-accounts-module/entrypoint.sh
#CMD ["/sf3-accounts-module/entrypoint.sh"]

FROM python:3.9.7-slim as Base-image
RUN apt-get update -y && apt-get install -y procps vim  && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /sf3-account-module
RUN python -m venv /account_venv

ENV PATH="/account_venv/bin:$PATH"

COPY ./pyproject.toml /sf3-account-module/pyproject.toml

#RUN pip install poetry && poetry config virtualenvs.create false \
#    && poetry install --no-root
RUN pip install --no-cache-dir --compile --upgrade pip poetry wheel

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-dev


FROM python:3.9.7-slim as build-image
RUN apt-get update -y && apt-get install -y procps vim  && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /sf3-account-module

COPY --from=Base-image /sf3-account-module/pyproject.toml /sf3-account-module/pyproject.toml
COPY --from=Base-image /account_venv /account_venv

ENV PATH="/account_venv/bin:$PATH"
COPY ./src /sf3-account-module/src
COPY ./main.py /sf3-account-module/main.py

COPY ./deployments/entrypoint.sh /sf3-account-module/entrypoint.sh

RUN chmod +x /sf3-account-module/entrypoint.sh

CMD ["/sf3-account-module/entrypoint.sh"]
