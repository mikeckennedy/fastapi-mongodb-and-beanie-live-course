import datetime
import colorama
import random
import time


# TODO: For now, same as sync, make it async.

def main():
    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App started.", flush=True)
    data = []
    generate_data(10, data)
    generate_data(10, data)
    process_data(20, data)

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + f"App exiting, total time: {dt.total_seconds():,.2f} sec.", flush=True)


def generate_data(num: int, data: list):
    for idx in range(1, num + 1):
        item = idx * idx
        data.append((item, datetime.datetime.now()))

        print(colorama.Fore.YELLOW + f" -- generated item {idx}", flush=True)
        time.sleep(random.random() + .5)


def process_data(num: int, data: list):
    processed = 0
    while processed < num:
        item = data.pop(0)
        if not item:
            time.sleep(.01)
            continue

        processed += 1
        value = item[0]
        t = item[1]
        dt = datetime.datetime.now() - t

        print(colorama.Fore.CYAN +
              f" +++ Processed value {value} after {dt.total_seconds():,.2f} sec.", flush=True)
        time.sleep(.5)


if __name__ == '__main__':
    main()
