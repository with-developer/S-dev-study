import time
import subprocess

def measure_nc_execution_time(input_data):
    start_time = time.time()
    # nc 명령어 실행 및 표준 입력으로 데이터 전송
    process = subprocess.Popen(['nc', 'host', 'port'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate(input=input_data.encode())
    end_time = time.time()
    
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
    print(f"Output:\n{output.decode()}")

# 입력 데이터
input_data = "Hello, NC!"
measure_nc_execution_time(input_data)
