from flasktest.submod import submod

def test_submod():
    assert submod.submod == {'sub': 'mod'}
