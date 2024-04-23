from unittest import TestCase
from rubik.view.solve import solve
from rubik.view.rotate import rotate
from rubik.controller.bottomLayer import checkIfBottomLayer
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.middleLayer import checkIfMiddleLayer
from rubik.controller.middleLayer import checkIfMiddleLayer
from rubik.controller.middleLayer import _doRightTrigger as doRightTrigger
from rubik.controller.middleLayer import _doLeftTrigger as doLeftTrigger
from rubik.controller.middleLayer import _findMatchingCenter as findMatchingCenter
from rubik.controller.middleLayer import _doAndTrackURotate as doAndTrackURotate
from rubik.controller.middleLayer import _doAndTrackuRotate as doAndTrackuRotate
from rubik.controller.middleLayer import _findDuoToRotate as findDuoToRotate
from rubik.controller.middleLayer import _doFTMMatch as doFTMMatch
from rubik.controller.middleLayer import _doRTMMatch as doRTMMatch
from rubik.controller.middleLayer import _doLTMMatch as doLTMMatch
from rubik.controller.middleLayer import _doBTMMatch as doBTMMatch
from rubik.controller.middleLayer import _doUBMSwitch as doUBMSwitch
from rubik.controller.middleLayer import _doUMRSwitch as doUMRSwitch
from rubik.controller.middleLayer import _doUMLSwitch as doUMLSwitch
from rubik.controller.middleLayer import _doUTMSwitch as doUTMSwitch
from rubik.model.cube import Cube
from rubik.model.constants import *
 

class middleLayerTest(TestCase):
    
    
# Happy path

# Solved cube test
    def testSolvedMiddleLayer(self):
        encodedCube = 'byrgggggggboooooooyrobbbbbbbyyrrrrrryyggyyroywwwwwwwww'
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
        self.assertEqual(True, checkIfMiddleLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfMiddleLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfMiddleLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfMiddleLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfMiddleLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfMiddleLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfMiddleLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfBottomLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfMiddleLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfMiddleLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfMiddleLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfMiddleLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfMiddleLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfMiddleLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfMiddleLayer(solvedCube))
        
# Method tests
        
# check if middle layer test
    def testCheckIfMiddleLayer(self):
        encodedCube = 'byrgggggggboooooooyrobbbbbbbyyrrrrrryyggyyroywwwwwwwww'
        result = checkIfMiddleLayer(encodedCube)
        self.assertEqual(True, result)
        
