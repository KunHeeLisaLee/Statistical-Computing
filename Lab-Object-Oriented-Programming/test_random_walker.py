from random_walker_module import RandomWalker, ModifiedRandomWalker

"""Exceptions"""


class ConvergenceError(Exception):
    pass


try:
    raise ConvergenceError("My algorithm failed to converge.")
except ConvergenceError as err:
    print(err)


"""Unit tests for RandomWalker()"""
# Test initialization

def test_init():
    walker = RandomWalker()
    assert walker.get_x_pos() == 0
    assert walker.get_y_pos() == 0

# Test step(): whether it has walked


def test_step():
    walker = RandomWalker()
    walker.step()
    assert walker.get_x_pos() != 0
    assert walker.get_y_pos() != 0

# Test multiple steps


def test_total_steps():
    walker = RandomWalker()
    for _ in range(500):
        walker.step()
        assert walker.get_x_pos() != 0
        assert walker.get_y_pos() != 0


"""Unit tests for ModifiedRandomWalker()"""
# Test initialization


def test_modi_init():
    walker = ModifiedRandomWalker()
    assert walker.get_x_pos() == 0
    assert walker.get_y_pos() == 0

# Test step(): whether it has found the closest object


def test_modi_step():
    walker0 = RandomWalker()
    walker1 = RandomWalker()
    walker2 = ModifiedRandomWalker()

    walker0.x_pos, walker0.y_pos = 1, 1  # assign coordinates
    walker1.x_pos, walker1.y_pos = 2, 2  # assign coordinates

    walker2.step([walker0, walker1])
    x_pos = walker2.get_x_pos()
    y_pos = walker2.get_y_pos()

    assert (-3 <= x_pos <= 3) and (-3 <= y_pos <= 3)

# Test multiple steps


def test_modi_total_steps():
    walker0 = RandomWalker()
    walker1 = RandomWalker()
    walker2 = ModifiedRandomWalker()

    walker0.x_pos, walker0.y_pos = 1, 1  # assign coordinates
    walker1.x_pos, walker1.y_pos = 2, 2  # assign coordinates

    for _ in range(500):
        walker2.step([walker0, walker1])
        assert walker2.get_x_pos() != 0
        assert walker2.get_y_pos() != 0
