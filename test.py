import time
from multiprocessing import Pool

def f(a_list):
    out = 0
    for n in a_list:
        out += n * n
        time.sleep(0.1)

    return out


def f_mp(a_list):
    chunks = [a_list[i::5] for i in range(5)]

    pool = Pool(processes=5)

    result = pool.map(f, chunks)

    return sum(result)
print(f_mp([1,2,3,4,5,6,7,8,9,10]))
