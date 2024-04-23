from rubik.model.constants import *
from rubik.model.cube import Cube
from rubik.controller.bottomLayer import checkIfBottomLayer
from rubik.model.cube import Cube
from rubik.view.rotate import rotate
import rubik.model.cube as cube
from rubik.controller.bottomLayer import _doBottomLayer

def solveMiddleLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the middle layer is solved.
        
        input:  an instance of the cube class with the bottom layer solved
        output: the rotations required to solve the middle layer  
    '''  
    rotationsDone = ''
    cubeString = theCube.get()
    if (checkIfMiddleLayer(cubeString)):
        return rotationsDone
    
    if (checkIfBottomLayer(cubeString) == False):
        return "Bottom layer failed"
    
    cubeString, rotationsDone = _doMiddleLayer(cubeString, rotationsDone)
    return rotationsDone

def _doMiddleLayer(cubeString, rotationsDone):
    cubeString, rotationsDone = _doMiddleLayerFirstStep(cubeString, rotationsDone)
    cubeString, rotationsDone = _doMiddleLayerFinalStep(cubeString, rotationsDone)
    if (checkIfMiddleLayer(cubeString) == False):
        return _doMiddleLayer(cubeString, rotationsDone)
    return cubeString, rotationsDone

def _doMiddleLayerFirstStep(cubeString, rotationsDone):
    duoFront = _findDuoToRotate(cubeString, rotationsDone)
    rotatedTo = -1
    if (duoFront == FTM):
        cubeString, rotationsDone, rotatedTo = _doFTMMatch(cubeString, rotationsDone)
    if (duoFront == RTM):
        cubeString, rotationsDone, rotatedTo = _doRTMMatch(cubeString, rotationsDone)
    if (duoFront == BTM):
        cubeString, rotationsDone, rotatedTo = _doBTMMatch(cubeString, rotationsDone)
    if (duoFront == LTM):
        cubeString, rotationsDone, rotatedTo = _doLTMMatch(cubeString, rotationsDone)
    #After match    
    if (rotatedTo == FMM):
        cubeString, rotationsDone = _doUBMSwitch(cubeString, rotationsDone)
    if (rotatedTo == BMM):
        cubeString, rotationsDone = _doUTMSwitch(cubeString, rotationsDone)
    if (rotatedTo == RMM):
        cubeString, rotationsDone = _doUMRSwitch(cubeString, rotationsDone)
    if (rotatedTo == LMM):
        cubeString, rotationsDone = _doUMLSwitch(cubeString, rotationsDone)
    return cubeString, rotationsDone

def _doMiddleLayerFinalStep(cubeString, rotationsDone):
    if (checkIfMiddleLayer(cubeString) == False 
        and _checkIfAllTop(cubeString, rotationsDone) == True):
        if (cubeString[FMR] != cubeString[FMM]):
            cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, FMM)
            cubeString, rotationsDone = _doBottomLayer(cubeString, rotationsDone)
        if (cubeString[RMR] != cubeString[RMM]):
            cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, RMM)
            cubeString, rotationsDone = _doBottomLayer(cubeString, rotationsDone)
        if (cubeString[BMR] != cubeString[BMM]):
            cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, BMM)
            cubeString, rotationsDone = _doBottomLayer(cubeString, rotationsDone)
        if (cubeString[LMR] != cubeString[LMM]):
            cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, LMM)
            cubeString, rotationsDone = _doBottomLayer(cubeString, rotationsDone)
        return _doMiddleLayer(cubeString, rotationsDone)
    return cubeString, rotationsDone

def _checkIfAllTop(cubeString, rotationsDone):
    if (cubeString[FTM] == cubeString[UMM] or cubeString[UBM] == cubeString[UMM]):
        if (cubeString[RTM] == cubeString[UMM] or cubeString[UMR] == cubeString[UMM]):
            if (cubeString[BTM] == cubeString[UMM] or cubeString[UTM] == cubeString[UMM]):
                if (cubeString[LTM] == cubeString[UMM] or cubeString[UML] == cubeString[UMM]):
                    return True
    return False

def _doUBMSwitch(cubeString, rotationsDone):
    matched = _findMatchingCenter(cubeString, cubeString[UBM])
    if (matched == RMM):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, FMM)
        cubeString, rotationsDone = _doBottomLayer(cubeString, rotationsDone)
    if (matched == LMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, FMM)
        cubeString, rotationsDone = _doBottomLayer(cubeString, rotationsDone)
    return cubeString, rotationsDone

def _doUMRSwitch(cubeString, rotationsDone):
    matched = _findMatchingCenter(cubeString, cubeString[UMR])
    if (matched == BMM):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, RMM)
        cubeString, rotationsDone = _doBottomLayer(cubeString, rotationsDone)
    if (matched == FMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, RMM)
        cubeString, rotationsDone = _doBottomLayer(cubeString, rotationsDone)
    return cubeString, rotationsDone

def _doUMLSwitch(cubeString, rotationsDone):
    matched = _findMatchingCenter(cubeString, cubeString[UML])
    if (matched == FMM):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, LMM)
        cubeString, rotationsDone = _doBottomLayer(cubeString, rotationsDone)
    if (matched == BMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, LMM)
        cubeString, rotationsDone = _doBottomLayer(cubeString, rotationsDone)
    return cubeString, rotationsDone

def _doUTMSwitch(cubeString, rotationsDone):
    matched = _findMatchingCenter(cubeString, cubeString[UTM])
    if (matched == LMM):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, BMM)
        cubeString, rotationsDone = _doBottomLayer(cubeString, rotationsDone)
    if (matched == RMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, BMM)
        cubeString, rotationsDone = _doBottomLayer(cubeString, rotationsDone)
    return cubeString, rotationsDone


def _doFTMMatch(cubeString, rotationsDone):
    rotatedTo = -1
    if(cubeString[FTM] == cubeString[FMM]):
        rotatedTo = FMM
        return cubeString, rotationsDone, rotatedTo
    if(cubeString[FTM] == cubeString[RMM]):
        rotatedTo = RMM
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        return cubeString, rotationsDone, rotatedTo
    if(cubeString[FTM] == cubeString[BMM]):
        rotatedTo = BMM
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        return cubeString, rotationsDone, rotatedTo
    if(cubeString[FTM] == cubeString[LMM]):
        rotatedTo = LMM
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        return cubeString, rotationsDone, rotatedTo
    return cubeString, rotationsDone, rotatedTo

def _doRTMMatch(cubeString, rotationsDone):
    rotatedTo = -1
    if(cubeString[RTM] == cubeString[RMM]):
        rotatedTo = RMM
        return cubeString, rotationsDone, rotatedTo
    if(cubeString[RTM] == cubeString[BMM]):
        rotatedTo = BMM
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        return cubeString, rotationsDone, rotatedTo
    if(cubeString[RTM] == cubeString[LMM]):
        rotatedTo = LMM
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        return cubeString, rotationsDone, rotatedTo
    if(cubeString[RTM] == cubeString[FMM]):
        rotatedTo = FMM
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        return cubeString, rotationsDone, rotatedTo
    return cubeString, rotationsDone, rotatedTo

def _doLTMMatch(cubeString, rotationsDone):
    rotatedTo = -1
    if(cubeString[LTM] == cubeString[LMM]):
        rotatedTo = LMM
        return cubeString, rotationsDone, rotatedTo
    if(cubeString[LTM] == cubeString[FMM]):
        rotatedTo = FMM
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        return cubeString, rotationsDone, rotatedTo
    if(cubeString[LTM] == cubeString[RMM]):
        rotatedTo = RMM
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        return cubeString, rotationsDone, rotatedTo
    if(cubeString[LTM] == cubeString[BMM]):
        rotatedTo = BMM
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        return cubeString, rotationsDone, rotatedTo
    return cubeString, rotationsDone, rotatedTo

def _doBTMMatch(cubeString, rotationsDone):
    rotatedTo = -1
    if(cubeString[BTM] == cubeString[BMM]):
        rotatedTo = BMM
        return cubeString, rotationsDone, rotatedTo
    if(cubeString[BTM] == cubeString[LMM]):
        rotatedTo = LMM
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        return cubeString, rotationsDone, rotatedTo
    if(cubeString[BTM] == cubeString[FMM]):
        rotatedTo = FMM
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        return cubeString, rotationsDone, rotatedTo
    if(cubeString[BTM] == cubeString[RMM]):
        rotatedTo = RMM
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        return cubeString, rotationsDone, rotatedTo
    return cubeString, rotationsDone, rotatedTo

def _findDuoToRotate(cubeString, rotationsDone):
    topColor = cubeString[UMM]
    found = -1
    if (cubeString[UBM] != topColor and cubeString[FTM] != topColor):
        found = FTM
        return found
    if (cubeString[UMR] != topColor and cubeString[RTM] != topColor):
        found = RTM
        return found
    if (cubeString[UTM] != topColor and cubeString[BTM] != topColor):
        found = BTM
        return found
    if (cubeString[UML] != topColor and cubeString[LTM] != topColor):
        found = LTM
        return found
    return found


def _doRightTrigger(cubeString, rotationsDone, midFaceToRotate):
    parms = {}
    if (midFaceToRotate == FMM):
        parms['cube'] = cubeString
        parms['dir'] = 'RUr'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'RUr'
        return cubeString, rotationsDone
    if (midFaceToRotate == RMM):
        parms['cube'] = cubeString
        parms['dir'] = 'BUb'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'BUb'
        return cubeString, rotationsDone
    if (midFaceToRotate == LMM):
        parms['cube'] = cubeString
        parms['dir'] = 'FUf'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'FUf'
        return cubeString, rotationsDone
    if (midFaceToRotate == BMM):
        parms['cube'] = cubeString
        parms['dir'] = 'LUl'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'LUl'
        return cubeString, rotationsDone
    return 'Failed', 'Failed'

def _doLeftTrigger(cubeString, rotationsDone, midFaceToRotate):
    parms = {}
    if (midFaceToRotate == FMM):
        parms['cube'] = cubeString
        parms['dir'] = 'luL'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'luL'
        return cubeString, rotationsDone
    if (midFaceToRotate == RMM):
        parms['cube'] = cubeString
        parms['dir'] = 'fuF'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'fuF'
        return cubeString, rotationsDone
    if (midFaceToRotate == LMM):
        parms['cube'] = cubeString
        parms['dir'] = 'buB'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'buB'
        return cubeString, rotationsDone
    if (midFaceToRotate == BMM):
        parms['cube'] = cubeString
        parms['dir'] = 'ruR'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'ruR'
        return cubeString, rotationsDone
    return 'Failed', 'Failed'

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

def _findMatchingCenter(cubeString, searchColor):
    if (searchColor == cubeString[FMM]):
        return FMM
    if (searchColor == cubeString[RMM]):
        return RMM
    if (searchColor == cubeString[LMM]):
        return LMM
    if (searchColor == cubeString[BMM]):
        return BMM
    return -1

def checkIfMiddleLayer(cubeString):
    if (cubeString[DTL] == cubeString[DTM] == cubeString[DTR] == cubeString[DML] ==
        cubeString[DMM] == cubeString[DMR] == cubeString[DBL] == cubeString[DBM] ==
        cubeString[DBR] and cubeString[FML] == cubeString[FMM] == cubeString[FMR] == cubeString[FBL] ==
        cubeString[FBM] == cubeString[FBR] and cubeString[RML] == cubeString[RMM] == cubeString[RMR] == 
        cubeString[RBL] == cubeString[RBM] == cubeString[RMR] and cubeString[LML] == cubeString[LMM] == 
        cubeString[LMR] == cubeString[LBL] == cubeString[LBM] == cubeString[LBR] and cubeString[BML] == 
        cubeString[BMM] == cubeString[BMR] == cubeString[BBL] == cubeString[BBM] == cubeString[BBR]):
        return True
    return False

