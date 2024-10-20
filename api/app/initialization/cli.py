from api.app.command.migrate import migrate


def register_cli(app):
    app.cli.add_command(migrate)
