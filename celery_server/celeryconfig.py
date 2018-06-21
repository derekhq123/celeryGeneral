BROKER_URL='pyamqp://'
CELERY_RESULT_BACKEND='redis://localhost'

##CELERY_IMPORTS=()
CELERY_IMPORTS=('celery_server.library')
CELERY_TASK_SERIALIZER='pickle'
CELERY_RESULT_SERIALIZER='pickle'
CELERY_ACCEPT_CONTENT=['pickle','json']
