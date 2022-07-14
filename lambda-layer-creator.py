import os
import subprocess
import shutil
import sys

pythonVersion = 'python3.8'
dependency = 'requests'
layerBaseFolder = 'lambda-layer'
layerFullPath = f'{layerBaseFolder}/python/lib/{pythonVersion}/site-packages'

if os.path.isdir(layerBaseFolder):
    shutil.rmtree(layerBaseFolder)

os.makedirs(layerFullPath)
subprocess.check_call([sys.executable, '-m', 'pip', 'install', dependency, '--target', layerFullPath])
shutil.make_archive(layerBaseFolder, 'zip', layerBaseFolder)