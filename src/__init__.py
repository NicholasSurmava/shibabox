from flask import Flask, render_template

import asyncio
import aiohttp

app = Flask(__name__)



@app.route('/')
def index():
    # async def main():
    #     async with aiohttp.ClientSession() as session:
    #         async with session.get('https://source.unsplash.com/random') as resp:
    #             response = await resp.read()
    #             print(response)

    # asyncio.run(main())

    img = "https://source.unsplash.com/random"

    return render_template('index.html', img=img)






