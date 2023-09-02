import aiohttp
import asyncio
import random


async def upload_data(session, game_number, session_id, score):
    url = f'http://localhost:8000/upload_game{game_number}'
    params = {
            'session_id': session_id,
            'student_id': "your student id",  # TODO
            'name'      : "your name",  # TODO
            'score'     : score
    }
    async with session.post(url, params=params) as response:
        print(response.status)


async def main():
    async with aiohttp.ClientSession() as session:
        session_id_response = await session.get('http://localhost:8000/session_id', params={'game': 1})
        session_id = await session_id_response.json()

        score = 0

        while True:
            tasks = []
            for game_number in range(1, 4):
                task = upload_data(session, game_number, session_id, score)
                tasks.append(task)
            await asyncio.gather(*tasks)
            score += 1


if __name__ == '__main__':
    asyncio.run(main())
