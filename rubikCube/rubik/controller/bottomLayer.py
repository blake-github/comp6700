from rubik.model.constants import *
from rubik.view.rotate import rotate
import rubik.model.cube as cube
from rubik.controller.bottomCross import checkIfBottomCross
from rubik.model.cube import Cube

def solveBottomLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the bottom layer is solved.
        
        input:  an instance of the cube class with the down-face cross solved
        output: the rotations required to solve the bottom layer  
    '''  
    rotationsDone = ''
    cubeString = theCube.get()
    if (checkIfBottomLayer(cubeString)):
        return rotationsDone
    
    if (checkIfBottomCross(cubeString) == False):
        return "Bottom cross failed"
    
    cubeString, rotationsDone = _doBottomLayer(cubeString, rotationsDone)
    return rotationsDone

def _doBottomLayer(cubeString, rotationsDone):
    cubeString, rotationsDone = _matchTopColorsAndTrigger(cubeString, rotationsDone)
    cubeString, rotationsDone = _matchBottomColorsAndTrigger(cubeString, rotationsDone)
    if (checkIfBottomLayer(cubeString) == False):
        if (cubeString[UBR] == cubeString[DMM]):
            cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, FMM)
            cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, FMM)
            return _doBottomLayer(cubeString, rotationsDone)
        if (cubeString[UBL] == cubeString[DMM]):
            cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, FMM)
            cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, FMM)
            return _doBottomLayer(cubeString, rotationsDone)
        if (cubeString[UTR] == cubeString[DMM]):
            cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, BMM)
            cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, BMM)
            return _doBottomLayer(cubeString, rotationsDone)
        if (cubeString[UTL] == cubeString[DMM]):
            cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, BMM)
            cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, BMM)
            return _doBottomLayer(cubeString, rotationsDone)
        return _doBottomLayer(cubeString, rotationsDone)
    return cubeString, rotationsDone
    
    
def _matchTopColorsAndTrigger(cubeString, rotationsDone):
    cubeString, rotationsDone = _topRightMatchAndTrigger(cubeString, rotationsDone)
    cubeString, rotationsDone = _topLeftMatchAndTrigger(cubeString, rotationsDone)
    return cubeString, rotationsDone

def _topRightMatchAndTrigger(cubeString, rotationsDone):
    if (cubeString[FTR] == cubeString[DMM]):
        matched = _findMatchingCenter(cubeString, cubeString[RTL])
        cubeString, rotationsDone = _doFTRMatchAndTrigger(cubeString, rotationsDone, matched)
    if (cubeString[RTR] == cubeString[DMM]):
        matched = _findMatchingCenter(cubeString, cubeString[BTL])
        cubeString, rotationsDone = _doRTRMatchAndTrigger(cubeString, rotationsDone, matched)
    if (cubeString[BTR] == cubeString[DMM]):
        matched = _findMatchingCenter(cubeString, cubeString[LTL])
        cubeString, rotationsDone = _doBTRMatchAndTrigger(cubeString, rotationsDone, matched)
    if (cubeString[LTR] == cubeString[DMM]):
        matched = _findMatchingCenter(cubeString, cubeString[FTL])
        cubeString, rotationsDone = _doLTRMatchAndTrigger(cubeString, rotationsDone, matched)
    return cubeString, rotationsDone

def _doFTRMatchAndTrigger(cubeString, rotationsDone, matched):
    if (matched == BMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, BMM)
    elif (matched == LMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, LMM)
    elif (matched == FMM):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, FMM)
    else:
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, RMM)
    return cubeString, rotationsDone

def _doRTRMatchAndTrigger(cubeString, rotationsDone, matched):
    if (matched == LMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, LMM)
    elif (matched == FMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, FMM)
    elif (matched == RMM):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, RMM)
    else:
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, BMM)
    return cubeString, rotationsDone

def _doBTRMatchAndTrigger(cubeString, rotationsDone, matched):
    if (matched == FMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, FMM)
    elif (matched == RMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, RMM)
    elif (matched == BMM):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, BMM)
    else:
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, LMM)
    return cubeString, rotationsDone

def _doLTRMatchAndTrigger(cubeString, rotationsDone, matched):
    if (matched == RMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, RMM)
    elif (matched == BMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, BMM)
    elif (matched == LMM):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, LMM)
    else:
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, FMM)
    return cubeString, rotationsDone

def _topLeftMatchAndTrigger(cubeString, rotationsDone):
    if (cubeString[FTL] == cubeString[DMM]):
        matched = _findMatchingCenter(cubeString, cubeString[LTR])
        cubeString, rotationsDone = _doFTLMatchAndTrigger(cubeString, rotationsDone, matched)
    if (cubeString[LTL] == cubeString[DMM]):
        matched = _findMatchingCenter(cubeString, cubeString[BTR])
        cubeString, rotationsDone = _doLTLMatchAndTrigger(cubeString, rotationsDone, matched)
    if (cubeString[BTL] == cubeString[DMM]):
        matched = _findMatchingCenter(cubeString, cubeString[RTR])
        cubeString, rotationsDone = _doBTLMatchAndTrigger(cubeString, rotationsDone, matched)
    if (cubeString[RTL] == cubeString[DMM]):
        matched = _findMatchingCenter(cubeString, cubeString[FTR])
        cubeString, rotationsDone = _doRTLMatchAndTrigger(cubeString, rotationsDone, matched)
    return cubeString, rotationsDone

def _doFTLMatchAndTrigger(cubeString, rotationsDone, matched):
    if (matched == FMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, FMM)
    elif (matched == RMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, RMM)
    elif (matched == BMM):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, BMM)
    else:
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, LMM)
    return cubeString, rotationsDone

def _doLTLMatchAndTrigger(cubeString, rotationsDone, matched):
    if (matched == LMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, LMM)
    elif (matched == FMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, FMM)
    elif (matched == RMM):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, RMM)
    else:
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, BMM)
    return cubeString, rotationsDone

def _doBTLMatchAndTrigger(cubeString, rotationsDone, matched):
    if (matched == BMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, BMM)
    elif (matched == LMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, LMM)
    elif (matched == FMM):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, FMM)
    else:
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, RMM)
    return cubeString, rotationsDone

def _doRTLMatchAndTrigger(cubeString, rotationsDone, matched):
    if (matched == RMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, RMM)
    elif (matched == BMM):
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doAndTrackuRotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, BMM)
    elif (matched == LMM):
        cubeString, rotationsDone = _doAndTrackURotate(cubeString, rotationsDone)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, LMM)
    else:
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, FMM)
    return cubeString, rotationsDone

def _matchBottomColorsAndTrigger(cubeString, rotationsDone):
    cubeString, rotationsDone = _doubleRights(cubeString, rotationsDone)
    cubeString, rotationsDone = _doubleLefts(cubeString, rotationsDone)
    return cubeString, rotationsDone

def _doubleRights(cubeString, rotationsDone):
    if (cubeString[FBR] == cubeString[DMM]):
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, FMM)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, FMM)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, FMM)
        cubeString, rotationsDone = _topRightMatchAndTrigger(cubeString, rotationsDone)
    if (cubeString[RBR] == cubeString[DMM]):
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, RMM)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, RMM)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, RMM)
        cubeString, rotationsDone = _topRightMatchAndTrigger(cubeString, rotationsDone)
    if (cubeString[BBR] == cubeString[DMM]):
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, BMM)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, BMM)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, BMM)
        cubeString, rotationsDone = _topRightMatchAndTrigger(cubeString, rotationsDone)
    if (cubeString[LBR] == cubeString[DMM]):
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, LMM)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, LMM)
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, LMM)
        cubeString, rotationsDone = _topRightMatchAndTrigger(cubeString, rotationsDone)
    return cubeString, rotationsDone

def _doubleLefts(cubeString, rotationsDone):
    if (cubeString[FBL] == cubeString[DMM]):
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, FMM)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, FMM)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, FMM)
        cubeString, rotationsDone = _topLeftMatchAndTrigger(cubeString, rotationsDone)
    if (cubeString[RBL] == cubeString[DMM]):
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, RMM)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, RMM)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, RMM)
        cubeString, rotationsDone = _topLeftMatchAndTrigger(cubeString, rotationsDone)
    if (cubeString[BBL] == cubeString[DMM]):
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, BMM)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, BMM)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, BMM)
        cubeString, rotationsDone = _topLeftMatchAndTrigger(cubeString, rotationsDone)
    if (cubeString[LBL] == cubeString[DMM]):
        cubeString, rotationsDone = _doLeftTrigger(cubeString, rotationsDone, LMM)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, LMM)
        cubeString, rotationsDone = _doRightTrigger(cubeString, rotationsDone, LMM)
        cubeString, rotationsDone = _topLeftMatchAndTrigger(cubeString, rotationsDone)
    return cubeString, rotationsDone



def _doAndTrackuRotate(cubeString, rotationsDone):
    parms = {}
    parms['cube'] = cubeString
    parms['dir'] = 'u'
    postRotate = rotate(parms)
    cubeString = postRotate.get('cube')
    rotationsDone += 'u'
    return cubeString, rotationsDone

def _doAndTrackURotate(cubeString, rotationsDone):
    parms = {}
    parms['cube'] = cubeString
    parms['dir'] = 'U'
    postRotate = rotate(parms)
    cubeString = postRotate.get('cube')
    rotationsDone += 'U'
    return cubeString, rotationsDone


def checkIfBottomLayer(cubeString):
    if (cubeString[DTL] == cubeString[DTM] == cubeString[DTR] == cubeString[DML] ==
        cubeString[DMM] == cubeString[DMR] == cubeString[DBL] == cubeString[DBM] ==
        cubeString[DBR]):
        return True
    return False

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

