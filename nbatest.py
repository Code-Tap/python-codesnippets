'''
Code Snippet from https://terriblecode.com/blog/asynchronous-http-requests-in-python/
Unfortunately Source API has changed and code nolonger works 
'''


import asyncio
import aiofiles
import aiohttp

base_url = 'http://stats.nba.com/stats'
HEADERS = {
    'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/45.0.2454.101 Safari/537.36'),
}

async def get_players(player_args):
    endpoint = '/commonallplayers'
    params = {'leagueid': '00', 'season': '2016-17', 'isonlycurrentseason': '1'}
    url = f'{base_url}{endpoint}'
    print('Getting all players...')
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS, params=params) as resp:
            data = await resp.json()
    player_args.extend(
        [(item[0], item[2]) for item in data['resultSets'][0]['rowSet']])

async def get_player(player_id, player_name):
    endpoint = '/commonplayerinfo'
    params = {'playerid': player_id}
    url = f'{base_url}{endpoint}'
    print(f'Getting player {player_name}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS, params=params) as resp:
            print(resp)
            data = await resp.text()
    async with aiofiles.open(
            f'{player_name.replace(" ", "_")}.json', 'w') as file:
        await file.write(data)

loop = asyncio.get_event_loop()
player_args = []
loop.run_until_complete(get_players(player_args))
loop.run_until_complete(asyncio.gather(*(get_player(*args) for args in player_args)))