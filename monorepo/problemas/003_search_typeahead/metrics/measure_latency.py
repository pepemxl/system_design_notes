import asyncio
import aiohttp
import time


async def fetch(session, url, query):
    start_time = time.monotonic()
    async with session.get(url, params={'q': query}) as response:
        await response.text()  # Leer la respuesta
        latency = time.monotonic() - start_time
        return latency


async def test_node(N_request):
    url = 'http://localhost:3000/search'
    queries = ['a'] * N_request

    async with aiohttp.ClientSession() as session:
        tasks = []
        for query in queries:
            tasks.append(fetch(session, url, query))

        latencies = await asyncio.gather(*tasks)
        average_latency = sum(latencies) / len(latencies)
        
        print(f'Average latency: {average_latency:.4f} seconds')


async def test_flask(N_request):
    url = 'http://localhost:5001/search'
    queries = ['a'] * N_request

    async with aiohttp.ClientSession() as session:
        tasks = []
        for query in queries:
            tasks.append(fetch(session, url, query))

        latencies = await asyncio.gather(*tasks)
        average_latency = sum(latencies) / len(latencies)
        
        print(f'Average latency: {average_latency:.4f} seconds')


def test_latency_backend_node():
    N_request = 100
    start_time = time.time()
    asyncio.run(test_node(N_request=N_request))
    total_time = time.time() - start_time
    print(f'Total time for {N_request} requests: {total_time:.4f} seconds')


def test_latency_backend_flask():
    N_request = 100
    start_time = time.time()
    asyncio.run(test_flask(N_request=N_request))
    total_time = time.time() - start_time
    print(f'Total time for {N_request} requests: {total_time:.4f} seconds')


if __name__ == '__main__':
    test_latency_backend_node()
    test_latency_backend_flask()
