import asyncio
import concurrent.futures
import requests

async def main():

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:

        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(executor, requests.get, 'http://example.com')
            for i in range(2000)
                ]
        for response in await asyncio.gather(*futures):
            print(response)
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(main())