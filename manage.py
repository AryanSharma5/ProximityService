from flask.cli import FlaskGroup

from src import db
from src.app import app

cli = FlaskGroup(app)


@cli.add_command("create_models")
def create_models():
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()
