from unittest import TestCase
from rubik.view.rotate import rotate
 
class RotateTest(TestCase):
    
   
# Rotate Analysis
#
#    Methods: rotate        accepts parameters, error checks, passes direction to
#                           Cube.rotate, returns python dictionary of results
#    Inputs:
#        parms: python dictionary with directions and cube {'dir': & 'cube':}
#            dir: string, [FfRrBbLlUu], optional (defaults to F), unvalidated
#            cube: string, 54 characters, unique 5th 14th 23rd 32nd 41st and 50th chars
#                  6 different chars included, mandatory, unvalidated
#            no extra keys
#    
#    Outputs:
#        Returns python dictionary showing results or errors
#        Nominal: {'cube': & 'status': ok}
#        Incorrect: {'status': 'error: some message'}
#
#    
#




        
# Happy path
#These should be fine since we already implemented cube.py (green lights)
#First red light test will be with empty dir

# Cube rotation 1 direction (F)
        
    def testRotateF(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'ygorbrbbyyyogrgrowwgoogrrwggobboyrowwybwybowgrwbywbyrg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual('ok', result.get('status'))
        self.assertEqual(expectedResult, result.get('cube'))
        
# Cube rotation 1 direction (f)
        
    def testRotatef(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'ybbrbrogywyoyrgbowwgoogrrwggorbogroywybwybbwrgwoywbyrg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'f'
        result = rotate(parms)
        self.assertEqual('ok', result.get('status'))
        self.assertEqual(expectedResult, result.get('cube'))
        
# Cube rotation 1 direction (R)
        
    def testRotateR(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'orwgbbyrgrwborywgorgobgrbwggogbowroowyywybygbbyrywoyrw'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'R'
        result = rotate(parms)
        self.assertEqual('ok', result.get('status'))
        self.assertEqual(expectedResult, result.get('cube'))
        
# Cube rotation 1 direction (r)
        
    def testRotater(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'orbgbbyrrogwyrobwrggobgrwwggogbowroowyrwyoygwbyyywbyrb'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'r'
        result = rotate(parms)
        self.assertEqual('ok', result.get('status'))
        self.assertEqual(expectedResult, result.get('cube'))
        
# Cube rotation 1 direction (B)
        
    def testRotateB(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'orygbbyrbbygwrrroyrowwgggrobogyowwooogwwybygrbywywbgbr'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'B'
        result = rotate(parms)
        self.assertEqual('ok', result.get('status'))
        self.assertEqual(expectedResult, result.get('cube'))

# Cube rotation 1 direction (b)
        
    def testRotateb(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'orygbbyrbbywwryroborgggwworyogrowgoorbgwybygrbywywbwgo'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'b'
        result = rotate(parms)
        self.assertEqual('ok', result.get('status'))
        self.assertEqual(expectedResult, result.get('cube'))
        
# Cube rotation 1 direction (L)
        
    def testRotateL(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'wrywbbyrbbyowrgrowwgyogyrwbrbgoooowggybrybogroywgwbyrg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'L'
        result = rotate(parms)
        self.assertEqual('ok', result.get('status'))
        self.assertEqual(expectedResult, result.get('cube'))
        
# Cube rotation 1 direction (l)
        
    def testRotatel(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'bryybbyrbbyowrgrowwgyogwrwwgwoooogbroybgybygrgywrwborg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'l'
        result = rotate(parms)
        self.assertEqual('ok', result.get('status'))
        self.assertEqual(expectedResult, result.get('cube'))
        
# Cube rotation 1 direction (U)
        
    def testRotateU(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'byogbbyrbwgowrgrowgogogrrwgorybowrooywwgyyrbbbywywbyrg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'U'
        result = rotate(parms)
        self.assertEqual('ok', result.get('status'))
        self.assertEqual(expectedResult, result.get('cube'))
        
# Cube rotation 1 direction (u)
        
    def testRotateu(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'goggbbyrborywrgrowbyoogrrwgwgobowroobbryygwwybywywbyrg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'u'
        result = rotate(parms)
        self.assertEqual('ok', result.get('status'))
        self.assertEqual(expectedResult, result.get('cube'))
        
# Cube rotation 2 directions (Fr)
        
    def testRotateFr(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'ygbrbbbbgogwyroygrggobgrbwggobboyrowwyrwyoowwrwoywryry'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'Fr'
        result = rotate(parms)
        self.assertEqual('ok', result.get('status'))
        self.assertEqual(expectedResult, result.get('cube'))
        
# Cube rotation lots directions (FRBLUfrblu)
        
    def testRotateLong(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'oryrbyywwbbobrgrwggrgygwrowoybgoybboywwoyowgrbogrwbrgy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FRBLUfrblu'
        result = rotate(parms)
        self.assertEqual('ok', result.get('status'))
        self.assertEqual(expectedResult, result.get('cube'))
        
# Cube rotation with null direction
# Defaults to F instruction
        
    def testNullDirCubeNomial(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'ygorbrbbyyyogrgrowwgoogrrwggobboyrowwybwybowgrwbywbyrg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = ''
        result = rotate(parms)
        self.assertEqual('ok', result.get('status'))
        self.assertEqual(expectedResult, result.get('cube'))
        
# Cube rotation missing dir key
# Defaults to F instruction
        
    def testNoDirKeyCubeNomial(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'ygorbrbbyyyogrgrowwgoogrrwggobboyrowwybwybowgrwbywbyrg'
        parms = {}
        parms['cube'] = encodedCube
        result = rotate(parms)
        self.assertEqual('ok', result.get('status'))
        self.assertEqual(expectedResult, result.get('cube'))
        
#Sad Path

# Incorrect direction (D)
    def testWrongDirCubeNominal(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'D'
        result = rotate(parms)
        self.assertEqual('error: invalid directions', result.get('status'))
        
# Incorrect direction (d)    
    def testWrongDirCubeNominal2(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'd'
        result = rotate(parms)
        self.assertEqual('error: invalid directions', result.get('status'))
        
# Incorrect direction (D in longer string)    
    def testWrongDirCubeNominal3(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FfRrDLlUu'
        result = rotate(parms)
        self.assertEqual('error: invalid directions', result.get('status'))
        
# Incorrect direction (T [random character outside of options])    
    def testWrongDirCubeNominal4(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'T'
        result = rotate(parms)
        self.assertEqual('error: invalid directions', result.get('status'))

# Null cube       
    def testOneDirEmptyCube(self):
        encodedCube = ''
        expectedResult = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwwwwooorrryyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result.get('status'))
        
# Cube too short        
    def testOneDirShortCube(self):
        encodedCube = 'gg'
        expectedResult = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwwwwooorrryyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result.get('status'))
 
# Cube too long       
    def testOneDirLongCube(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyygrb'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result.get('status'))
        
# Cube has ' ' as characters       
    def testCubeEmptyChar(self):
        encodedCube = 'bbbbbbbbb         rrrrrrrrroooooooooyyyyyyyyywwwwwwwww'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result.get('status'))
        
# Cube does not have 9 of valid characters       
    def testCubeNonNine(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwb'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result.get('status'))
        
# Incorrect key     
    def testIncorrectKey(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['buce'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual('error: missing cube key', result.get('status'))
        
# Incorrect key second test   
    def testIncorrectKey2(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['blue'] = 'B'
        result = rotate(parms)
        self.assertEqual('error: invalid key', result.get('status'))
        
# Extra key  
    def testExtraKey(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        parms['newkey'] = 'key'
        result = rotate(parms)
        self.assertEqual('error: too many keys', result.get('status'))
        
# Missing cube key
    def testMissingCubeKey(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual('error: missing cube key', result.get('status'))
        
# Non unique cube (5th and 14th match) 
    def testCubeNonUnique(self):
        encodedCube = 'gggggggggrrrrgrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result.get('status'))
        
# Non unique cube (5th and 23rd match)        
    def testCubeNonUnique2(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbgbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result.get('status'))
   
# Non unique cube (5th and 32nd match)     
    def testCubeNonUnique3(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbboooogoooowwwwwwwwwyyyyyyyyy'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result.get('status'))
     
# Non unique cube (5th and 41st match)   
    def testCubeNonUnique4(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwgwwwwyyyyyyyyy'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result.get('status'))
        
# Non unique cube (5th and 50th match)
    def testCubeNonUnique5(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyygyyyy'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result.get('status'))
        
# Non unique cube (14th and 23rd match)
    def testCubeNonUnique6(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbrbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result.get('status'))
        
# Invalid characters in cube
    def testCubeInvalidChars(self):
        encodedCube = 'bbybbybby*********wrrwrrwrroooooooooyyryyryyrwwbwwbwwb'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result.get('status'))
