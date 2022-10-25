import psutil
"""
memoryを取得
https://pg-chain.com/python-psutil
"""
mem = psutil.virtual_memory()

print(mem.total)


