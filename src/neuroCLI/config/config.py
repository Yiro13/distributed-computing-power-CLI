import click
from neuroCLI.files import filemanager


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
        click.echo(
            click.style(f"Authorized {role}, User: {user}", bold=True, fg="green")
        )

    else:
        email = click.prompt("NeuroGrid email", type=str)
        password = click.prompt(
            "NeuroGrid password", hide_input=True, confirmation_prompt=True
        )

        if not filemanager.writeToken(email, password):
            click.echo(click.style("Invalid credentials", bold=True, fg="red"))
