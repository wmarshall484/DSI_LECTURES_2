
class Camera(object):
    '''
    This class knows how to grab images from a webcam.
    '''

    def __init__(self, input_port=None):
        '''
        Creates a new camera object. If input_port is not
        None, the camera is opened on the given port.
        '''
        if input_port is not None:
            self.open(input_port)

    def open(self, input_port):
        '''
        Opens the camera on the given port in preparation
        from capturing frames.
        '''
        pass # TODO

    def close(self):
        '''
        Closes the camera. You can open on a new port next,
        if you'd like.
        '''
        pass # TODO

    def capture(self):
        '''
        Captures and returns a single frame from the open
        camera.
        '''
        pass # TODO


class Arm(object):
    '''
    This class knows how to move, grasp and release the arm.
    '''

    def __init__(self, ctl_port=None):
        '''
        Creates a new arm object. If ctl_port is not
        None, the arm is opened on the given port.
        '''
        if ctl_port is not None:
            self.open(ctl_port)

    def open(self, ctl_port):
        '''
        Opens the arm on the given port in preparation
        from controlling it.
        '''
        pass # TODO

    def close(self):
        '''
        Closes the arm. You can open on a new port next,
        if you'd like.
        '''
        pass # TODO

    def move_to(self, location):
        '''
        Moves the arm to the given location.
        '''
        pass # TODO

    def grasp(self):
        '''
        Grasps the hand of the arm.
        '''
        pass # TODO

    def release(self):
        '''
        Releases the hand of the arm.
        '''
        pass # TODO
