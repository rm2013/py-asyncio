import asyncio
import time

from sequential import build_addition_units

@asyncio.coroutine
def add_one_unit(add_unit):
    sum = 0
    for val in add_unit[0]:
        sum = sum + val
    add_unit = (add_unit[0], sum)
    yield from asyncio.sleep(3)
    return add_unit

if __name__ == "__main__":
    # build add units
    size = 1000000
    start_time = time.time()
    addition_units = build_addition_units(size)
    duration = time.time() - start_time
    print(f"Built {size} units in {duration} seconds")

    start_time = time.time()
    loop = asyncio.get_event_loop()
    #loop through and add tasks one for each addition unit
    tasks = []
    for add_unit in addition_units:
        task = asyncio.ensure_future(add_one_unit(add_unit))
        tasks.append(task)
    done, _ = loop.run_until_complete(asyncio.wait(tasks))
    #done is the array of returned addition units with the sum
    duration = time.time() - start_time
    print(f"Added {len(addition_units)} addition units in {duration} seconds")
