from unittest import TestCase
from rubik.view.solve import solve
from rubik.view.rotate import rotate
from rubik.controller.bottomLayer import checkIfBottomLayer
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.middleLayer import checkIfMiddleLayer
from rubik.controller.upFaceCross import checkIfUpFaceCross
from rubik.controller.upFaceSurface import checkIfUpFaceSurface
from rubik.controller.upFaceSurface import _doEightStepRotation as doEightStepRotation
from rubik.controller.upFaceSurface import _alignTopLeftCorner as alignTopLeftCorner
from rubik.controller.upFaceSurface import _checkIfFishAndFix as checkIfFishAndFix
from rubik.model.cube import Cube
from rubik.model.constants import *


class middleLayerTest(TestCase):

        
# Happy path

# Solved cube test
    def testSolvedUpFace(self):
        encodedCube = 'grbggggggroooooooobbgbbbbbbogrrrrrrryyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual('', directions)

# Nominal test
    def testNominalCube(self):
        encodedCube = 'gbbgbbgbbrrorrorrobggbggbggroorooroowwywywwwyyywywyyyw'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfUpFaceSurface(solvedCube))
        
# Nominal test 2
    def testNominalCube2(self):
        encodedCube = 'EExcccxFbcbcExxEExbbcF7bb7cE7F7ExbcFFxExbE7FF7c7bF7xF7'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfUpFaceSurface(solvedCube))
        
# Nominal test 3
    def testNominalCube3(self):
        encodedCube = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfUpFaceSurface(solvedCube))
        
# Nominal test 4
    def testNominalCube4(self):
        encodedCube = 'DffrkkkHHHrDArkDDrkHrrHHffrADkDDfkHAHrfAfAAkDrfAAAkfDH'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfUpFaceSurface(solvedCube))
        
# Nominal test 5
    def testNominalCube5(self):
        encodedCube = 'emmvvqvvqqjqjjmKeKKKmeKKjmjvKmmmqvvqejjqeeKvvjjmeqKeqe'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfUpFaceSurface(solvedCube))
        
# Nominal test 6
    def testNominalCube6(self):
        encodedCube = 'oo58800j0oyjyjy88j08o5yj0yj58jo50o0yyo850jy585055oj8oy'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfUpFaceSurface(solvedCube))
        
# Nominal test 7
    def testNominalCube7(self):
        encodedCube = 'ppR2nx2nnxx28xnRR8nn8p82pxR282pp8xR8x2xR2nn8npRpxRp82R'
                       ##ppR2nx2nnxx28xnRR8nn8p82pxR282pp8xR8x2xR2nn8npRpxRp82R
                       ##ggbyroyrrooyworbbwrrwgwygobywyggwobwoyobyrrwrgbgobgwyb
                       ##p-g R-b 2-y n-r x-o 8-w 
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfUpFaceSurface(solvedCube))
        
# Nominal test 8
    def testNominalCube8(self):
        encodedCube = 'hqqhqzeqqzRheehRBhezBeheBBzqBRqRRRRhehzhBzzBeBzBqzeqRR'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfUpFaceSurface(solvedCube))
        
# Nominal test 9
    def testNominalCube9(self):
        encodedCube = 'JspJssxzJJ7sp7pxzz7Jx7Jxpzszs77z7xp7Jxpzpspxzsp7JxJzxs'
                     ##gbygbbroggwbywyroowgrwgryobobwwowrywgryoybyrobywgrgorb
                     ##J-g s-b p-y x-r z-o 7-w 
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfUpFaceSurface(solvedCube))
        
# Nominal test 10
    def testNominalCube10(self):
        encodedCube = 'qz7dwzqwVddz77VzVVqwddzdwqV7Vw7Vzd7zz7Vwdw7Vw7qdqqqwzq'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfUpFaceSurface(solvedCube))
        