# Right trigger tests
    def testDoRightTrigger(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        resultCube = 'rrybbybbbgrrgrryrrgooggggggbbwooooooyyyyyybbowwrwwwwww'
        rotationsDone = ''
        midFaceToRotate = FMM
        postCube, resultRotates = doRightTrigger(encodedCube, rotationsDone, midFaceToRotate)
        self.assertEqual(resultCube, postCube)
        
# Right trigger test 2
    def testDoRightTrigger2(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        resultCube = 'rrwbbbbbbggyrryrrroggoggyggobbooooooyybyyryyrwwwwwwwwg'
        rotationsDone = ''
        midFaceToRotate = RMM
        postCube, resultRotates = doRightTrigger(encodedCube, rotationsDone, midFaceToRotate)
        self.assertEqual(resultCube, postCube)
        
# Right trigger test 3
    def testDoRightTrigger3(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        resultCube = 'rbbrbbybbrggrrrrrroowggggggbbyooyooooyyoyygyybwwwwwwww'
        rotationsDone = ''
        midFaceToRotate = LMM
        postCube, resultRotates = doRightTrigger(encodedCube, rotationsDone, midFaceToRotate)
        self.assertEqual(resultCube, postCube)
        
# Right trigger test 4
    def testDoRightTrigger4(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        resultCube = 'brrbbbbbbggwrrrrrrooyggygggboobooyoorggyyyyyywwwwwwoww'
        rotationsDone = ''
        midFaceToRotate = BMM
        postCube, resultRotates = doRightTrigger(encodedCube, rotationsDone, midFaceToRotate)
        self.assertEqual(resultCube, postCube)
        
# Left trigger tests
    def testDoLeftTrigger(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        resultCube = 'yooybbbbbwbbrrrrrrrrgggggggoogoogooyyyyyyyrbbowwwwwwww'
        rotationsDone = ''
        midFaceToRotate = FMM
        postCube, resultRotates = doLeftTrigger(encodedCube, rotationsDone, midFaceToRotate)
        self.assertEqual(resultCube, postCube)
        
# Left trigger test 2
    def testDoLeftTrigger2(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        resultCube = 'bbobbobbyybbyrrrrrwrrggggggggoooooooyyryyryygwwbwwwwww'
        rotationsDone = ''
        midFaceToRotate = RMM
        postCube, resultRotates = doLeftTrigger(encodedCube, rotationsDone, midFaceToRotate)
        self.assertEqual(resultCube, postCube)
        
# Left trigger test 3
    def testDoLeftTrigger3(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        resultCube = 'woobbbbbbbbrrrrrrrggrggrggyyggyooooobyyoyyoyywwwwwwgww'
        rotationsDone = ''
        midFaceToRotate = LMM
        postCube, resultRotates = doLeftTrigger(encodedCube, rotationsDone, midFaceToRotate)
        self.assertEqual(resultCube, postCube)
        
# Left trigger test 4
    def testDoLeftTrigger4(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        resultCube = 'oobbbbbbbrrbrrbrryyrrygggggwggooooooggoyyyyyywwwwwwwwr'
        rotationsDone = ''
        midFaceToRotate = BMM
        postCube, resultRotates = doLeftTrigger(encodedCube, rotationsDone, midFaceToRotate)
        self.assertEqual(resultCube, postCube)
        
# findMatchingCenter test
    def testFindMatchingCenter(self):
        encodedCube = 'gbygbbroggwbywyroowgrwgryobobwwowrywgryoybyrobywgrgorb'
        searchColor = encodedCube[FTM]
        result = findMatchingCenter(encodedCube, searchColor)
        self.assertEqual(4, result)
        
# U Rotate test
    def testDoURotate(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        resultCube = 'rrrbbbbbbgggrrrrrroooggggggbbbooooooyyyyyyyyywwwwwwwww'
        rotationsDone = ''
        postCube, resultRotates = doAndTrackURotate(encodedCube, rotationsDone)
        self.assertEqual(resultCube, postCube)
        
# u Rotate test
    def testDouRotate(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        resultCube = 'ooobbbbbbbbbrrrrrrrrrgggggggggooooooyyyyyyyyywwwwwwwww'
        rotationsDone = ''
        postCube, resultRotates = doAndTrackuRotate(encodedCube, rotationsDone)
        self.assertEqual(resultCube, postCube)
        
# Find Duo to Rotate test
    def testFindDuo(self):
        encodedCube = 'yowbbgbbbybyowwwwwggyygbgggwwbyooooogyogywoybrrrrrrrrr'
        rotationsDone = ''
        resultFront = findDuoToRotate(encodedCube, rotationsDone)
        self.assertEqual(RTM, resultFront)
        
# FTM match test
    def testDoFTMMatch(self):
        encodedCube = 'wwbbbgbbbyowowwwwwybyygbgggggyyoooooowbyyyggorrrrrrrrr'
        resultCube = 'ggybbgbbbwwbowwwwwyowygbgggybyyooooobyowygoygrrrrrrrrr'
        rotationsDone = ''
        cubeString, rotationsDone, rotatedTo = doFTMMatch(encodedCube, rotationsDone)
        self.assertEqual(resultCube, cubeString)
        
# RTM match test
    def testDoRTMMatch(self):
        encodedCube = 'yowbbgbbbybyowwwwwggyygbgggwwbyooooogyogywoybrrrrrrrrr'
        resultCube = 'ybybbgbbbggyowwwwwwwbygbgggyowyooooooggyyybworrrrrrrrr'
        rotationsDone = ''
        cubeString, rotationsDone, rotatedTo = doRTMMatch(encodedCube, rotationsDone)
        self.assertEqual(resultCube, cubeString)
        
# LTM match test
    def testDoLTMMatch(self):
        encodedCube = 'yowbbgbbbybyowwwwwggyygbgggwwbyooooogyogywoybrrrrrrrrr'
        resultCube = 'ggybbgbbbwwbowwwwwyowygbgggybyyooooobyowygoygrrrrrrrrr'
        rotationsDone = ''
        cubeString, rotationsDone, rotatedTo = doLTMMatch(encodedCube, rotationsDone)
        self.assertEqual(resultCube, cubeString)
        
# BTM match test
    def testDoBTMMatch(self):
        encodedCube = 'ybybbgbbbggyowwwwwwwbygbgggyowyooooooggyyybworrrrrrrrr'
        resultCube = 'ggybbgbbbwwbowwwwwyowygbgggybyyooooobyowygoygrrrrrrrrr'
        rotationsDone = ''
        cubeString, rotationsDone, rotatedTo = doBTMMatch(encodedCube, rotationsDone)
        self.assertEqual(resultCube, cubeString)
        
# UBM Switch test
    def testDoUBMSwitch(self):
        encodedCube = 'ybybbgbbbggyowwwwwwwbygbgggyowyooooooggyyybworrrrrrrrr'
        resultCube = 'ggybbbbbboyywwwwwwwobygbgggwwyyoooooygggyooybrrrrrrrrr'
        rotationsDone = ''
        cubeString, rotationsDone = doUBMSwitch(encodedCube, rotationsDone)
        self.assertEqual(resultCube, cubeString)
        
# UMR Switch test
    def testDoUMRSwitch(self):
        encodedCube = 'ggybbgbbbwwbowwwwwyowygbgggybyyooooobyowygoygrrrrrrrrr'
        resultCube = 'ybbbbgbbbyogowwwwwoywggbgggyygyooooobgywyywworrrrrrrrr'
        rotationsDone = ''
        cubeString, rotationsDone = doUMRSwitch(encodedCube, rotationsDone)
        self.assertEqual(resultCube, cubeString)
        
# UML Switch test
    def testDoUMLSwitch(self):
        encodedCube = 'gybbbbbbbyoywwwwwwbwgggbgggoowyoooooyywgyyygorrrrrrrrr'
        resultCube = 'oogbbbbbbybywwwwwwbgoggggggbwgooooooyywyyyyywrrrrrrrrr'
        rotationsDone = ''
        cubeString, rotationsDone = doUMLSwitch(encodedCube, rotationsDone)
        self.assertEqual(resultCube, cubeString)
        
# UTM Switch test
    def testDoUTMSwitch(self):
        encodedCube = 'yygoryrrryrwgogoooywrrwgwwwowrwgrgggyooyyygowbbbbbbbbb'
        resultCube = 'yggoryrrryyggooooorrwwwgwwwyyowgrgggoyyoywrrwbbbbbbbbb'
        rotationsDone = ''
        cubeString, rotationsDone = doUTMSwitch(encodedCube, rotationsDone)
        self.assertEqual(resultCube, cubeString)
    
        
        
        
        
        
        