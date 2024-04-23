from unittest import TestCase
from rubik.view.solve import solve
from rubik.view.rotate import rotate
from rubik.controller.bottomCross import checkIfBottomCross
from rubik.controller.bottomCross import solveBottomCross
from rubik.model.cube import Cube
 

class bottomCrossTest(TestCase):
    
# bottomCross analysis
#
#    Methods: 
#    solveBottomCross
#        inputs:
#            encodedCube: string, 54 characters, unique 5th 14th 23rd 32nd 41st and 50th chars
#                  6 different chars included, mandatory, unvalidated
#        outputs:
#            Returns string of rotations to take get cube to a bottom cross state
#
#    
#
#
#
#
        
# Happy path

        
# Nominal test
    def testNominalCube(self):
        encodedCube = 'gbbgbbgbbrrorrorrobggbggbggroorooroowwywywwwyyywywyyyw'
        solutionCube = 'gbggbggbgorooroorobgbbgbbgbrorrorroryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        parms = {}
        parms['cube'] = encodedCube
        solution = solveBottomCross(theCube)
        parms['dir'] = solution
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfBottomCross(solvedCube))
        
# Nominal test 2
    def testNominalCube2(self):
        encodedCube = 'EExcccxFbcbcExxEExbbcF7bb7cE7F7ExbcFFxExbE7FF7c7bF7xF7'
        solutionCube = 'gbggbggbgorooroorobgbbgbbgbrorrorroryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        parms = {}
        parms['cube'] = encodedCube
        solution = solveBottomCross(theCube)
        parms['dir'] = solution
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfBottomCross(solvedCube))
        
# Nominal test 3
    def testNominalCube3(self):
        encodedCube = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
        theCube = Cube(encodedCube)
        parms = {}
        parms['cube'] = encodedCube
        solution = solveBottomCross(theCube)
        parms['dir'] = solution
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfBottomCross(solvedCube))
        
# Nominal test 4
    def testNominalCube4(self):
        encodedCube = 'DffrkkkHHHrDArkDDrkHrrHHffrADkDDfkHAHrfAfAAkDrfAAAkfDH'
        solutionCube = 'gbggbggbgorooroorobgbbgbbgbrorrorroryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        parms = {}
        parms['cube'] = encodedCube
        solution = solveBottomCross(theCube)
        parms['dir'] = solution
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfBottomCross(solvedCube))
        
# Nominal test 5
    def testNominalCube5(self):
        encodedCube = 'emmvvqvvqqjqjjmKeKKKmeKKjmjvKmmmqvvqejjqeeKvvjjmeqKeqe'
        solutionCube = 'gbggbggbgorooroorobgbbgbbgbrorrorroryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        parms = {}
        parms['cube'] = encodedCube
        solution = solveBottomCross(theCube)
        parms['dir'] = solution
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfBottomCross(solvedCube))
        
# Nominal test 6
    def testNominalCube6(self):
        encodedCube = 'oo58800j0oyjyjy88j08o5yj0yj58jo50o0yyo850jy585055oj8oy'
        solutionCube = 'gbggbggbgorooroorobgbbgbbgbrorrorroryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        parms = {}
        parms['cube'] = encodedCube
        solution = solveBottomCross(theCube)
        parms['dir'] = solution
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfBottomCross(solvedCube))
        
# Nominal test 7
    def testNominalCube7(self):
        encodedCube = 'wbyrrgrwrowboogbggyowwwwwrwybgbbyyyobrrggobyrgygoyrobo'
                      #FQKrrXrFrHFQHHXQXXKHFFFFFrFKQXQQKKKHQrrXXHQKrXKXHKrHQH
                      # F=w, Q=b, K=y, r=r, X=g, H=o
        solutionCube = 'gbggbggbgorooroorobgbbgbbgbrorrorroryyyyyyyyywwwwwwwww'
        theCube = Cube(encodedCube)
        parms = {}
        parms['cube'] = encodedCube
        solution = solveBottomCross(theCube)
        parms['dir'] = solution
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfBottomCross(solvedCube))
        

