import os
import time

amor_agosto = os.environ.get("AMOR_AGOSTO")
amor_diciembre = os.environ.get("AMOR_DICIEMBRE")

print("*"*20)
for _ in range(5):
    print(f"A la persona que me hinoptizo en DICIEMBRE fue: {amor_diciembre}")
print("*"*20)
for _ in range(5):
    print(f"A la persona que me hinoptizo en AGOSTO fue: {amor_agosto}")
