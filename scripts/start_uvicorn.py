def run():
    import subprocess
    import multiprocessing

    cpu_count = multiprocessing.cpu_count()
    print(f"Starting with CPU count: {cpu_count}")
    subprocess.run(
        f"uvicorn benchmark.main:app --workers {cpu_count} --host 0.0.0.0 --port 8000",
        shell=True,
    )
