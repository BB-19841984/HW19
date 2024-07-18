import time
import threading

def create(file) -> None:
    time.sleep(1)
    return create(file)


if __name__ == "__main__":
    times = 100
    threads = []

    start = time.time()
    for _ in range(times):
        create('myfile.txt')
    print(f"Времы выполнения {time.time() - start}")

    for i in range(times):
        thread = threading.Thread(target=create, args=(i,))
        thread.start()
        threads.append(thread)
    
    #дожидаемся завершения всех потоков
    for thread in threads:
        thread.join()