# Nominal test 11
    def testNominalCube11(self):
        encodedCube = 'ggbyrbrbbggowooyworrwyborgwbrwbwwggwyyyogobwoyyoryrrbg'
                     ##ff7zv7v77fflQllzQlvvQz7lvfQ7vQ7QQffQzzzlfl7Qlzzlvzvv7f
                     ##f-g 7-b z-y v-r l-o Q-w 
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfUpFaceSurface(solvedCube))
        
# Nominal test 12
    def testNominalCube12(self):
        encodedCube = 'CSCHSCCkVSVHkVCCCHSkSVIHISHHVIIkSkSIkIVIHHkkkVHSVCIICV'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfUpFaceSurface(solvedCube))
        
# Nominal test 13
    def testNominalCube13(self):
        encodedCube = 'Z0ZVGGCGZGGG0CZCC0CGBCVVB00GZVZBBVBG0C0B0BBVBZZV0ZVCCV'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfUpFaceSurface(solvedCube))
        
# Nominal test 14
    def testNominalCube14(self):
        encodedCube = 'DGG6Dww6ODGOOP6PGGDDDDwPwPGOw6D6O6GOPO6PGPGwP6ww6ODwOP'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfUpFaceSurface(solvedCube))
        
# Nominal test 15
    def testNominalCube15(self):
        encodedCube = 'xcclcbqxxxcblq66xxl66bbxqlqlqbb6clclcl6bxxqq6bqb6l6cqc'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfUpFaceSurface(solvedCube))
        
# Nominal test 16
    def testNominalCube16(self):
        encodedCube = 'RMMMMccRJJMJRRRcc8MJ8PcPRcRJJMJJR88Pc8PMPPP88R8Pc8PMJc'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfUpFaceSurface(solvedCube))


# Method tests
# (Not re-doing the doAndTrackURotate methods since they are identical
# to last increment
    
#Up Face Surface Check (True)
    def testCheckIfUpFaceSurface(self):
        encodedCube = 'grbggggggroooooooobbgbbbbbbogrrrrrrryyyyyyyyywwwwwwwww'
        checkValue = checkIfUpFaceSurface(encodedCube)
        self.assertEqual(True, checkValue)
        
#Up Face Surface Check (False)
    def testCheckIfUpFaceSurface2(self):
        encodedCube = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
        checkValue = checkIfUpFaceSurface(encodedCube)
        self.assertEqual(False, checkValue)
        
# Eight step rotation test
# RUrURUUr
    def testDoEightStepRotations(self):
        encodedCube = 'rbbbbgbbgwroyrryrrbywggbggbooywooyoogoygyygyrwrowwwrww'
        rotationsDone = ''
        cubeString, rotationsDone = doEightStepRotation(encodedCube, rotationsDone)
        shouldCube = 'ybobbgbbggoyyrryrrrrwggbggbrybwooyoobygoygoywwrowwwrww'
        self.assertEqual(shouldCube, cubeString)
        
# Eight step rotation test 2
# RUrURUUr
    def testDoEightStepRotations2(self):
        encodedCube = 'oyogbwrrygyrorwbbybwgbgggrorrgyooboywgwgyoybwbwobwrwyr'
        rotationsDone = ''
        cubeString, rotationsDone = doEightStepRotation(encodedCube, rotationsDone)
        shouldCube = 'wyrgbwrrywrgorwbbyoygbgggrowwbyooboyooygygrbgbwobwrwyr'
        self.assertEqual(shouldCube, cubeString)
        
# Top left align test (already aligned)
# For these tests, the cube arrives ready to be aligned
# so no input validation
    def testAlignTopLeftCorner(self):
        encodedCube = 'rbbbbgbbgwroyrryrrbywggbggbooywooyoogoygyygyrwrowwwrww'
        rotationsDone = ''
        cubeString, rotationsDone = alignTopLeftCorner(encodedCube, rotationsDone)
        shouldCube = 'rbbbbgbbgwroyrryrrbywggbggbooywooyoogoygyygyrwrowwwrww'
        self.assertEqual(shouldCube, cubeString)
        
