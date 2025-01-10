import click
from neuroCLI.files import filemanager
from neuroCLI.com.serverCom import status


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

    if filemanager.verifyToken():
        """
            Initializing user on platform
        """
        clientID = "Yiro-DEEXCCJ"
        status.run(clientID)

        role = "Host" if m == "host" else "Client"
        click.echo(click.style(f"Authorized {role}", bold=True, fg="green"))

    """else:
        username = click.prompt("NeuroGrid username", type=str)
        password = click.prompt(
            "NeuroGrid password", hide_input=True, confirmation_prompt=True
        )"""
