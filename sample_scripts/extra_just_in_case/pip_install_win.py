import pip
import pip._internal

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', "-t", "libs\\python3.7\\site-packages", package])

install("numpy")
