def run():
    import subprocess

    subprocess.run(
        "fuser -k 8000/tcp", shell=True
    )
    subprocess.run(
        "poetry run uvicorn benchmark.main:app --reload",
        shell=True,
    )