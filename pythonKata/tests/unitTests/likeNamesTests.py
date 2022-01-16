import logging
import sys

import pytest

from pythonKata.likeNames import likes

logger = logging.getLogger(__name__)
# logger.addHandler(logging.StreamHandler(sys.stdout))
# logger.setLevel(logging.DEBUG)

def likesNotListTest():
    with pytest.raises(ValueError) as error:
        likes(tuple())

def likesTest(data_likes):
    logger.info(f'names={data_likes[0]} expected={data_likes[1]}')
    assert likes(data_likes[0]) == data_likes[1]