# Top left align test (front)
    def testAlignTopLeftCorner2(self):
        encodedCube = 'ooybbgbbgrbbyrryrrwroggbggbbywwooyooyyroyygggwrowwwrww'
        rotationsDone = ''
        cubeString, rotationsDone = alignTopLeftCorner(encodedCube, rotationsDone)
        shouldCube = 'rbbbbgbbgwroyrryrrbywggbggbooywooyoogoygyygyrwrowwwrww'
        self.assertEqual(shouldCube, cubeString)
        
# Top left align test (right)
    def testAlignTopLeftCorner3(self):
        encodedCube = 'bywbbgbbgooyyrryrrrbbggbggbwrowooyoorygyygyogwrowwwrww'
        rotationsDone = ''
        cubeString, rotationsDone = alignTopLeftCorner(encodedCube, rotationsDone)
        shouldCube = 'rbbbbgbbgwroyrryrrbywggbggbooywooyoogoygyygyrwrowwwrww'
        self.assertEqual(shouldCube, cubeString)
        
# Top left align test (back)
    def testAlignTopLeftCorner4(self):
        encodedCube = 'wrobbgbbgbywyrryrrooyggbggbrbbwooyoogggyyoryywrowwwrww'
        rotationsDone = ''
        cubeString, rotationsDone = alignTopLeftCorner(encodedCube, rotationsDone)
        shouldCube = 'rbbbbgbbgwroyrryrrbywggbggbooywooyoogoygyygyrwrowwwrww'
        self.assertEqual(shouldCube, cubeString)
        
# Fish check and fix test (already)
    def testCheckIfFish(self):
        encodedCube = 'brygggggggbyoooooorgybbbbbbboorrrrrrrygyyyyyowwwwwwwww'
        rotationsDone = ''
        cubeString, rotationsDone, wasFish = checkIfFishAndFix(encodedCube, rotationsDone)
        shouldCube = 'brygggggggbyoooooorgybbbbbbboorrrrrrrygyyyyyowwwwwwwww'
        self.assertEqual(shouldCube, cubeString)
        
# Fish check and fix test 2 (top left)
    def testCheckIfFish2(self):
        encodedCube = 'gbyggggggrgyooooooboobbbbbbbryrrrrrryyryyyoygwwwwwwwww'
        rotationsDone = ''
        cubeString, rotationsDone, wasFish = checkIfFishAndFix(encodedCube, rotationsDone)
        shouldCube = 'brygggggggbyoooooorgybbbbbbboorrrrrrrygyyyyyowwwwwwwww'
        self.assertEqual(shouldCube, cubeString)
        
# Fish check and fix test 3 (top right)
    def testCheckIfFish3(self):
        encodedCube = 'rgyggggggboooooooobrybbbbbbgbyrrrrrroyyyyygyrwwwwwwwww'
        rotationsDone = ''
        cubeString, rotationsDone, wasFish = checkIfFishAndFix(encodedCube, rotationsDone)
        shouldCube = 'brygggggggbyoooooorgybbbbbbboorrrrrrrygyyyyyowwwwwwwww'
        self.assertEqual(shouldCube, cubeString)
        
# Fish check and fix test 4 (bottom right)
    def testCheckIfFish4(self):
        encodedCube = 'booggggggbryoooooogbybbbbbbrgyrrrrrrgyoyyyryywwwwwwwww'
        rotationsDone = ''
        cubeString, rotationsDone, wasFish = checkIfFishAndFix(encodedCube, rotationsDone)
        shouldCube = 'brygggggggbyoooooorgybbbbbbboorrrrrrrygyyyyyowwwwwwwww'
        self.assertEqual(shouldCube, cubeString)
        
# Fish check and fix test 5 (no fish)
    def testCheckIfFish5(self):
        encodedCube = 'wwwggrwwwgogyobgoyogyybygbrorborwbrbbyygygrrrooobwbywr'
        rotationsDone = ''
        cubeString, rotationsDone, wasFish = checkIfFishAndFix(encodedCube, rotationsDone)
        shouldCube = 'brygggggggbyoooooorgybbbbbbboorrrrrrrygyyyyyowwwwwwwww'
        self.assertEqual(False, wasFish)

    

    
    