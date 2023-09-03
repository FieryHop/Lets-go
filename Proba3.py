import asyncio
import time
import tempfile

import urllib.request

file_tmp = tempfile.TemporaryDirectory()

print('Beginning file download with urllib2...')
url = 'https://gitea.radium.group/radium/project-configuration/archive/master.zip'
with open(file_tmp) as r:
    urllib.request.urlretrieve(url, file_tmp)


print(c)
# async def f1():
#     print('Запуск')
#
#     # file_tmp.write(b"Testing write and read file")
#     # file_tmp.seek(0)
#
#     await file_tmp
#     print('ready')
#
# print(file_tmp)



# async def main():
#     task1 = asyncio.create_task(f1)
#
#     await task1


