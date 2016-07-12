from invoke import run, task


@task(aliases=['scss', 'a'])
def sass(ctx):
    run('sass --watch project/client/static/stylesheets/', echo=True)


@task
def init(ctx):
    cmd = ('python manage.py create_db'
           'python manage.py db init'
           'python manage.py db migrate'
           'python manage.py create_admin'
           'python manage.py create_data')
    run(cmd, echo=True)


@task(aliases=['s', 'serve'])
def server(ctx, port=5000):
    run('python manage.py runserver -p {}'.format(port), echo=True)


@task
def migrate(ctx):
    run('python manage.py db migrate')


@task
def js(ctx, prod=False):
    mode = 'build' if prod else 'dev'
    run('cd project/client/static/app && npm run {}'.format(mode), echo=True)


@task(aliases=['t'])
def test(ctx, cov=False):
    if cov:
        run('python manage.py cov', echo=True)
    else:
        run('python manage.py test', echo=True)


@task(default=True)
def usage(ctx):
    run('invoke --list', echo=True)
