bind = "unix:/var/run/cabotage/cabotage.sock"
backlog = 2048
preload_app = True
max_requests = 2048
max_requests_jitter = 128

worker_connections = 1000
timeout = 60
keepalive = 2

errorlog = "-"
loglevel = "debug"
accesslog = "-"

#statsd_host = "localhost:8125"


def when_ready(server):
    open("/tmp/app-initialized", "w").close()
