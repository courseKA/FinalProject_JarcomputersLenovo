import os
import time
import threading


def work_hard(delay):
    print('Start working')
    time.sleep(delay)
    #total_sum = sum([0, 10000000000**3])
    #print(f'total_sum: {total_sum}')
    
start = time.time()    
# work_hard()
# work_hard()
# work_hard()
tr1 = threading.Thread(target=work_hard, args=(1,))
tr2 = threading.Thread(target=work_hard, args=(1,))
tr3 = threading.Thread(target=work_hard, args=(1,))

tr1.start()
tr2.start()
tr3.start()

tr1.join()
tr2.join()
tr3.join()

end = time.time()
print(f'Time elapsed: {end - start}')