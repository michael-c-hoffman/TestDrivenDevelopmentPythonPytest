# pylint: disable-all
tests = [
    ([], 'no one likes this'),
    (['Peter'], 'Peter likes this'),
    (['Jacob', 'Alex'], 'Jacob and Alex like this'),
    (['Max', 'John', 'Mark'], 'Max, John and Mark like this'),
    (['Alex', 'Jacob', 'Mark', 'Max'], 'Alex, Jacob and 2 others like this'),
]
