import logging
import sys

from pythonKata.fib import fibx

logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def fibTest(data_fib) -> None:
    assert fibx(data_fib[0]) == data_fib[1]
