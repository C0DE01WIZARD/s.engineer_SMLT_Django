from celery import Celery

app = Celery('tasks', broker='redis://localhost')


@app.tasks
def add(x, y):
    return x + y


a = add(1, 2)
print(a)