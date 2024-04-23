from unittest import TestCase
from rubik.view.solve import solve
from rubik.view.rotate import rotate
from rubik.controller.bottomLayer import checkIfBottomLayer
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import _findMatchingCenter as findMatchingCenter
from rubik.model.cube import Cube
from rubik.model.constants import *
 

class bottomLayer(TestCase):

        
# Happy path

# Solved cube test
    def testSolvedBottomLayer(self):
        encodedCube = 'ygyrbbbbbrbooryrrryoyggggggbbbooyooorygryyorgwwwwwwwww'
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
        self.assertEqual(True, checkIfBottomLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfBottomLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfBottomLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfBottomLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfBottomLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfBottomLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfBottomLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfBottomLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfBottomLayer(solvedCube))
        
# Nominal test 11
    def testNominalCube11(self):
        encodedCube = 'ff7zv7v77fflQllzQlvvQz7lvfQ7vQ7QQffQzzzlfl7Qlzzlvzvv7f'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfBottomLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfBottomLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfBottomLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfBottomLayer(solvedCube))
        
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
        self.assertEqual(True, checkIfBottomLayer(solvedCube))
        
# Nominal test 16
    def testNominalCube16(self):
        encodedCube = 'obwgrorrrywbrorooowrwgbbbbbrggwwbwwogwgoggborgyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfBottomLayer(solvedCube))
        
# Nominal test 17
    def testNominalCube17(self):
        encodedCube = 'oloZ0l00FZFZooFZo30FZ3lool3oo3ZFlF030ZF030l3lF3lZZ3lF0'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfBottomLayer(solvedCube))
        
#Method testing

# Check bottom layer test
    def testCheckBottomLayer(self):
        encodedCube = 'ygyrbbbbbrbooryrrryoyggggggbbbooyooorygryyorgwwwwwwwww'
        result = checkIfBottomLayer(encodedCube)
        self.assertEqual(True, result)
        
# Check bottom layer test 
    def testCheckBottomLayer2(self):
        encodedCube = 'gbbgbbgbbrrorrorrobggbggbggroorooroowwywywwwyyywywyyyw'
        result = checkIfBottomLayer(encodedCube)
        self.assertEqual(False, result)
        
        
    

        