# knightsTour
Task
Problem: you have a standard 8x8 chessboard, empty but for a single knight on some square. Your task is to emit a series of legal knight moves that result in the knight visiting every square on the chessboard exactly once. Note that it is not a requirement that the tour be "closed"; that is, the knight need not end within a single move of its start position.

Input: starting square
Output: move sequence

All input/output is to use Algebraic Notation.
See https://en.wikipedia.org/wiki/Algebraic_notation_(chess)

## Notes
- [x] Board of 8x8 2d array
- [x] Board coordinate on board
- [x] Check if square available
- [x] Move to square and mark as visited
- [x] Knight current location
- [x] Define knight valid moves (upleft, upright, downleft, downright)
- [x] Negative moves which would wrap around list in python check
- [x] knight list of moves
- [ ] run - Loop through all next moves 
    - [ ] Check if board complete
- [ ] knight backtrack last move and try different path repeat until back to beginning

[Source https://rosettacode.org/wiki/Knight's_tour]
## Setup
```sh
poetry install

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Credits
This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.
