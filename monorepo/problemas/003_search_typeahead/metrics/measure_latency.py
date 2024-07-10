import asyncio
import aiohttp
import time


backend_services = {
    "service_01": {
        "port": 5001,
        "name": "node",
    },
    "service_02": {
        "port": 5002,
        "name": "flask_python_3.6",
    },
    "service_03": {
        "port": 5003,
        "name": "flask_python_3.7",
    },
    "service_04": {
        "port": 5004,
        "name": "flask_python_3.8",
    },
    "service_05": {
        "port": 5005,
        "name": "flask_python_3.9",
    },
    "service_06": {
        "port": 5006,
        "name": "flask_python_3.10",
    },
    "service_07": {
        "port": 5007,
        "name": "flask_python_3.11",
    },
    "service_08": {
        "port": 5008,
        "name": "flask_python_3.12",
    },
    "service_101": {
        "port": 5101,
        "name": "flask_redis_python_3.9",
    },
}

async def fetch(session, url, query):
    start_time = time.monotonic()
    async with session.get(url, params={'q': query}) as response:
        await response.text()  # Leer la respuesta
        latency = time.monotonic() - start_time
        return latency


async def bulk_request_service(N_request, service):
    name = service.get("name", None)
    port = service.get("port", None)
    url = "http://localhost:{0}/search".format(port)
    queries = ['a'] * N_request

    async with aiohttp.ClientSession() as session:
        tasks = []
        for query in queries:
            tasks.append(fetch(session, url, query))

        latencies = await asyncio.gather(*tasks)
        average_latency = sum(latencies) / len(latencies)
        
        print(f'Average latency for service {name}: {average_latency:.4f} seconds')


def test_service(service):
    name = service.get("name", None)
    N_request = 100
    start_time = time.time()
    asyncio.run(bulk_request_service(N_request=N_request, service=service))
    total_time = time.time() - start_time
    print(f'Total time for {N_request} requests on service {name}: {total_time:.4f} seconds')


def compare_latency():
    for key_service in backend_services:
        service = backend_services.get(key_service)
        test_service(service)


if __name__ == '__main__':
    compare_latency()

