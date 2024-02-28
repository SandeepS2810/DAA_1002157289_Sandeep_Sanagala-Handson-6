import timeit
import random
import matplotlib.pyplot as plt

def QS_non_random(li):
    if len(li) <= 1:
        return li
    p = li[len(li) // 2]
    s = [x for x in li if x < p]
    eq = [x for x in li if x == p]
    l = [x for x in li if x > p]
    return QS_non_random(s) + eq + QS_non_random(l)

def benchmark_qs(func, data):
    start_time = timeit.default_timer()
    result = func(data.copy())
    end_time = timeit.default_timer()
    print(f"Input: {data[:10]}... | Output: {result[:10]}... | Time: {end_time - start_time:.6f} seconds")
    return end_time - start_time

def best_case(size):
    return list(range(size))

def worst_case(size):
    return list(range(size, 0, -1))

def avg_case(size):
    return random.sample(range(size * 10), size)

sizes = [10, 100, 1000]
best = []
worst = []
avg = []

for size in sizes:
    bc_input = best_case(size)
    wc_input = worst_case(size)
    avg_input = avg_case(size)  
    print(f"\n*** Input Size: {size} ***")
    print("\nBest Case:")
    best.append(benchmark_qs(QS_non_random, bc_input))

    print("\nWorst Case:")
    worst.append(benchmark_qs(QS_non_random, wc_input))

    print("\nAverage Case:")
    avg.append(benchmark_qs(QS_non_random, avg_input))

plt.plot(sizes, best, label='Non-random pivot (Best Case)')
plt.plot(sizes, worst, label='Non-random pivot (Worst Case)')
plt.plot(sizes, avg, label='Non-random pivot (Average Case)')

plt.xlabel('Input Size (n)')
plt.ylabel('Average Runtime (seconds)')
plt.legend()
plt.show()
