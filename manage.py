import os
from app import create_app,db
from flask_script import Shell,Manager

app = create_app('default')
manage = Manager(app)

def make_shell_context():
    return dict(app = app,db = db)
manage.add_command("shell",Shell(make_context = make_shell_context))

if __name__ == '__main__':
    manage.run()

