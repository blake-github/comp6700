from unittest import TestCase
from rubik.view.solve import solve
from rubik.view.rotate import rotate
from rubik.controller.bottomLayer import checkIfBottomLayer
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.middleLayer import checkIfMiddleLayer
from rubik.controller.upFaceCross import checkIfUpFaceCross
from rubik.controller.upFaceSurface import checkIfUpFaceSurface
from rubik.controller.upperLayer import checkIfSolved
from rubik.controller.upperLayer import _matchingCornersAlign as matchingCornersAlign
from rubik.controller.upperLayer import checkIfCorners
from rubik.controller.upperLayer import _doFinalRotationBack as doFinalRotationBack
from rubik.controller.upperLayer import _doFinalRotationRight as doFinalRotationRight
from rubik.controller.upperLayer import _doFinalRotationLeft as doFinalRotationLeft
from rubik.controller.upperLayer import _doFinalRotationFront as doFinalRotationFront
from rubik.controller.upperLayer import _doCornerRotationsBack as doCornerRotationsBack
from rubik.controller.upperLayer import _doCornerRotationsRight as doCornerRotationsRight
from rubik.controller.upperLayer import _doCornerRotationsLeft as doCornerRotationsLeft
from rubik.controller.upperLayer import _doCornerRotationsFront as doCornerRotationsFront
from rubik.controller.upperLayer import _findSolvedFace as findSolvedFace
from rubik.model.cube import Cube
from rubik.model.constants import *


class upperLayerTest(TestCase):

        
# Happy path

# Solved cube test
    def testSolvedCube(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
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
        self.assertEqual(True, checkIfSolved(solvedCube))
        
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
        self.assertEqual(True, checkIfSolved(solvedCube))
        
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
        self.assertEqual(True, checkIfSolved(solvedCube))
        
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
        self.assertEqual(True, checkIfSolved(solvedCube))
        
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
        self.assertEqual(True, checkIfSolved(solvedCube))
        
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
        self.assertEqual(True, checkIfSolved(solvedCube))
        
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
        self.assertEqual(True, checkIfSolved(solvedCube))
        
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
        self.assertEqual(True, checkIfSolved(solvedCube))
        
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
        self.assertEqual(True, checkIfSolved(solvedCube))
        
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
        self.assertEqual(True, checkIfSolved(solvedCube))
        
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
        self.assertEqual(True, checkIfSolved(solvedCube))
        
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
        self.assertEqual(True, checkIfSolved(solvedCube))
        
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
        self.assertEqual(True, checkIfSolved(solvedCube))
        
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
        self.assertEqual(True, checkIfSolved(solvedCube))
        
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
        self.assertEqual(True, checkIfSolved(solvedCube))
        
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
        self.assertEqual(True, checkIfSolved(solvedCube))
        
# Nominal test 17
    def testNominalCube17(self):
        encodedCube = 'wbyrrgrwrowboogbggyowwwwwrwybgbbyyyobrrggobyrgygoyrobo'
                      #FQKrrXrFrHFQHHXQXXKHFFFFFrFKQXQQKKKHQrrXXHQKrXKXHKrHQH
                      # F=w, Q=b, K=y, r=r, X=g, H=o
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfSolved(solvedCube))
        
# Nominal test 18
    def testNominalCube18(self):
        encodedCube = 'oloZ0l00FZFZooFZo30FZ3lool3oo3ZFlF030ZF030l3lF3lZZ3lF0'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfSolved(solvedCube))
        
# Method tests
# (Not re-doing the doAndTrackURotate methods since they are identical
# to last increment
    
