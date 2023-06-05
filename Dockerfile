FROM ewdurbin/fides:2.14.1b8

RUN /opt/fides/bin/pip install gunicorn
COPY gunicorn.conf.py /fides/gunicorn.conf.py
