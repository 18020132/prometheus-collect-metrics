import datetime
import time
import requests
import argparse
from PromQL import PromQL

class prometheus_collect_metrics():
  def Memory_Total(): 
    response = requests.get(PROMETHEUS + '/api/v1/query',
      params={ 
        # 'query': f"{memTotal}"
        'query' : f"{memory_free()}"
      })
    results = response.json()['data']['result']
    for result in results:
      memory_total = '{value[1]}'.format(**result)
    return print("Memory Free: " + str(round(int(memory_total)/pow(10,9),2)) + "GB")

  def Memory_Free():
    response = requests.get(PROMETHEUS + '/api/v1/query',
      params={ 
        # 'query': f"{memFree}"
        'query': f"{memory_total()}"
      })
    results = response.json()['data']['result']
    for result in results:
      memory_free = '{value[1]}'.format(**result)
    return print("Memory total: " + str(round(int(memory_free)/pow(10,9),2)) + "GB")
  
  def Memory_Usage():
    response = requests.get(PROMETHEUS + '/api/v1/query',
      params={ 
        # 'query': f"{node_memory_Usage_bytes}"
        'query': f"{memory_usage()}"
      })
    results = response.json()['data']['result']
    for result in results:
      memory_usage = '{value[1]}'.format(**result)
    return print("Memory Usage: " + str(round(int(memory_usage)/pow(10,9),2)) + "GB")

  def Cpu_Usage(): 
    response = requests.get(PROMETHEUS + '/api/v1/query',
      params={
      #  'query': f"{node_cpu_Usage_bytes}"
        'query': f"{cpu_usage()}"
      })
    results = response.json()['data']['result']
    for result in results:
      cpu = '{value[1]}'.format(**result)
    return 100-(float(cpu)*100)
