import asyncio
import random

#await ждет результата

async def f(): # это карутина, а не функция
    while True:
        print('f() func')
        await asyncio.sleep(1)


def g_helper():
    return random.randint(0, 100)


async def g(): # это карутина, а не функция
    while True:
        print(g_helper())
        await asyncio.sleep(1)



async def main():
    main_loop.create_task(g()) # создаст задачу main И задачу g, две задачи параллельно
    main_loop.create_task(f()) # вначале создает задачу, потом выполняет f(), потом g()
# await f() это подзадача


main_loop = asyncio.get_event_loop()
main_loop.run_until_complete(main())
main_loop.run_forever() # после добавления этой строки, второй принт из g() довыполнился
