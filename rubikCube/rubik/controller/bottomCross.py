from rubik.model.constants import *
from rubik.view.rotate import rotate
import rubik.model.cube as cube


def solveBottomCross(encodedCube):
    '''
        This is the top-level function  for rotating
        a cube into the down-face cross configuration.
        
        input:  an instance of the cube class
        output: the rotations required to transform the input cube into the down-face cross 
    '''  
    parms = {}
    rotationsDone = ''
    cubeString = encodedCube.get()
    if (checkIfBottomCross(cubeString)):
        return rotationsDone
    
    cubeString, rotationsDone = doUpperPedals(cubeString, rotationsDone)
    cubeString, rotationsDone = doTransferToBottom(cubeString, rotationsDone)
    return rotationsDone
    
    
    
def doUpperPedals(cubeString, rotationsDone):
    failedDo = True
    if (cubeString[UBM] != cubeString[DMM]):
        cubeString, rotationsDone, failedDo = doUpperBottomMatch(cubeString, rotationsDone)
    #    if (failedDo == False):
    #        cubeString, rotationsDone = doAndTrackURotate(cubeString, rotationsDone)
            #return doUpperPedals()
    if (cubeString[UMR] != cubeString[DMM]):
        cubeString, rotationsDone, failedDo = doUpperRightMatch(cubeString, rotationsDone)
    #    if (failedDo == False):
    #        cubeString, rotationsDone = doAndTrackURotate(cubeString, rotationsDone)
            #return doUpperPedals()
    if (cubeString[UML] != cubeString[DMM]):
        cubeString, rotationsDone, failedDo = doUpperLeftMatch(cubeString, rotationsDone)
    #    if (failedDo == False):
    #        cubeString, rotationsDone = doAndTrackURotate(cubeString, rotationsDone)
            #return doUpperPedals()
    if (cubeString[UTM] != cubeString[DMM]):
        cubeString, rotationsDone, failedDo = doUpperTopMatch(cubeString, rotationsDone)
    #    if (failedDo == False):
    #        cubeString, rotationsDone = doAndTrackURotate(cubeString, rotationsDone)
            #return doUpperPedals()
    if (failedDo == False):
            cubeString, rotationsDone = doAndTrackURotate(cubeString, rotationsDone)
    if (checkIfUpperPedals(cubeString, rotationsDone)):
        return cubeString, rotationsDone
    return doUpperPedals(cubeString, rotationsDone)

