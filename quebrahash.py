from multiprocessing import Process, Queue
from string import printable
from itertools import product, cycle
from hashlib import sha256
from queue import Empty
from time import perf_counter


PROCS = 16 # one less that CPU count
MAXLEN = 4
DIGEST = "5fa28ce7d04ee5f2054cc1722ad8f5f7ce11b75dc041d91e1cd934cf82eec2ca"
BATCH = 10_000 # empirically determined to be a fairly good batch size

#print(f"{printable[:-6]}")

# check a batch of passwords
def process(qsend, qres):
    while batch := qsend.get():
        for v in map(str.encode, batch):
            if sha256(v).hexdigest() == DIGEST:
                qres.put(v)
                break

# generate passwords
def genpwd():
    for length in range(MAXLEN, MAXLEN + 1):
        for pwd in product(printable[:-6], repeat=length):
            yield "".join(pwd)
            #print("".join(pwd))


def main():
    qres = Queue() # response queue
    # start PROCS processes each with a discrete input queue
    # each proc uses the same response queue
    procs = []
    for queue in (queues := [Queue() for _ in range(PROCS)]):
        (proc := Process(target=process, args=(queue, qres))).start()
        procs.append(proc)

    batch = []
    qc = cycle(queues)
    solution = None

    for pwd in genpwd():
        batch.append(pwd)
        if len(batch) == BATCH:
            # send batch to the next queue in the cycle
            next(qc).put(batch)
            batch = []
            # occasional check for a response
            try:
                solution = qres.get(block=False)
                break
            except Empty:
                pass

    # if there's no solution (yet) make sure anything left over in the batch list is submitted
    if not solution:
        next(qc).put(batch)
    
    # tells each process to stop
    for queue in queues:
        queue.put(None)

    # wait for all subprocesses to end
    for p in procs:
        p.join()

    # if there was no solution, check the response queue once more
    # ...because there could be subprocesses still running when the main loop ended (generator exhausted)
    if not solution:
        try:
            solution = qres.get(block=False)
        except Empty:
            pass

    if solution:
        print(f"Hash original: {DIGEST}")
        print(f"O conteúdo original era: {solution}")
    else:
        print("No solution found")

if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    duration = int(end - start)
    print(f"Duração={duration}s")