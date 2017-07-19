import decisions


class Controller(object):
    '''
    This class implements the high-level logic of the
    Smart Sorting Robot. It captures frames from the camera,
    delegates to the decision module to classify each piece
    of trash, and then directs the arm to put the trash
    into the correct trash bin.
    '''

    def __init__(self, decisionModule, camera, arm):
        '''
        This init method is very simple. It only stores
        references to the objects that we need.

        It's important that we only store references here
        and NOT create new objects here. Why? We'll see why
        when we test this class. :)
        '''
        self.decisionModule = decisionModule
        self.camera = camera
        self.arm = arm

    def loop_once(self):
        '''
        This method performs one detection/action cycle.
        '''
        frame = self.camera.capture()
        decision = self.decisionModule.process(frame)

        if decision == decisions.RECYCLE:
            self._run_path_to_bin(-12.5)

        elif decision == decisions.COMPOST:
            self._run_path_to_bin(1.5)

        else:  # <-- must be decisions.LANDFILL, right?
            self._run_path_to_bin(15.5)

    def _run_path_to_bin(self, bin_x_location):
        '''
        This method grasps the trash, move it to
        the correct bin, release it, and then moves
        back to its idle position.
        '''
        self.arm.move_to((0, 0, 5))
        self.arm.release()
        self.arm.move_to((0, 0, 0))
        self.arm.grasp()
        self.arm.move_to((0, 0, 5))
        self.arm.move_to((bin_x_location, 0, 5))
        self.arm.release()
        self.arm.move_to((0, 0, 5))
