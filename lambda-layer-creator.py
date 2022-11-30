import os
import subprocess
import shutil
import sys

def createLambdaLayer(dependencies, pythonVersion=f'python{sys.version_info.major}.{sys.version_info.minor}'):
    layerBaseFolder = 'lambda-layer'
    layerFullPath = f'{layerBaseFolder}/python/lib/{pythonVersion}/site-packages'
    pipInstallCommand = [sys.executable, '-m', 'pip', 'install'] + dependencies + ['--target', layerFullPath]

    # Delete previously created lambda layers
    if os.path.isdir(layerBaseFolder):
        shutil.rmtree(layerBaseFolder)

    os.makedirs(layerFullPath)
    subprocess.check_call(pipInstallCommand)
    shutil.make_archive(layerBaseFolder, 'zip', layerBaseFolder)

def main():
    dependencies = ['requests', 'beautifulsoup4'] # Modify this to whatever dependencies you want in the lambda layer
    createLambdaLayer(dependencies)

if __name__ == '__main__':
    main()