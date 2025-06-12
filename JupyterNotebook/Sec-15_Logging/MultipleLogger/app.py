import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

Logger=logging.getLogger("ArithmethicApp")

def add(a,b):
    result=a+b
    Logger.debug(f"Addition of {a}+{b}={result}")
    return result

def subtract(a,b):
    result=a-b
    Logger.debug(f"Subtraction of {a}-{b}={result}")
    return result

def multiply(a,b):
    result=a*b
    Logger.debug(f"Multiplcation of {a}*{b}={result}")
    return result

def divide(a,b):
    try:
        result=a/b
        Logger.debug(f"Addition of {a}/{b}={result}")
        return result
    except ZeroDivisionError:
        Logger.error("Division by Zero Error")
        return None

add(10,15)
subtract(10,15)
multiply(10,15)
divide(10,0)
print()