from rubik.model.constants import *
from rubik.model.cube import Cube
from rubik.controller.middleLayer import checkIfMiddleLayer
from rubik.model.cube import Cube
from rubik.view.rotate import rotate
import rubik.model.cube as cube

def solveUpCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the up-face cross configuration.
        
        input:  an instance of the cube class with the middle layer solved
        output: the rotations required to solve the up-face cross  
    '''  
    rotationsDone = ''
    cubeString = theCube.get()
    if (checkIfUpFaceCross(cubeString)):
        return rotationsDone
    
    if (checkIfMiddleLayer(cubeString) == False):
        return "Middle layer failed"
    
    cubeString, rotationsDone = _doUpFaceCross(cubeString, rotationsDone)
    return rotationsDone

def _doUpFaceCross(cubeString, rotationsDone):
    wasThree = False
    if (_checkIfWorstCase(cubeString) == True):
        cubeString, rotationsDone = _doSixStepRotation(cubeString, rotationsDone)
    cubeString, rotationsDone, wasThree = _checkThreeAndVert(cubeString, rotationsDone)
    if (wasThree == True):
        cubeString, rotationsDone = _doSixStepRotation(cubeString, rotationsDone)
    cubeString, rotationsDone = _doNineAndTwelveAlign(cubeString, rotationsDone)
    cubeString, rotationsDone = _doSixStepRotation(cubeString, rotationsDone)
    if (checkIfUpFaceCross(cubeString) == False):
        return _doUpFaceCross(cubeString, rotationsDone)
    return cubeString, rotationsDone

def _doSixStepRotation(cubeString, rotationsDone):
    #FURurf
    parms = {}
    parms['cube'] = cubeString
    parms['dir'] = 'FURurf'
    postRotate = rotate(parms)
    cubeString = postRotate.get('cube')
    rotationsDone += 'FURurf'
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

def _checkIfWorstCase(cubeString):
    topMid = cubeString[UMM]
    if (topMid == cubeString[UTM] or topMid == cubeString[UMR] or topMid == cubeString[UML]
        or topMid == cubeString[UBM]):
        return False
    return True

def _checkThreeAndVert(cubeString, rotationsDone):
    wasThree = False
    topMid = cubeString[UMM]
    if (topMid == cubeString[UTM] and topMid == cubeString[UBM]):
        wasThree = True
        return cubeString, rotationsDone, wasThree
    if (topMid == cubeString[UML] and topMid == cubeString[UMR]):
        wasThree = True
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        return cubeString, rotationsDone, wasThree
    return cubeString, rotationsDone, wasThree

def _doNineAndTwelveAlign(cubeString, rotationsDone):
    topMid = cubeString[UMM]
    if (topMid == cubeString[UMR] and topMid == cubeString[UBM]):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        return cubeString, rotationsDone
    if (topMid == cubeString[UML] and topMid == cubeString[UBM]):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        return cubeString, rotationsDone
    if (topMid == cubeString[UTM] and topMid == cubeString[UMR]):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        return cubeString, rotationsDone
    return cubeString, rotationsDone

def checkIfUpFaceCross(cubeString):
    if (cubeString[UTM] == cubeString[UMM] == cubeString[UML] == cubeString[UBM] == cubeString[UMR]):
        return True
    return False

