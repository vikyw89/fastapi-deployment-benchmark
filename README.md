# FastAPI Benchmark

This README provides a benchmark comparison between synchronous and asynchronous endpoints in FastAPI, running under different server configurations.

## Server Code

```python
@app.get("/sync/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    time.sleep(1)
    return {"item_id": item_id, "q": q}

@app.get("/async/{item_id}")
async def aread_item(item_id: int, q: Union[str, None] = None):
    await asyncio.sleep(1)
    return {"item_id": item_id, "q": q}
```

## Benchmark Results

### Running with `fastapi run benchmark/main.py`

| Endpoint | Command                                                 | Requests per second (mean) |
| -------- | ------------------------------------------------------- | -------------------------- |
| Async    | `ab -c 10000 -n 10000 "http://localhost:8000/async/31"` | 1496.38 [#/sec]            |
| Sync     | `ab -c 10000 -n 10000 "http://localhost:8000/sync/31"`  | 39.48 [#/sec]              |

### Running with `poetry run gunicorn benchmark.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker`

| Endpoint | Command                                                 | Requests per second (mean) |
| -------- | ------------------------------------------------------- | -------------------------- |
| Async    | `ab -c 10000 -n 10000 "http://localhost:8000/async/31"` | 3462.74 [#/sec]            |
| Sync     | `ab -c 10000 -n 10000 "http://localhost:8000/sync/31"`  | 105.77 [#/sec]             |

### Running with `poetry run gunicorn benchmark.main:app --workers 12 --worker-class uvicorn.workers.UvicornWorker`

| Endpoint | Command                                                 | Requests per second (mean) |
| -------- | ------------------------------------------------------- | -------------------------- |
| Async    | `ab -c 10000 -n 10000 "http://localhost:8000/async/31"` | 7593.36 [#/sec]            |
| Sync     | `ab -c 10000 -n 10000 "http://localhost:8000/sync/31"`  | 155.80 [#/sec]             |

### Running with `uvicorn benchmark.main:app --workers 4 --host 0.0.0.0 --port 8000`

| Endpoint | Command                                                 | Requests per second (mean) |
| -------- | ------------------------------------------------------- | -------------------------- |
| Async    | `ab -c 10000 -n 10000 "http://localhost:8000/async/31"` | 7507.83 [#/sec]            |

## Conclusion

- Asynchronous endpoints significantly outperform synchronous ones in terms of requests per second.
- Increasing the number of workers with Gunicorn improves the performance for both synchronous and asynchronous endpoints.
- The asynchronous approach is particularly beneficial for I/O-bound operations, as demonstrated in this benchmark.

### @vikyw89-20240805
