import GPUtil
import torch
import click


def getHardwareInfo():
    gpus = GPUtil.getGPUs()
    if not gpus:
        return "No GPU found"

    gpu_info = []
    for gpu in gpus:
        gpu_info.append(
            {
                "id": gpu.id,
                "name": gpu.name,
                "load": f"{gpu.load * 100:.1f}%",
                "memory_total": f"{gpu.memoryTotal} MB",
                "memory_used": f"{gpu.memoryUsed} MB",
                "memory_free": f"{gpu.memoryFree} MB",
                "temperature": f"{gpu.temperature} °C",
            }
        )
    return gpu_info


def getHardwareCudaInfo():
    if torch.cuda.is_available():
        return torch.cuda.get_device_properties(0)
    return "CUDA is unavailable"


def setup(user: str, role: str):
    click.echo(click.style(f"Authorized {role} - User: {user}", bold=True, fg="green"))

    gpuInfo = getHardwareInfo()
    if isinstance(gpuInfo, str):
        click.echo(click.style("No GPU found", bold=True, fg="red"))
    else:
        click.echo(click.style("Detected GPU(s):", bold=True, fg="green"))
        for gpu in gpuInfo:
            click.echo(
                click.style(
                    f"  - GPU {gpu['id']}: {gpu['name']}", fg="yellow", bold=True
                )
            )
            click.echo(
                click.style(
                    f"    Load: {gpu['load']}, "
                    f"Memory: {gpu['memoryUsed']} / {gpu['memoryTotal']}, "
                    f"Free Memory: {gpu['memoryFree']}, "
                    f"Temperature: {gpu['temperature']}",
                    fg="cyan",
                )
            )

    cudaInfo = getHardwareCudaInfo()
    if isinstance(cudaInfo, str):
        click.echo(click.style("CUDA is unavailable", bold=True, fg="red"))
    else:
        click.echo(click.style("CUDA Details:", bold=True, fg="green"))
        click.echo(
            click.style(
                f"  Name: {cudaInfo.name}, "
                f"Memory: {cudaInfo.total_memory / (1024**2):.2f} MB, "
                f"Compute Capability: {cudaInfo.major}.{cudaInfo.minor}",
                fg="magenta",
            )
        )
