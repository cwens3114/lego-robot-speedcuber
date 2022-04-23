from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math, sys

# functions
def scanOneSide(mColorRotater, mHorRotater, cSensor, savedColors):
    mColorRotater.run_for_degrees(-280, 30)
    savedColors.append(cSensor.get_color())

    mColorRotater.run_for_degrees(100, 30)

    sideColorsIdx = [1, 2, 3, 4]
    for i in sideColorsIdx:
        savedColors.append(cSensor.get_color())
        horizontalRotate(mHorRotater)
        mColorRotater.run_for_degrees(35, 30)

        savedColors.append(cSensor.get_color())
        horizontalRotate(mHorRotater)
        mColorRotater.run_for_degrees(-35, 30)

    mColorRotater.run_for_degrees(180, 30)

# vertical rotate
def verticalRotate(mVerRotater):
    mVerRotater.run_for_degrees(-160, 30)
    mVerRotater.run_for_degrees(160, 30)

# horizontal rotate 180 degrees
def horizontalRotate180(mHorRotater):
    mHorRotater.run_for_degrees(135*4, 30)

# clockwise horizontal rotate 90 degrees
def cwHor90(mHorRotater):
    mHorRotater.run_for_degrees(-135*2, 30)

# unclockwise horizontal rotate 90 degrees
def uwHor90(mHorRotater):
    mHorRotater.run_for_degrees(135*2, 30)

# horizontal rotate 45 degrees
def horizontalRotate(mHorRotater):
    mHorRotater.run_for_degrees(135, 30)

# horizontal rotate -45 degrees
def horizontalRotateNeg(mHorRotater):
    mHorRotater.run_for_degrees(-135, 30)

# move bottom clockwise
def moveClockwise(mHorRotater, mVerRotater):
    mVerRotater.run_for_degrees(-85, 30)
    mHorRotater.run_for_degrees(320, 70)
    mHorRotater.run_for_degrees(-50, 70)
    mVerRotater.run_for_degrees(85, 30)

# move bottom unclockwise
def moveUnclockwise(mHorRotater, mVerRotater):
    mVerRotater.run_for_degrees(-85, 30)
    mHorRotater.run_for_degrees(-320, 70)
    mHorRotater.run_for_degrees(50, 70)
    mVerRotater.run_for_degrees(85, 30)


# scan all sides
def scanAllSides(mHorRotater, mVerRotater, mColorRotater, cSensor):
    savedColors = []
    scanOneSide(mColorRotater, mHorRotater, cSensor, savedColors)
    verticalRotate(mVerRotater)
    scanOneSide(mColorRotater, mHorRotater, cSensor, savedColors)
    verticalRotate(mVerRotater)
    scanOneSide(mColorRotater, mHorRotater, cSensor, savedColors)
    verticalRotate(mVerRotater)
    scanOneSide(mColorRotater, mHorRotater, cSensor, savedColors)
    horizontalRotate(mHorRotater)
    horizontalRotate(mHorRotater)
    verticalRotate(mVerRotater)
    scanOneSide(mColorRotater, mHorRotater, cSensor, savedColors)
    verticalRotate(mVerRotater)
    verticalRotate(mVerRotater)
    scanOneSide(mColorRotater, mHorRotater, cSensor, savedColors)
    horizontalRotateNeg(mHorRotater)
    horizontalRotateNeg(mHorRotater)
    verticalRotate(mVerRotater)
    horizontalRotateNeg(mHorRotater)
    horizontalRotateNeg(mHorRotater)
    return savedColors

def cwR(mHorRotater, mVerRotater):
    cwHor90(mHorRotater)
    verticalRotate(mVerRotater)
    moveClockwise(mHorRotater, mVerRotater)
    horizontalRotate180(mHorRotater)
    verticalRotate(mVerRotater)
    cwHor90(mHorRotater)

def uwR(mHorRotater, mVerRotater):
    cwHor90(mHorRotater)
    verticalRotate(mVerRotater)
    moveUnclockwise(mHorRotater, mVerRotater)
    horizontalRotate180(mHorRotater)
    verticalRotate(mVerRotater)
    cwHor90(mHorRotater)

def cwL(mHorRotater, mVerRotater):
    uwHor90(mHorRotater)
    verticalRotate(mVerRotater)
    moveClockwise(mHorRotater, mVerRotater)
    horizontalRotate180(mHorRotater)
    verticalRotate(mVerRotater)
    uwHor90(mHorRotater)

def uwL2(mHorRotater, mVerRotater):
    uwHor90(mHorRotater)
    verticalRotate(mVerRotater)
    moveUnclockwise(mHorRotater, mVerRotater)
    moveUnclockwise(mHorRotater, mVerRotater)
    horizontalRotate180(mHorRotater)
    verticalRotate(mVerRotater)
    uwHor90(mHorRotater)

def cwL2(mHorRotater, mVerRotater):
    uwHor90(mHorRotater)
    verticalRotate(mVerRotater)
    moveClockwise(mHorRotater, mVerRotater)
    moveClockwise(mHorRotater, mVerRotater)
    horizontalRotate180(mHorRotater)
    verticalRotate(mVerRotater)
    uwHor90(mHorRotater)

