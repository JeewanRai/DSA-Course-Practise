import time

def measure_time(slow_fast_func):
    def slow_fast_logic_func(*arg, **kwargs):
        # logic will be build inside 
        start_time = time.time()
        result = slow_fast_func(*arg, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return result
    return slow_fast_logic_func

@measure_time
def slow_function():
    time.sleep(2)


if __name__ == "__main__":
    print(slow_function())
    

