import time
import threading

start = time.perf_counter()
def do_something():
    print('sleeping 1 second')
    time.sleep(1)
    print('Done sleeping')

# func() --> 1 second --> func() --> 1 second --> Done
do_something()
do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')