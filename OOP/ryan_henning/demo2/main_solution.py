from decisions import DecisionModule
from hardware import Camera, Arm
from controller import Controller


if __name__ == '__main__':

    decisionModule = DecisionModule()

    camera         = Camera("/dev/video0")
    arm            = Arm("/dev/usbtty3")

    controller     = Controller(decisionModule, camera, arm)

    while True:
        controller.loop_once()
