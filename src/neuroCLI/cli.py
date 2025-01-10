import click
from neuroCLI.config.config import init


@click.group
def cli() -> None:
    pass


cli.add_command(init)

if __name__ == "__main__":
    cli()
