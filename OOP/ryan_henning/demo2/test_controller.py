# test with command: !nosetests %

import nose.tools as n

from controller import Controller
import decisions


def test_empty_basket():
    '''
    This tests the Controller to make sure that it doesn't move the arm when the basket is empty.
    '''

    class MockDecisionModule(object):
        def process(self, frame):
            return decisions.EMPTY

    class MockCamera(object):
        def capture(self):
            return None

    class MockArm(object):
        def __init__(self):
            self.did_move = False

        def move_to(self, location):
            self.did_move = True

        def release(self):
            self.did_move = True

        def grasp(self):
            self.did_move = True

    decisionModule = MockDecisionModule()
    camera         = MockCamera()
    arm            = MockArm()

    controller = Controller(decisionModule, camera, arm)
    controller.loop_once()
    n.assert_false(arm.did_move)
