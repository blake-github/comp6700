import rubik.model.constants
from rubik.model.cube import Cube
from rubik.model.constants import *
from rubik.model.cube import Cube
from rubik.controller.upFaceSurface import checkIfUpFaceSurface
from rubik.model.cube import Cube
from rubik.view.rotate import rotate
import rubik.model.cube as cube

def solveUpperLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the entire upper layer is solved.
        
        input:  an instance of the cube class with up-face surface solved
        output: the rotations required to solve the upper layer  
    '''  
    rotationsDone = ''
    cubeString = theCube.get()
    if (checkIfSolved(cubeString)):
        return rotationsDone
    
    if (checkIfUpFaceSurface(cubeString) == False):
        return "Up face failed"
    
    cubeString, rotationsDone = _doUpperLayer(cubeString, rotationsDone)
    return rotationsDone


def _doUpperLayer(cubeString, rotationsDone):
    while (checkIfCorners(cubeString) == False):
        cubeString, rotationsDone, faceValue = _matchingCornersAlign(cubeString, rotationsDone)
        if (faceValue == LMM):
            cubeString, rotationsDone = _doCornerRotationsLeft(cubeString, rotationsDone)
        if (faceValue == RMM):
            cubeString, rotationsDone = _doCornerRotationsRight(cubeString, rotationsDone)
        if (faceValue == BMM):
            cubeString, rotationsDone = _doCornerRotationsBack(cubeString, rotationsDone)
        if (faceValue == FMM):
            cubeString, rotationsDone = _doCornerRotationsFront(cubeString, rotationsDone)
    alignment = _findSolvedFace(cubeString)
    if (alignment == BMM):
        cubeString, rotationsDone = _doFinalRotationBack(cubeString, rotationsDone)
    if (alignment == RMM):
        cubeString, rotationsDone = _doFinalRotationRight(cubeString, rotationsDone)
    if (alignment == LMM):
        cubeString, rotationsDone = _doFinalRotationLeft(cubeString, rotationsDone)
    if (alignment == FMM):
        cubeString, rotationsDone = _doFinalRotationFront(cubeString, rotationsDone)
    if (checkIfSolved(cubeString) == False):
        return _doUpperLayer(cubeString, rotationsDone)
    return cubeString, rotationsDone


def _matchingCornersAlign(cubeString, rotationsDone):
    faceValue = LMM
    cubeString, rotationsDone, faceValue = _firstStepMatch(cubeString, rotationsDone, faceValue)
    cubeString, rotationsDone, faceValue = _secondStepMatch(cubeString, rotationsDone, faceValue)
    cubeString, rotationsDone, faceValue = _thirdStepMatch(cubeString, rotationsDone, faceValue)
    cubeString, rotationsDone, faceValue = _fourthStepMatch(cubeString, rotationsDone, faceValue)
    return cubeString, rotationsDone, faceValue

def _firstStepMatch(cubeString, rotationsDone, faceValue):
    if (cubeString[BTL] == cubeString[BTR] == cubeString[BMM]):
        faceValue = BMM
        return cubeString, rotationsDone, faceValue
    if (cubeString[BTL] == cubeString[BTR] == cubeString[RMM]):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        faceValue = RMM
        return cubeString, rotationsDone, faceValue
    if (cubeString[BTL] == cubeString[BTR] == cubeString[FMM]):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        faceValue = FMM
        return cubeString, rotationsDone, faceValue
    if (cubeString[BTL] == cubeString[BTR] == cubeString[LMM]):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        faceValue = LMM
        return cubeString, rotationsDone, faceValue
    return cubeString, rotationsDone, faceValue

def _secondStepMatch(cubeString, rotationsDone, faceValue):
    if (cubeString[RTL] == cubeString[RTR] == cubeString[RMM]):
        faceValue = RMM
        return cubeString, rotationsDone, faceValue
    if (cubeString[RTL] == cubeString[RTR] == cubeString[FMM]):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        faceValue = FMM
        return cubeString, rotationsDone, faceValue
    if (cubeString[RTL] == cubeString[RTR] == cubeString[LMM]):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        faceValue = LMM
        return cubeString, rotationsDone, faceValue
    if (cubeString[RTL] == cubeString[RTR] == cubeString[BMM]):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        faceValue = BMM
        return cubeString, rotationsDone, faceValue
    return cubeString, rotationsDone, faceValue

def _thirdStepMatch(cubeString, rotationsDone, faceValue):
    if (cubeString[FTL] == cubeString[FTR] == cubeString[FMM]):
        faceValue = FMM
        return cubeString, rotationsDone, faceValue
    if (cubeString[FTL] == cubeString[FTR] == cubeString[LMM]):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        faceValue = LMM
        return cubeString, rotationsDone, faceValue
    if (cubeString[FTL] == cubeString[FTR] == cubeString[BMM]):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        faceValue = BMM
        return cubeString, rotationsDone, faceValue
    if (cubeString[FTL] == cubeString[FTR] == cubeString[RMM]):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        faceValue = RMM
        return cubeString, rotationsDone, faceValue
    return cubeString, rotationsDone, faceValue

def _fourthStepMatch(cubeString, rotationsDone, faceValue):
    if (cubeString[LTL] == cubeString[LTR] == cubeString[LMM]):
        faceValue = LMM
        return cubeString, rotationsDone, faceValue
    if (cubeString[LTL] == cubeString[LTR] == cubeString[BMM]):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        faceValue = BMM
        return cubeString, rotationsDone, faceValue
    if (cubeString[LTL] == cubeString[LTR] == cubeString[RMM]):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        faceValue = RMM
        return cubeString, rotationsDone, faceValue
    if (cubeString[LTL] == cubeString[LTR] == cubeString[FMM]):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        faceValue = FMM
        return cubeString, rotationsDone, faceValue
    return cubeString, rotationsDone, faceValue

def _findSolvedFace(cubeString):
    alignment = BMM
    if (cubeString[BMM] == cubeString[BTM] == cubeString[BMR] == cubeString[BML] 
        == cubeString[BBM] == cubeString[BTL] == cubeString[BTR] == cubeString[BBL]
        == cubeString[BBR]):
        alignment = BMM
        return alignment
    if (cubeString[RMM] == cubeString[RTM] == cubeString[RMR] == cubeString[RML] 
        == cubeString[RBM] == cubeString[RTL] == cubeString[RTR] == cubeString[RBL]
        == cubeString[RBR]):
        alignment = RMM
        return alignment
    if (cubeString[LMM] == cubeString[LTM] == cubeString[LMR] == cubeString[LML] 
        == cubeString[LBM] == cubeString[LTL] == cubeString[LTR] == cubeString[LBL]
        == cubeString[LBR]):
        alignment = LMM
        return alignment
    if (cubeString[FMM] == cubeString[FTM] == cubeString[FMR] == cubeString[FML] 
        == cubeString[FBM] == cubeString[FTL] == cubeString[FTR] == cubeString[FBL]
        == cubeString[FBR]):
        alignment = FMM
        return alignment
    return alignment

def _doCornerRotationsLeft(cubeString, rotationsDone):
    parms = {}
    parms['cube'] = cubeString
    parms['dir'] = 'lURuLUrRUrURUUr'
    postRotate = rotate(parms)
    cubeString = postRotate.get('cube')
    rotationsDone += 'lURuLUrRUrURUUr'
    return cubeString, rotationsDone

def _doCornerRotationsBack(cubeString, rotationsDone):
    parms = {}
    parms['cube'] = cubeString
    parms['dir'] = 'bUFuBUfFUfUFUUf'
    postRotate = rotate(parms)
    cubeString = postRotate.get('cube')
    rotationsDone += 'bUFuBUfFUfUFUUf'
    return cubeString, rotationsDone

def _doCornerRotationsRight(cubeString, rotationsDone):
    parms = {}
    parms['cube'] = cubeString
    parms['dir'] = 'rULuRUlLUlULUUl'
    postRotate = rotate(parms)
    cubeString = postRotate.get('cube')
    rotationsDone += 'rULuRUlLUlULUUl'
    return cubeString, rotationsDone

def _doCornerRotationsFront(cubeString, rotationsDone):
    parms = {}
    parms['cube'] = cubeString
    parms['dir'] = 'fUBuFUbBUbUBUUb'
    postRotate = rotate(parms)
    cubeString = postRotate.get('cube')
    rotationsDone += 'fUBuFUbBUbUBUUb'
    return cubeString, rotationsDone

def _doFinalRotationBack(cubeString, rotationsDone):
    parms = {}
    parms['cube'] = cubeString
    parms['dir'] = 'FFUrLFFlRUFF'
    postRotate = rotate(parms)
    cubeString = postRotate.get('cube')
    rotationsDone += 'FFUrLFFlRUFF'
    return cubeString, rotationsDone

def _doFinalRotationRight(cubeString, rotationsDone):
    parms = {}
    parms['cube'] = cubeString
    parms['dir'] = 'LLUfBLLbFULL'
    postRotate = rotate(parms)
    cubeString = postRotate.get('cube')
    rotationsDone += 'LLUfBLLbFULL'
    return cubeString, rotationsDone

def _doFinalRotationLeft(cubeString, rotationsDone):
    parms = {}
    parms['cube'] = cubeString
    parms['dir'] = 'RRUbFRRfBURR'
    postRotate = rotate(parms)
    cubeString = postRotate.get('cube')
    rotationsDone += 'RRUbFRRfBURR'
    return cubeString, rotationsDone

def _doFinalRotationFront(cubeString, rotationsDone):
    parms = {}
    parms['cube'] = cubeString
    parms['dir'] = 'BBUlRBBrLUBB'
    postRotate = rotate(parms)
    cubeString = postRotate.get('cube')
    rotationsDone += 'BBUlRBBrLUBB'
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

def checkIfCorners(cubeString):
    if (cubeString[FTR] == cubeString[FTL] == cubeString[FMM]
        and cubeString[RTR] == cubeString[RTL] == cubeString[RMM]
        and cubeString[LTR] == cubeString[LTL] == cubeString[LMM]
        and cubeString[BTR] == cubeString[BTL] == cubeString[BMM]):
        return True
    return False

def _getFrontString(cubeString):
    frontString = (cubeString[FTL] + cubeString[FTM] + cubeString[FTR]
                + cubeString[FML] + cubeString[FMM] + cubeString[FMR]
                + cubeString[FBL] + cubeString[FBM] + cubeString[FBR])
    return frontString

def _getRightString(cubeString):
    rightString = (cubeString[RTL] + cubeString[RTM] + cubeString[RTR]
                + cubeString[RML] + cubeString[RMM] + cubeString[RMR]
                + cubeString[RBL] + cubeString[RBM] + cubeString[RBR])
    return rightString

def _getBackString(cubeString):
    backString = (cubeString[BTL] + cubeString[BTM] + cubeString[BTR]
                + cubeString[BML] + cubeString[BMM] + cubeString[BMR]
                + cubeString[BBL] + cubeString[BBM] + cubeString[BBR])
    return backString

def _getLeftString(cubeString):
    leftString = (cubeString[LTL] + cubeString[LTM] + cubeString[LTR]
                + cubeString[LML] + cubeString[LMM] + cubeString[LMR]
                + cubeString[LBL] + cubeString[LBM] + cubeString[LBR])
    return leftString

def _getUpString(cubeString):
    upString = (cubeString[UTL] + cubeString[UTM] + cubeString[UTR]
                + cubeString[UML] + cubeString[UMM] + cubeString[UMR]
                + cubeString[UBL] + cubeString[UBM] + cubeString[UBR])
    return upString

def _getDownString(cubeString):
    downString = (cubeString[DTL] + cubeString[DTM] + cubeString[DTR]
                + cubeString[DML] + cubeString[DMM] + cubeString[DMR]
                + cubeString[DBL] + cubeString[DBM] + cubeString[DBR])
    return downString


def checkIfSolved(cubeString):
    frontStarter = cubeString[FTL]
    rightStarter = cubeString[RTL]
    backStarter = cubeString[BTL]
    leftStarter = cubeString[LTL]
    upStarter = cubeString[UTL]
    downStarter = cubeString[DTL]
    
    frontString = _getFrontString(cubeString)
    
    rightString = _getRightString(cubeString)
    
    backString = _getBackString(cubeString)
    
    leftString = _getLeftString(cubeString)
    
    upString = _getUpString(cubeString)
    
    downString = _getDownString(cubeString)
    
    if (all(ch == frontStarter for ch in frontString) and all(ch == rightStarter for ch in rightString)
        and all(ch == backStarter for ch in backString) and all(ch == leftStarter for ch in leftString)
        and all(ch == upStarter for ch in upString) and all(ch == downStarter for ch in downString)):
        return True
    return False

