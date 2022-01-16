import logging

logger = logging.getLogger(__name__)

def likes(names: list) -> str:
    if not isinstance(names, list):
        raise ValueError(f'names: must be list')

    likeString = ''
    suffix = 'likes this'
    suffixMult = 'like this'
    nameLength = len(names)
    if nameLength == 0:
        return f'no one {suffix}'
    elif nameLength == 1:
        return f'{names[0]} {suffix}'
    elif nameLength == 2:
        return f'{names[0]} and {names[1]} {suffixMult}'
    elif nameLength == 3:
        return f'{names[0]}, {names[1]} and {names[2]} {suffixMult}'
    else:
        return f'{names[0]}, {names[1]} and {nameLength - 2} others {suffixMult}'
