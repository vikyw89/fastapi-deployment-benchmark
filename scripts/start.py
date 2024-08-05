def run():
    import subprocess
    import multiprocessing

    cpu_count = multiprocessing.cpu_count()
    print(f"Starting with CPU count: {cpu_count}")
    subprocess.run(
        f"gunicorn benchmark.main:app -w {cpu_count} --worker-class uvicorn.workers.UvicornWorker -b 0.0.0.0:8000",
        shell=True,
    )