#Solved cube check (True)
    def testSolvedCubeCheck(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        self.assertEqual(checkIfSolved(encodedCube), True)
        
#Solved cube check (False)
    def testSolvedCubeCheck2(self):
        encodedCube = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
        self.assertEqual(checkIfSolved(encodedCube), False)
        
# Matching Corners Test 1
    def testMatchCorners(self):
        encodedCube = 'brbbbbbbbrogrrrrrrobrggggggggoooooooyyyyyyyyywwwwwwwww'
        matchedCube = 'brbbbbbbbrogrrrrrrobrggggggggoooooooyyyyyyyyywwwwwwwww'
        rotationsDone = ''
        postCube, rotationsDone, faceValue = matchingCornersAlign(encodedCube, rotationsDone)
        self.assertEqual(matchedCube, postCube)
        self.assertEqual(faceValue, FMM)
        
# Matching Corners Test 2
    def testMatchCorners2(self):
        encodedCube = 'rogbbbbbbobrrrrrrrggoggggggbrbooooooyyyyyyyyywwwwwwwww'
        matchedCube = 'brbbbbbbbrogrrrrrrobrggggggggoooooooyyyyyyyyywwwwwwwww'
        rotationsDone = ''
        postCube, rotationsDone, faceValue = matchingCornersAlign(encodedCube, rotationsDone)
        self.assertEqual(matchedCube, postCube)
        self.assertEqual(faceValue, FMM)
        
# Matching Corners Test 3
    def testMatchCorners3(self):
        encodedCube = 'obrbbbbbbggorrrrrrbrbggggggrogooooooyyyyyyyyywwwwwwwww'
        matchedCube = 'brbbbbbbbrogrrrrrrobrggggggggoooooooyyyyyyyyywwwwwwwww'
        rotationsDone = ''
        postCube, rotationsDone, faceValue = matchingCornersAlign(encodedCube, rotationsDone)
        self.assertEqual(matchedCube, postCube)
        self.assertEqual(faceValue, FMM)
        
# Matching Corners Test 4
    def testMatchCorners4(self):
        encodedCube = 'ggobbbbbbbrbrrrrrrrogggggggobrooooooyyyyyyyyywwwwwwwww'
        matchedCube = 'brbbbbbbbrogrrrrrrobrggggggggoooooooyyyyyyyyywwwwwwwww'
        rotationsDone = ''
        postCube, rotationsDone, faceValue = matchingCornersAlign(encodedCube, rotationsDone)
        self.assertEqual(matchedCube, postCube)
        self.assertEqual(faceValue, FMM)
        
# Matching Corners Test 5
    def testMatchCorners5(self):
        encodedCube = 'bggbbbbbboobrrrrrrrbrgggggggroooooooyyyyyyyyywwwwwwwww'
        matchedCube = 'oobbbbbbbrbrrrrrrrgroggggggbggooooooyyyyyyyyywwwwwwwww'
        rotationsDone = ''
        postCube, rotationsDone, faceValue = matchingCornersAlign(encodedCube, rotationsDone)
        self.assertEqual(matchedCube, postCube)
        self.assertEqual(faceValue, RMM)
        
# Matching Corners Test 6
    def testMatchCorners6(self):
        encodedCube = 'oobbbbbbbrbrrrrrrrgroggggggbggooooooyyyyyyyyywwwwwwwww'
        matchedCube = 'oobbbbbbbrbrrrrrrrgroggggggbggooooooyyyyyyyyywwwwwwwww'
        rotationsDone = ''
        postCube, rotationsDone, faceValue = matchingCornersAlign(encodedCube, rotationsDone)
        self.assertEqual(matchedCube, postCube)
        self.assertEqual(faceValue, RMM)
        
# Matching Corners Test 7
    def testMatchCorners7(self):
        encodedCube = 'rbrbbbbbbgrorrrrrrbggggggggoobooooooyyyyyyyyywwwwwwwww'
        matchedCube = 'oobbbbbbbrbrrrrrrrgroggggggbggooooooyyyyyyyyywwwwwwwww'
        rotationsDone = ''
        postCube, rotationsDone, faceValue = matchingCornersAlign(encodedCube, rotationsDone)
        self.assertEqual(matchedCube, postCube)
        self.assertEqual(faceValue, RMM)
        
# Matching Corners Test 8
    def testMatchCorners8(self):
        encodedCube = 'grobbbbbbbggrrrrrroobggggggrbrooooooyyyyyyyyywwwwwwwww'
        matchedCube = 'oobbbbbbbrbrrrrrrrgroggggggbggooooooyyyyyyyyywwwwwwwww'
        rotationsDone = ''
        postCube, rotationsDone, faceValue = matchingCornersAlign(encodedCube, rotationsDone)
        self.assertEqual(matchedCube, postCube)
        self.assertEqual(faceValue, RMM)
        
#Solved corners check (False)
    def testCheckIfCorners(self):
        encodedCube = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
        self.assertEqual(checkIfCorners(encodedCube), False)
        
#Solved corners check (True)
    def testCheckIfCorners2(self):
        encodedCube = 'rrrrrrrrrooooooooowwwwwwwwwbbbbbbbbbgggggggggyyyyyyyyy'
        self.assertEqual(checkIfCorners(encodedCube), True)
        
#Final rotation tests (back)
    def testFinalRotationBack(self):
        encodedCube = 'grobbbbbbbggrrrrrroobggggggrbrooooooyyyyyyyyywwwwwwwww'
        matchedCube = 'ggobbbbbbbbgrrrrrroobggggggrrrooooooyyyyyyyyywwwwwwwww'
        rotationsDone = ''
        postCube, rotationsDone = doFinalRotationBack(encodedCube, rotationsDone)
        self.assertEqual(matchedCube, postCube)
        
#Final rotation tests (right)
    def testFinalRotationRight(self):
        encodedCube = 'grobbbbbbbggrrrrrroobggggggrbrooooooyyyyyyyyywwwwwwwww'
        matchedCube = 'goobbbbbbbggrrrrrrobbggggggrrrooooooyyyyyyyyywwwwwwwww'
        rotationsDone = ''
        postCube, rotationsDone = doFinalRotationRight(encodedCube, rotationsDone)
        self.assertEqual(matchedCube, postCube)
        
#Final rotation tests (left)
    def testFinalRotationLeft(self):
        encodedCube = 'grobbbbbbbggrrrrrroobggggggrbrooooooyyyyyyyyywwwwwwwww'
        matchedCube = 'ggobbbbbbbogrrrrrrorbggggggrbrooooooyyyyyyyyywwwwwwwww'
        rotationsDone = ''
        postCube, rotationsDone = doFinalRotationLeft(encodedCube, rotationsDone)
        self.assertEqual(matchedCube, postCube)
        
#Final rotation tests (front)
    def testFinalRotationFront(self):
        encodedCube = 'grobbbbbbbggrrrrrroobggggggrbrooooooyyyyyyyyywwwwwwwww'
        matchedCube = 'grobbbbbbbogrrrrrrobbggggggrgrooooooyyyyyyyyywwwwwwwww'
        rotationsDone = ''
        postCube, rotationsDone = doFinalRotationFront(encodedCube, rotationsDone)
        self.assertEqual(matchedCube, postCube)
        
#Corner rotation tests (back)
    def testCornerRotationsBack(self):
        encodedCube = 'grobbbbbbbggrrrrrroobggggggrbrooooooyyyyyyyyywwwwwwwww'
        matchedCube = 'bbrbbbbbbgggrrrrrroobggggggrroooooooyyyyyyyyywwwwwwwww'
        rotationsDone = ''
        postCube, rotationsDone = doCornerRotationsBack(encodedCube, rotationsDone)
        self.assertEqual(matchedCube, postCube)
        
#Corner rotation tests (right)
    def testCornerRotationsRight(self):
        encodedCube = 'grobbbbbbbggrrrrrroobggggggrbrooooooyyyyyyyyywwwwwwwww'
        matchedCube = 'rrobbbbbbbggrrrrrrobrgggggggobooooooyyyyyyyyywwwwwwwww'
        rotationsDone = ''
        postCube, rotationsDone = doCornerRotationsRight(encodedCube, rotationsDone)
        self.assertEqual(matchedCube, postCube)
        
#Corner rotation tests (left)
    def testCornerRotationsLeft(self):
        encodedCube = 'grobbbbbbbggrrrrrroobggggggrbrooooooyyyyyyyyywwwwwwwww'
        matchedCube = 'gggbbbbbbororrrrrrbobggggggrbrooooooyyyyyyyyywwwwwwwww'
        rotationsDone = ''
        postCube, rotationsDone = doCornerRotationsLeft(encodedCube, rotationsDone)
        self.assertEqual(matchedCube, postCube)
        
#Corner rotation tests (front)
    def testCornerRotationsFront(self):
        encodedCube = 'grobbbbbbbggrrrrrroobggggggrbrooooooyyyyyyyyywwwwwwwww'
        matchedCube = 'grobbbbbbbobrrrrrrrggggggggobrooooooyyyyyyyyywwwwwwwww'
        rotationsDone = ''
        postCube, rotationsDone = doCornerRotationsFront(encodedCube, rotationsDone)
        self.assertEqual(matchedCube, postCube)
        
#Find solved face (front)
    def testFindSolvedFaceFront(self):
        encodedCube = 'bbbbbbbbbrgrrrrrrrgogggggggoroooooooyyyyyyyyywwwwwwwww'
        face = findSolvedFace(encodedCube)
        self.assertEqual(face, FMM)
        
#Find solved face (back)
    def testFindSolvedFaceBack(self):
        encodedCube = 'bobbbbbbbrbrrrrrrrgggggggggoroooooooyyyyyyyyywwwwwwwww'
        face = findSolvedFace(encodedCube)
        self.assertEqual(face, BMM)
        
#Find solved face (right)
    def testFindSolvedFaceRight(self):
        encodedCube = 'ybbybbyobrrrrrrrrrggwggwggwooooooobogyygyygyybwwbwwbww'
        face = findSolvedFace(encodedCube)
        self.assertEqual(face, RMM)
        
#Find solved face (left)
    def testFindSolvedFaceLeft(self):
        encodedCube = 'bbwrbwbbwrrrrrbrrryggyggyggoooooooooyybyybyybwwgwwgwwg'
        face = findSolvedFace(encodedCube)
        self.assertEqual(face, LMM)




    

    
    