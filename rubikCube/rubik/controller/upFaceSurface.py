from rubik.model.constants import *
from rubik.model.cube import Cube
from rubik.controller.upFaceCross import checkIfUpFaceCross
from rubik.model.cube import Cube
from rubik.view.rotate import rotate
import rubik.model.cube as cube



def solveUpSurface(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the up face is solved.
        
        input:  an instance of the cube class with up-face cross solved
        output: the rotations required to solve the up surface  
    '''  
    rotationsDone = ''
    cubeString = theCube.get()
    if (checkIfUpFaceSurface(cubeString)):
        return rotationsDone
    
    if (checkIfUpFaceCross(cubeString) == False):
        return "Up cross failed"
    
    cubeString, rotationsDone = _doUpFaceSurface(cubeString, rotationsDone)
    return rotationsDone

def _doUpFaceSurface(cubeString, rotationsDone):
    cubeString, rotationsDone, wasFish = _checkIfFishAndFix(cubeString, rotationsDone)
    if (wasFish == False):
        cubeString, rotationsDone = _alignTopLeftCorner(cubeString, rotationsDone)
        cubeString, rotationsDone = _doEightStepRotation(cubeString, rotationsDone)
    if (wasFish == True):
        cubeString, rotationsDone = _doEightStepRotation(cubeString, rotationsDone)
    if (checkIfUpFaceSurface(cubeString) == False):
        return _doUpFaceSurface(cubeString, rotationsDone)
    return cubeString, rotationsDone

def _checkIfFishAndFix(cubeString, rotationsDone):
    wasFish = False
    topColor = cubeString[UMM]
    if (checkIfUpFaceCross(cubeString) and topColor == cubeString[UTL] 
        and topColor != cubeString[UTR] and topColor != cubeString[UBL]
        and topColor != cubeString[UBR]):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        wasFish = True
        return cubeString, rotationsDone, wasFish
    if (checkIfUpFaceCross(cubeString) and topColor == cubeString[UTR] 
        and topColor != cubeString[UTL] and topColor != cubeString[UBL]
        and topColor != cubeString[UBR]):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        wasFish = True
        return cubeString, rotationsDone, wasFish
    if (checkIfUpFaceCross(cubeString) and topColor == cubeString[UBL] 
        and topColor != cubeString[UTL] and topColor != cubeString[UTR]
        and topColor != cubeString[UBR]):
        wasFish = True
        return cubeString, rotationsDone, wasFish
    if (checkIfUpFaceCross(cubeString) and topColor == cubeString[UBR] 
        and topColor != cubeString[UTL] and topColor != cubeString[UTR]
        and topColor != cubeString[UBL]):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        wasFish = True
        return cubeString, rotationsDone, wasFish
    return cubeString, rotationsDone, wasFish

def _alignTopLeftCorner(cubeString, rotationsDone):
    upperLeft = cubeString[LTR]
    topColor = cubeString[UMM]
    if (topColor == upperLeft):
        return cubeString, rotationsDone
    if (topColor == cubeString[FTR]):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        return cubeString, rotationsDone
    if (topColor == cubeString[RTR]):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        return cubeString, rotationsDone
    if (topColor == cubeString[BTR]):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        return cubeString, rotationsDone
    return cubeString, rotationsDone

def _doEightStepRotation(cubeString, rotationsDone):
    #RUrURUUr
    parms = {}
    parms['cube'] = cubeString
    parms['dir'] = 'RUrURUUr'
    postRotate = rotate(parms)
    cubeString = postRotate.get('cube')
    rotationsDone += 'RUrURUUr'
    return cubeString, rotationsDone

def _doAndTrackURotate(cubeString, rotationsDone):
    parms = {}
    parms['cube'] = cubeString
    parms['dir'] = 'U'
    postRotate = rotate(parms)
    cubeString = postRotate.get('cube')
    rotationsDone += 'U'
    return cubeString, rotationsDone

def _doAndTrackuRotate(cubeString, rotationsDone):
    parms = {}
    parms['cube'] = cubeString
    parms['dir'] = 'u'
    postRotate = rotate(parms)
    cubeString = postRotate.get('cube')
    rotationsDone += 'u'
    return cubeString, rotationsDone


def checkIfUpFaceSurface(cubeString):
    if (cubeString[UMM] == cubeString[UTM] == cubeString[UMR] == cubeString[UML] 
        == cubeString[UBM] == cubeString[UTL] == cubeString[UTR] == cubeString[UBL]
        == cubeString[UBR]):
        return True
    return False
