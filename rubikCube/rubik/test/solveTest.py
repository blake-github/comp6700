from unittest import TestCase
from rubik.view.solve import solve
from rubik.view.rotate import rotate
from rubik.controller.bottomCross import checkIfBottomCross
 

class SolveTest(TestCase):
    
# Solve analysis
#
#    Solve: class
#    Methods: solve:    calls different classes in order to solve cube
#
#    Cube.solve
#        inputs:
#            parms: python dictionary with cube {'cube':}
#            cube: string, 54 characters, unique 5th 14th 23rd 32nd 41st and 50th chars
#                  6 different chars included, mandatory, unvalidated
#            no extra keys
#        outputs:
#            Returns python dictionary showing results or errors
#            Nominal: {'cube': & 'status': 'ok' & 'integrity': ''}
#            Incorrect: {'status': 'error: some message'}
#
#
#
        
# Happy path


# Solved cube test 
#(can't test through rotate because rotate will default to F)
    def testSolvedCube(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        solutionCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        self.assertEqual('', solution.get('solution'))
        
# Nominal test
    def testNominalCube(self):
        encodedCube = 'gbbgbbgbbrrorrorrobggbggbggroorooroowwywywwwyyywywyyyw'
        solutionCube = 'gbggbggbgorooroorobgbbgbbgbrorrorroryyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfBottomCross(solvedCube))
        
# Nominal test 2
    def testNominalCube2(self):
        encodedCube = 'EExcccxFbcbcExxEExbbcF7bb7cE7F7ExbcFFxExbE7FF7c7bF7xF7'
        solutionCube = 'gbggbggbgorooroorobgbbgbbgbrorrorroryyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfBottomCross(solvedCube))
        
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
        self.assertEqual(True, checkIfBottomCross(solvedCube))
        
# Nominal test 4
    def testNominalCube4(self):
        encodedCube = 'DffrkkkHHHrDArkDDrkHrrHHffrADkDDfkHAHrfAfAAkDrfAAAkfDH'
        solutionCube = 'gbggbggbgorooroorobgbbgbbgbrorrorroryyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfBottomCross(solvedCube))
        
# Nominal test 5
    def testNominalCube5(self):
        encodedCube = 'emmvvqvvqqjqjjmKeKKKmeKKjmjvKmmmqvvqejjqeeKvvjjmeqKeqe'
        solutionCube = 'gbggbggbgorooroorobgbbgbbgbrorrorroryyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfBottomCross(solvedCube))
        
# Nominal test 6
    def testNominalCube6(self):
        encodedCube = 'oo58800j0oyjyjy88j08o5yj0yj58jo50o0yyo850jy585055oj8oy'
        solutionCube = 'gbggbggbgorooroorobgbbgbbgbrorrorroryyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedCube = result.get('cube')
        self.assertEqual(True, checkIfBottomCross(solvedCube))
        
        
        
# Method tests

# Integrity key test
    def testIntegreityKey(self):
        encodedCube = 'gbbgbbgbbrrorrorrobggbggbggroorooroowwywywwwyyywywyyyw'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedInteg = solution.get('integrity')
        token = 'db7d4bc162fcd3b2ac5ee66d5af419d2bdb37d264fa1cef5d88d7427d2708cec'
        isSubstring = solvedInteg in token
        self.assertEqual(True, isSubstring)
        
# Integrity key test 2
    def testIntegreityKey2(self):
        encodedCube = 'EExcccxFbcbcExxEExbbcF7bb7cE7F7ExbcFFxExbE7FF7c7bF7xF7'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedInteg = solution.get('integrity')
        token = 'f611f1780eda35116574c5139bf762c4d442725c8a26599fd9ce70047b718012'
        isSubstring = solvedInteg in token
        self.assertEqual(True, isSubstring)
        
# Integrity key test 3
    def testIntegreityKey3(self):
        encodedCube = 'DGG6Dww6ODGOOP6PGGDDDDwPwPGOw6D6O6GOPO6PGPGwP6ww6ODwOP'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        directions = solution.get('solution')
        parms['dir'] = directions
        result = rotate(parms)
        solvedInteg = solution.get('integrity')
        token = 'bf24c2840cff968d37a3c9d92146ca882a22ca231996cfa6d27da1b0bfa6e4c2'
        isSubstring = solvedInteg in token
        self.assertEqual(True, isSubstring)
        


    
    
#Sad path

# Cube too short        
# Incorrect key test    
    def testIncorrectKey(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['buce'] = encodedCube
        solution = solve(parms)
        self.assertEqual('error: missing cube key', solution.get('status'))
        
# Extra key test    
    def testExtraKey(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['newkey'] = 'key'
        solution = solve(parms)
        self.assertEqual('error: too many keys', solution.get('status'))
        
# Missing key test    
    def testMissingKey(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        solution = solve(parms)
        self.assertEqual('error: missing cube key', solution.get('status'))
        
# Small test to check if cube validation works here
    def testBadCube(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwb'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        self.assertEqual('error: invalid cube', solution.get('status'))
        
# Second test to check if cube validation works here
    def testBadCharCube(self):
        encodedCube = 'bbbbbbbbb*********rrrrrrrrroooooooooyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        self.assertEqual('error: invalid cube', solution.get('status'))
        
# Invalid cube test
    def testInvalidCube(self):
        encodedCube = 'bgbbbbbbbrrrrrrrrrgooggggggybooooooogyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        solution = solve(parms)
        self.assertEqual('error: unsolvable cube', solution.get('status'))
        