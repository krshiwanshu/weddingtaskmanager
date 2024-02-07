# from ..app import db
# from ..models.task import Task
#
#
# def get_all_task():
#     return Task.query.all()
#
#
# def create_tasks(content):
#     new_task = Task(content=content)
#     db.session.add(new_task)
#     db.session.commit()
#     return new_task
#
#
# def get_task(task_id):
#     return Task.query.get_or_404(task_id)