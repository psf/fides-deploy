FROM ethyca/fides:2.15.0rc0

RUN /opt/fides/bin/pip install gunicorn
COPY gunicorn.conf.py /fides/gunicorn.conf.py
