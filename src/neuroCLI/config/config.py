import click
from neuroCLI.files import filemanager
from neuroCLI.config import setup
from neuroCLI.com.serverCom.tokenManager import status


@click.command()
@click.option("--m", help="h to be a host, c to be a client")
def init(m: str) -> None:
    if m not in {"host", "client"}:
        click.echo(
            click.style(
                "Please specify if you are a host or client", bold=True, fg="red"
            )
        )
        return

    user = filemanager.verifyToken()

    if user:
        role = "Host" if m == "host" else "Client"

        if role == "Host":
            setup.setup(user, role)

            status.startStatusPing(user)

    else:
        email = click.prompt("NeuroGrid email", type=str)
        password = click.prompt(
            "NeuroGrid password", hide_input=True, confirmation_prompt=True
        )

        if not filemanager.writeToken(email, password):
            click.echo(click.style("Invalid credentials", bold=True, fg="red"))
        else:
            click.echo(click.style("Please initialize again", bold=True, fg="red"))
