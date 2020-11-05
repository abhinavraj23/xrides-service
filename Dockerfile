FROM python:3.7.7
ENV PYTHONUNBUFFERED 1

ARG build_env
ENV BUILD_ENV ${build_env}

RUN [ -d /xrides ] || mkdir /xrides;
COPY ./xrides /xrides
COPY  requirements.txt /xrides
WORKDIR /xrides
RUN pip install -r requirements.txt
# RUN python manage.py migrate

# EXPOSE 8000
# CMD python manage.py runserver
