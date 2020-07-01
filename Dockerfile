FROM python:3.6
WORKDIR /usr/src/app
ARG PIP_INDEX_URL=http://nexus.reduc.edu.cu/repository/pypi.python.org-proxy/simple
ARG PIP_TRUSTED_HOST=nexus.reduc.edu.cu
ARG PIP_TIMEOUT=350

ENV DEBUG=True
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DB_ENGINE=django.db.backends.sqlite3
ENV DB_HOST=
ENV DB_PORT=
ENV DB_NAME=db.sqlite3
ENV DB_USER=
ENV DB_PASSWORD=
ENV SECRET_KEY=mysocratesnotes
ENV DEFAULT_SUPERUSER_NAME=admin
ENV DEFAULT_SUPERUSER_EMAIL=admin@example.com
ENV DEFAULT_SUPERUSER_PASSWORD=secret
ENV AD_DNS_NAME=
ENV AD_LDAP_PORT=
ENV LDAP_AUTH_USE_TLS=
ENV LDAP_AUTH_SEARCH_BASE=
ENV LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN=

EXPOSE 8000
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
VOLUME /usr/src/app/media
ENTRYPOINT ["./run_web.sh"]