def uwL(mHorRotater, mVerRotater):
    uwHor90(mHorRotater)
    verticalRotate(mVerRotater)
    moveUnclockwise(mHorRotater, mVerRotater)
    horizontalRotate180(mHorRotater)
    verticalRotate(mVerRotater)
    uwHor90(mHorRotater)


def cwD(mHorRotater, mVerRotater):
    moveClockwise(mHorRotater, mVerRotater)

def uwD(mHorRotater, mVerRotater):
    moveUnclockwise(mHorRotater, mVerRotater)

def cwU(mHorRotater, mVerRotater):
    verticalRotate(mVerRotater)
    verticalRotate(mVerRotater)
    moveClockwise(mHorRotater, mVerRotater)
    verticalRotate(mVerRotater)
    verticalRotate(mVerRotater)

def uwU(mHorRotater, mVerRotater):
    verticalRotate(mVerRotater)
    verticalRotate(mVerRotater)
    moveUnclockwise(mHorRotater, mVerRotater)
    verticalRotate(mVerRotater)
    verticalRotate(mVerRotater)

def cwF(mHorRotater, mVerRotater):
    verticalRotate(mVerRotater)
    moveClockwise(mHorRotater, mVerRotater)
    horizontalRotate180(mHorRotater)
    verticalRotate(mVerRotater)
    horizontalRotate180(mHorRotater)

def uwF(mHorRotater, mVerRotater):
    verticalRotate(mVerRotater)
    moveUnclockwise(mHorRotater, mVerRotater)
    horizontalRotate180(mHorRotater)
    verticalRotate(mVerRotater)
    horizontalRotate180(mHorRotater)

def cwB(mHorRotater, mVerRotater):
    horizontalRotate180(mHorRotater)
    verticalRotate(mVerRotater)
    moveClockwise(mHorRotater, mVerRotater)
    horizontalRotate180(mHorRotater)
    verticalRotate(mVerRotater)

def uwB(mHorRotater, mVerRotater):
    horizontalRotate180(mHorRotater)
    verticalRotate(mVerRotater)
    moveUnclockwise(mHorRotater, mVerRotater)
    horizontalRotate180(mHorRotater)
    verticalRotate(mVerRotater)

def mix(mHorRotater, mVerRotater):
    cwR(mHorRotater, mVerRotater)
    uwF(mHorRotater, mVerRotater)
    cwD(mHorRotater, mVerRotater)
    cwB(mHorRotater, mVerRotater)
    uwU(mHorRotater, mVerRotater)
    uwL(mHorRotater, mVerRotater)
    cwF(mHorRotater, mVerRotater)
    uwU(mHorRotater, mVerRotater)
    cwD(mHorRotater, mVerRotater)
    uwR(mHorRotater, mVerRotater)
    uwF(mHorRotater, mVerRotater)
    cwL(mHorRotater, mVerRotater)
    cwU(mHorRotater, mVerRotater)
    uwB(mHorRotater, mVerRotater)
    cwD(mHorRotater, mVerRotater)
    cwF(mHorRotater, mVerRotater)
    uwD(mHorRotater, mVerRotater)
    uwL2(mHorRotater, mVerRotater)
    cwU(mHorRotater, mVerRotater)
    cwL(mHorRotater, mVerRotater)
    uwF(mHorRotater, mVerRotater)

def fix(mHorRotater, mVerRotater):
    cwF(mHorRotater, mVerRotater)
    uwL(mHorRotater, mVerRotater)
    uwU(mHorRotater, mVerRotater)
    cwL2(mHorRotater, mVerRotater)
    cwD(mHorRotater, mVerRotater)
    uwF(mHorRotater, mVerRotater)
    uwD(mHorRotater, mVerRotater)
    cwB(mHorRotater, mVerRotater)
    uwU(mHorRotater, mVerRotater)
    uwL(mHorRotater, mVerRotater)
    cwF(mHorRotater, mVerRotater)
    cwR(mHorRotater, mVerRotater)
    uwD(mHorRotater, mVerRotater)
    cwU(mHorRotater, mVerRotater)
    uwF(mHorRotater, mVerRotater)
    cwL(mHorRotater, mVerRotater)
    cwU(mHorRotater, mVerRotater)
    uwB(mHorRotater, mVerRotater)
    uwD(mHorRotater, mVerRotater)
    cwF(mHorRotater, mVerRotater)
    uwR(mHorRotater, mVerRotater)

def final(mHorRotater, mVerRotater):
    mHorRotater.run_for_degrees(135*8, 60)


# END functions

# =========== main ======================

hub = MSHub()
motor_hor_rotater = Motor('E')
motor_ver_rotater = Motor('B')
motor_color_rotater = Motor('C')
color_sensor = ColorSensor('A')

# mix(motor_hor_rotater,motor_ver_rotater)

scannedColors = scanAllSides(motor_hor_rotater,motor_ver_rotater, motor_color_rotater, color_sensor)
print ('Scanned colors, len = ', len(scannedColors), ': ', scannedColors)

fix(motor_hor_rotater,motor_ver_rotater)

final(motor_hor_rotater,motor_ver_rotater)

sys.exit('success')
# =========== END =====================

