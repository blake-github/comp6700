from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import Cube
from rubik.model.constants import *
from rubik.view.rotate import rotate
import hashlib
import random

def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    
    if 'cube' not in parms.keys():
        result['status'] = 'error: missing cube key'
        return result
    if len(parms.keys()) != 1:
        result['status'] = 'error: too many keys'
        return result
     
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    cubeString = theCube.get()
    if theCube.get().find('error') != -1:
        result['status'] = theCube.get()
        return result
    if checkIfSolved(theCube.get()):
        result['solution'] = ''
        result['status'] = 'ok'
        result['integrity'] = _getIntegrity(cubeString, '')
        return result
    
    rotations = ""
    try:
        rotations += solveBottomCross(theCube)      #iteration 2
        if (rotations != ''):
            theCube = _updateCube(cubeString, rotations)
        
        rotations += solveBottomLayer(theCube)      #iteration 3
        if (rotations != ''):
            theCube = _updateCube(cubeString, rotations)
            
        rotations += solveMiddleLayer(theCube)      #iteration 4
        if (rotations != ''):
            theCube = _updateCube(cubeString, rotations)
        rotations += solveUpCross(theCube)          #iteration 5
        if (rotations != ''):
            theCube = _updateCube(cubeString, rotations)
            
        rotations += solveUpSurface(theCube)        #iteration 5
        if (rotations != ''):
            theCube = _updateCube(cubeString, rotations)
            
        rotations += solveUpperLayer(theCube)       #iteration 6
        if (rotations != ''):
            theCube = _updateCube(cubeString, rotations)
    except:
        result['status'] = 'error: unsolvable cube'
        return result
    
    result['solution'] = rotations
    result['status'] = 'ok'    
    result['integrity'] = _getIntegrity(cubeString, rotations)                    #iteration 3
                     
    return result

def _getIntegrity(cubeString, rotations):
    subString = ''
    subLength = 8
    itemToTokenize = cubeString + rotations + 'bmm0066'
    sha256Hash = hashlib.sha256()
    sha256Hash.update(itemToTokenize.encode())
    fullToken = sha256Hash.hexdigest()
    fullLength = len(fullToken)
    randomStart = random.randrange(0, fullLength - subLength - 1)
    subString = fullToken[randomStart:(randomStart + subLength)]
    return subString

def _updateCube(cubeString, rotations):
    parms = {}
    parms['cube'] = cubeString
    parms['dir'] = rotations
    postRotate = rotate(parms)
    cubeString = postRotate.get('cube')
    theCube = Cube(cubeString)
    return theCube


def checkIfSolved(cubeString):
    frontStarter = cubeString[FTL]
    rightStarter = cubeString[RTL]
    backStarter = cubeString[BTL]
    leftStarter = cubeString[LTL]
    upStarter = cubeString[UTL]
    downStarter = cubeString[DTL]
    
    frontString = (cubeString[FTL] + cubeString[FTM] + cubeString[FTR]
                + cubeString[FML] + cubeString[FMM] + cubeString[FMR]
                + cubeString[FBL] + cubeString[FBM] + cubeString[FBR])
    
    rightString = (cubeString[RTL] + cubeString[RTM] + cubeString[RTR]
                + cubeString[RML] + cubeString[RMM] + cubeString[RMR]
                + cubeString[RBL] + cubeString[RBM] + cubeString[RBR])
    
    backString = (cubeString[BTL] + cubeString[BTM] + cubeString[BTR]
                + cubeString[BML] + cubeString[BMM] + cubeString[BMR]
                + cubeString[BBL] + cubeString[BBM] + cubeString[BBR])
    
    leftString = (cubeString[LTL] + cubeString[LTM] + cubeString[LTR]
                + cubeString[LML] + cubeString[LMM] + cubeString[LMR]
                + cubeString[LBL] + cubeString[LBM] + cubeString[LBR])
    
    upString = (cubeString[UTL] + cubeString[UTM] + cubeString[UTR]
                + cubeString[UML] + cubeString[UMM] + cubeString[UMR]
                + cubeString[UBL] + cubeString[UBM] + cubeString[UBR])
    
    downString = (cubeString[DTL] + cubeString[DTM] + cubeString[DTR]
                + cubeString[DML] + cubeString[DMM] + cubeString[DMR]
                + cubeString[DBL] + cubeString[DBM] + cubeString[DBR])
    
    if (all(ch == frontStarter for ch in frontString) and all(ch == rightStarter for ch in rightString)
        and all(ch == backStarter for ch in backString) and all(ch == leftStarter for ch in leftString)
        and all(ch == upStarter for ch in upString) and all(ch == downStarter for ch in downString)):
        return True
    return False