import logging
import sys

import pytest

from stringOrderCheck.stringOrder import checkOrder, orderIndices, orderScan

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)

"""

# input: "hello"
# ordering: 'hlo'
# true


# input: "helloooooh"
# ordering: 'hlo'
# false


# input: "helzzzzzloo"
# ordering: 'hlo'
# true
"""


@pytest.mark.parametrize(
    "inputSource, inputOrder, expected",
    [
        ("helloworld", "hlo!", list()),
        ("helloooooh", "hlo", [0, 9, 2, 3, 4, 5, 6, 7, 8]),
        ("helzzzzzloo", "lzo", [2, 8, 3, 4, 5, 6, 7, 9, 10]),
    ],
)
def orderIndicesTest(inputSource, inputOrder, expected):
    logger.info(f"inputstring={inputSource}")
    logger.info(f"inputOrder={inputOrder}")
    indices = orderIndices(inputSource, inputOrder)
    logger.info(f"indices={indices}")
    assert indices == expected


@pytest.mark.parametrize(
    "inputSource, inputOrder, ,nextchar, expected",
    [
        ("helloorld"[1:], "hlo!", "l", True),
        ("helloooooh"[2:], "hlo", "o", True),
        ("helzzzzzloo!"[-2:], "lo!", "l", False),
    ],
)
def checkOrderTest(inputSource, inputOrder, nextchar, expected):
    logger.info(f"inputSource={inputSource}")
    logger.info(f"nextchar={nextchar}")
    actual = checkOrder(inputSource, inputOrder, nextchar)
    assert actual == expected


@pytest.mark.parametrize(
    "inputSource, inputOrder, expected",
    [
        ("helloorld", "heod", True),
        ("helloooooh", "eo!", False),
        ("hellooo!ooh", "eo!", False),
        ("helzzzzzoo!", "hl!", True),
    ],
)
def orderScanTest(inputSource, inputOrder, expected):
    actual = orderScan(inputSource, inputOrder)
    assert actual == expected
