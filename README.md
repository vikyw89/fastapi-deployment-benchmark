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

server is run with

```python
fastapi run benchmark/main.py
```

test is run with

```bash
ab -c 10000 -n 10000 "http://localhost:8000/async/31"
```

result = Requests per second: 1496.38 [#/sec] (mean)

```bash
ab -c 10000 -n 10000 "http://localhost:8000/async/31"
```

result = Requests per second: 39.48 [#/sec] (mean)

server is run with

```bash
poetry run gunicorn benchmark.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker
```

test is run with

```bash
ab -c 10000 -n 10000 "http://localhost:8000/async/31"
```

Requests per second: 3462.74 [#/sec] (mean)

```bash
ab -c 10000 -n 10000 "http://localhost:8000/async/31"
```

Requests per second: 105.77 [#/sec] (mean)

server is run with

```bash
poetry run gunicorn benchmark.main:app --workers 12 --worker-class uvicorn.workers.UvicornWorker
```

test is run with

```bash
ab -c 10000 -n 10000 "http://localhost:8000/async/31"
```

Requests per second: 7593.36 [#/sec] (mean)

```bash
ab -c 10000 -n 10000 "http://localhost:8000/async/31"
```

Requests per second: 155.80 [#/sec] (mean)
