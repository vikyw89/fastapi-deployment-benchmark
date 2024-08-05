def run():
    import subprocess
    import multiprocessing

    cpu_count = multiprocessing.cpu_count()
    print(f"Starting with CPU count: {cpu_count}")
    subprocess.run(
        f"gunicorn benchmark.main:app --workers {cpu_count} --worker-class uvicorn.workers.UvicornWorker",
        shell=True,
    )
