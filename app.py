from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, login_required

# from .operations.task import get_all_task, create_tasks, get_task

app = Flask(__name__)
app.config['SECRET_KEY'] = 'This web-layout will be my base to creating a most useful, helpful and comprehensive business'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # Database file will be created in the project folder
db = SQLAlchemy(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)


def get_all_task():
    return Task.query.all()


def create_tasks(content):
    new_task = Task(content=content)
    db.session.add(new_task)
    db.session.commit()
    return new_task


def get_task(task_id):
    return Task.query.get_or_404(task_id)


@app.route('/')
def index():
    # from .operations.task import get_all_task
    tasks = get_all_task()
    return render_template('index.html', tasks=tasks, task_list_heading='All Tasks')


@app.route('/create_task', methods=['POST'])
def create_task():
    # from .operations.task import create_tasks
    content = request.form.get('content')
    new_task = create_tasks(content=content)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    # from .operations.task import get_task
    task = get_task(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/completed_tasks')
def completed_tasks():
    completed_tasks = Task.query.filter_by(completed=True).all()
    return render_template('index.html', tasks=completed_tasks, task_list_heading='Completed Tasks')


@app.route('/active_tasks')
def active_tasks():
    active_tasks = Task.query.filter_by(completed=False).all()
    return render_template('index.html', tasks=active_tasks, task_list_heading='Active Tasks')


# @app.route('/delete_tasks')
# def delete_task(task_id):
#     task = get_task(task_id)
#     db.session.delete(task)
#     db.session.commit()
#     return redirect(url_for('index'))
@app.route('/delete_task/<int:task_id>', methods=['GET', 'POST'])
def delete_task(task_id):
    task = get_task(task_id)

    if request.method == 'POST':
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('delete.html', task=task)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=False)
