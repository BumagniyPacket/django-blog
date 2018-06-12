import environ
import multiprocessing

env = environ.Env()

DEBUG = env.bool('DJANGO_DEBUG', False)

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
threads = workers
worker_class = 'meinheld.gmeinheld.MeinheldWorker'
user = 'django'
group = 'django'

if DEBUG:
    workers = 1
    threads = 1
    reload = True
    worker_class = 'sync'