def doUpperBottomMatch(cubeString, rotationsDone):
    parms = {}
    if (cubeString[LMR] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'F'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'F'
        return cubeString, rotationsDone, True
    if (cubeString[RML] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'f'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'f'
        return cubeString, rotationsDone, True
    if (cubeString[DTM] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'FF'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'FF'
        return cubeString, rotationsDone, True
    #End easies, start complexes
    if (cubeString[FMR] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'uR'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'uR'
        return cubeString, rotationsDone, True
    if (cubeString[FML] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'Ul'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'Ul'
        return cubeString, rotationsDone, True
    if (cubeString[FTM] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'FuR'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'FuR'
        return cubeString, rotationsDone, True
    if (cubeString[FBM] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'FUl'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'FUl'
        return cubeString, rotationsDone, True
    return cubeString, rotationsDone, False
                
def doUpperRightMatch(cubeString, rotationsDone):
    parms = {}
    if (cubeString[FMR] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'R'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'R'
        return cubeString, rotationsDone, True
    if (cubeString[BML] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'r'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'r'
        return cubeString, rotationsDone, True
    if (cubeString[DMR] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'RR'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'RR'
        return cubeString, rotationsDone, True
    #End easies, start complexes
    if (cubeString[RMR] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'uB'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'uB'
        return cubeString, rotationsDone, True
    if (cubeString[RML] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'Uf'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'Uf'
        return cubeString, rotationsDone, True
    if (cubeString[RTM] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'RuR'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'RuR'
        return cubeString, rotationsDone, True
    if (cubeString[RBM] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'RUl'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'RUl'
        return cubeString, rotationsDone, True
    return cubeString, rotationsDone, False
        
def doUpperLeftMatch(cubeString, rotationsDone):
    parms = {}
    if (cubeString[BMR] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'L'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'L'
        return cubeString, rotationsDone, True
    if (cubeString[FML] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'l'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'l'
        return cubeString, rotationsDone, True
    if (cubeString[DML] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'LL'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'LL'
        return cubeString, rotationsDone, True
    #End easies, start complexes
    if (cubeString[LMR] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'uF'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'uF'
        return cubeString, rotationsDone, True
    if (cubeString[LML] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'Ub'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'Ub'
        return cubeString, rotationsDone, True
    if (cubeString[LTM] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'LuF'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'LuF'
        return cubeString, rotationsDone, True
    if (cubeString[LBM] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'LUb'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'LUb'
        return cubeString, rotationsDone, True
    return cubeString, rotationsDone, False
        
def doUpperTopMatch(cubeString, rotationsDone):
    parms = {}
    if (cubeString[RMR] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'B'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'B'
        return cubeString, rotationsDone, True
    if (cubeString[LML] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'b'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'b'
        return cubeString, rotationsDone, True
    if (cubeString[DBM] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'BB'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'BB'
        return cubeString, rotationsDone, True
    #End easies, start complexes
    if (cubeString[BMR] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'uL'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'uL'
        return cubeString, rotationsDone, True
    if (cubeString[BML] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'Ur'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'Ur'
        return cubeString, rotationsDone, True
    if (cubeString[BTM] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'BuL'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'BuL'
        return cubeString, rotationsDone, True
    if (cubeString[BBM] == cubeString[DMM]):
        parms['cube'] = cubeString
        parms['dir'] = 'BUr'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'BUr'
        return cubeString, rotationsDone, True
    return cubeString, rotationsDone, False



def doTransferToBottom(cubeString, rotationsDone):
    if (cubeString[UBM] == cubeString[DMM]):
        cubeString, rotationsDone = doUpperBottomTransfer(cubeString, rotationsDone)
    if (cubeString[UML] == cubeString[DMM]):
        cubeString, rotationsDone = doUpperLeftTransfer(cubeString, rotationsDone)
    if (cubeString[UMR] == cubeString[DMM]):
        cubeString, rotationsDone = doUpperRightTransfer(cubeString, rotationsDone)
    if (cubeString[UTM] == cubeString[DMM]):
        cubeString, rotationsDone = doUpperTopTransfer(cubeString, rotationsDone)
    if (checkIfBottomCross(cubeString)):
        return cubeString, rotationsDone
    return doTransferToBottom(cubeString, rotationsDone)

def doUpperBottomTransfer(cubeString, rotationsDone):
    parms = {}
    matchIndex = findMatchingCenter(cubeString, cubeString[FTM])
    if (matchIndex == FMM):
        parms['cube'] = cubeString
        parms['dir'] = 'FF'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'FF'
        return cubeString, rotationsDone
    if (matchIndex == RMM):
        parms['cube'] = cubeString
        parms['dir'] = 'uRR'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'uRR'
        return cubeString, rotationsDone
    if (matchIndex == BMM):
        parms['cube'] = cubeString
        parms['dir'] = 'uuBB'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'uuBB'
        return cubeString, rotationsDone
    if (matchIndex == LMM):
        parms['cube'] = cubeString
        parms['dir'] = 'ULL'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'ULL'
        return cubeString, rotationsDone
    return cubeString, rotationsDone
    
def doUpperLeftTransfer(cubeString, rotationsDone):
    parms = {}
    matchIndex = findMatchingCenter(cubeString, cubeString[LTM])
    if (matchIndex == FMM):
        parms['cube'] = cubeString
        parms['dir'] = 'uFF'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'uFF'
        return cubeString, rotationsDone
    if (matchIndex == RMM):
        parms['cube'] = cubeString
        parms['dir'] = 'uuRR'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'uuRR'
        return cubeString, rotationsDone
    if (matchIndex == BMM):
        parms['cube'] = cubeString
        parms['dir'] = 'UBB'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'UBB'
        return cubeString, rotationsDone
    if (matchIndex == LMM):
        parms['cube'] = cubeString
        parms['dir'] = 'LL'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'LL'
        return cubeString, rotationsDone
    return cubeString, rotationsDone

def doUpperRightTransfer(cubeString, rotationsDone):
    parms = {}
    matchIndex = findMatchingCenter(cubeString, cubeString[RTM])
    if (matchIndex == FMM):
        parms['cube'] = cubeString
        parms['dir'] = 'UFF'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'UFF'
        return cubeString, rotationsDone
    if (matchIndex == RMM):
        parms['cube'] = cubeString
        parms['dir'] = 'RR'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'RR'
        return cubeString, rotationsDone
    if (matchIndex == BMM):
        parms['cube'] = cubeString
        parms['dir'] = 'uBB'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'uBB'
        return cubeString, rotationsDone
    if (matchIndex == LMM):
        parms['cube'] = cubeString
        parms['dir'] = 'UULL'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'UULL'
        return cubeString, rotationsDone
    return cubeString, rotationsDone

def doUpperTopTransfer(cubeString, rotationsDone):
    parms = {}
    matchIndex = findMatchingCenter(cubeString, cubeString[BTM])
    if (matchIndex == FMM):
        parms['cube'] = cubeString
        parms['dir'] = 'UUFF'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'UUFF'
        return cubeString, rotationsDone
    if (matchIndex == RMM):
        parms['cube'] = cubeString
        parms['dir'] = 'URR'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'URR'
        return cubeString, rotationsDone
    if (matchIndex == BMM):
        parms['cube'] = cubeString
        parms['dir'] = 'BB'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'BB'
        return cubeString, rotationsDone
    if (matchIndex == LMM):
        parms['cube'] = cubeString
        parms['dir'] = 'uLL'
        postRotate = rotate(parms)
        cubeString = postRotate.get('cube')
        rotationsDone += 'uLL'
        return cubeString, rotationsDone
    return cubeString, rotationsDone
    


def findMatchingCenter(cubeString, searchColor):
    if (searchColor == cubeString[FMM]):
        return FMM
    if (searchColor == cubeString[RMM]):
        return RMM
    if (searchColor == cubeString[LMM]):
        return LMM
    if (searchColor == cubeString[BMM]):
        return BMM
    return -1

def doAndTrackURotate(cubeString, rotationsDone):
    parms = {}
    parms['cube'] = cubeString
    parms['dir'] = 'U'
    postRotate = rotate(parms)
    cubeString = postRotate.get('cube')
    rotationsDone += 'U'
    return cubeString, rotationsDone

def checkIfUpperPedals(cubeString, rotationsDone):
    if (cubeString[DMM] == cubeString[UBM] and cubeString[DMM] == cubeString[UMR]
        and cubeString[DMM] == cubeString[UML] and cubeString[DMM] == cubeString[UTM]):
        return True
    return False


def checkIfBottomCross(cubeString):
    if (cubeString[DMM] == cubeString[DTM] == cubeString[DML] == cubeString[DMR] == cubeString[DBM]
        and cubeString[FMM] == cubeString[FBM] and cubeString[RMM] == cubeString[RBM]
        and cubeString[LMM] == cubeString[LBM] and cubeString[BMM] == cubeString[BBM]):
        return True
    return False




