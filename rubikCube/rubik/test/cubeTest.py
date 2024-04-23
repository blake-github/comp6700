import unittest
import rubik.model.cube as cube
 
class CubeTest(unittest.TestCase):
        
# Cube analysis
#
#    Cube: class, state machine, maintains internal state
#    Methods: _init_    constructs cube from serialized string
#             get        returns serialized string of internal representation
#             rotate    rotates the cube using 'dir' key
#
#    Cube.rotate
#        inputs:
#            directions: string, len .GE. 0, [FfRrBbLlUu], 
#                        optional (default to F), validated in rotate.py
#        outputs:
#            side-effects: no external effects, internal state change
#            nominal: return serialized cube
#            abnormal: should be no abnormal cases (error checks in rotate.py)
#
#
#    Cube._init_
#        inputs:
#            encodedCube: string, len 54, [a-z,A-Z,0-9], mandatory, unvalidated
#
#        outputs:
#            nominal: initializes the cube object
#            abnormal: errors for invalid cube
#
#    Cube.get
#        inputs:
#            none
#
#        outputs:
#            nominal: returns current cube
#

# Rotate tests
# Happy path

# Cube rotation 1 direction (F)
        
    def testRotateF(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'ygorbrbbyyyogrgrowwgoogrrwggobboyrowwybwybowgrwbywbyrg'
        theCube = cube.Cube(encodedCube)
        result = theCube.rotate('F')
        self.assertEqual(expectedResult, result)
        
# Cube rotation 1 direction (f)
        
    def testRotatef(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'ybbrbrogywyoyrgbowwgoogrrwggorbogroywybwybbwrgwoywbyrg'
        theCube = cube.Cube(encodedCube)
        result = theCube.rotate('f')
        self.assertEqual(expectedResult, result)
        
# Cube rotation 1 direction (R)
        
    def testRotateR(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'orwgbbyrgrwborywgorgobgrbwggogbowroowyywybygbbyrywoyrw'
        theCube = cube.Cube(encodedCube)
        result = theCube.rotate('R')
        self.assertEqual(expectedResult, result)
        
# Cube rotation 1 direction (r)
        
    def testRotater(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'orbgbbyrrogwyrobwrggobgrwwggogbowroowyrwyoygwbyyywbyrb'
        theCube = cube.Cube(encodedCube)
        result = theCube.rotate('r')
        self.assertEqual(expectedResult, result)
        
# Cube rotation 1 direction (B)
        
    def testRotateB(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'orygbbyrbbygwrrroyrowwgggrobogyowwooogwwybygrbywywbgbr'
        theCube = cube.Cube(encodedCube)
        result = theCube.rotate('B')
        self.assertEqual(expectedResult, result)
        
# Cube rotation 1 direction (b)
        
    def testRotateb(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'orygbbyrbbywwryroborgggwworyogrowgoorbgwybygrbywywbwgo'
        theCube = cube.Cube(encodedCube)
        result = theCube.rotate('b')
        self.assertEqual(expectedResult, result)
        
# Cube rotation 1 direction (L)
        
    def testRotateL(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'wrywbbyrbbyowrgrowwgyogyrwbrbgoooowggybrybogroywgwbyrg'
        theCube = cube.Cube(encodedCube)
        result = theCube.rotate('L')
        self.assertEqual(expectedResult, result)
        
# Cube rotation 1 direction (l)
        
    def testRotatel(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'bryybbyrbbyowrgrowwgyogwrwwgwoooogbroybgybygrgywrwborg'
        theCube = cube.Cube(encodedCube)
        result = theCube.rotate('l')
        self.assertEqual(expectedResult, result)
        
# Cube rotation 1 direction (U)
        
    def testRotateU(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'byogbbyrbwgowrgrowgogogrrwgorybowrooywwgyyrbbbywywbyrg'
        theCube = cube.Cube(encodedCube)
        result = theCube.rotate('U')
        self.assertEqual(expectedResult, result)
        
# Cube rotation 1 direction (u)
        
    def testRotateu(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'goggbbyrborywrgrowbyoogrrwgwgobowroobbryygwwybywywbyrg'
        theCube = cube.Cube(encodedCube)
        result = theCube.rotate('u')
        self.assertEqual(expectedResult, result)
        
# Cube rotation 2 directions (Fr)
        
    def testRotateFr(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'ygbrbbbbgogwyroygrggobgrbwggobboyrowwyrwyoowwrwoywryry'
        theCube = cube.Cube(encodedCube)
        result = theCube.rotate('Fr')
        self.assertEqual(expectedResult, result)
        
# Cube rotation lots directions (FRBLUfrblu)
        
    def testRotateLong(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'oryrbyywwbbobrgrwggrgygwrowoybgoybboywwoyowgrbogrwbrgy'
        theCube = cube.Cube(encodedCube)
        result = theCube.rotate('FRBLUfrblu')
        self.assertEqual(expectedResult, result)
        
        
        
#Sad Path
#Null cube       
    def testOneDirEmptyCube(self):
        encodedCube = ''
        expectedResult = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwwwwooorrryyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        theCube = cube.Cube(encodedCube)
        self.assertEqual('error: invalid cube', theCube.get())
        
# Cube too short        
    def testOneDirShortCube(self):
        encodedCube = 'gg'
        expectedResult = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwwwwooorrryyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        theCube = cube.Cube(encodedCube)
        self.assertEqual('error: invalid cube', theCube.get())
 
# Cube too long       
    def testOneDirLongCube(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyygrb'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        theCube = cube.Cube(encodedCube)
        self.assertEqual('error: invalid cube', theCube.get())
        
# Cube has ' ' as characters       
    def testCubeEmptyChar(self):
        encodedCube = 'bbbbbbbbb         rrrrrrrrroooooooooyyyyyyyyywwwwwwwww'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        theCube = cube.Cube(encodedCube)
        self.assertEqual('error: invalid cube', theCube.get())
        
# Cube does not have 9 of valid characters       
    def testCubeNonNine(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwb'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        theCube = cube.Cube(encodedCube)
        self.assertEqual('error: invalid cube', theCube.get())
        
# Non unique cube (5th and 14th match) 
    def testCubeNonUnique(self):
        encodedCube = 'gggggggggrrrrgrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        theCube = cube.Cube(encodedCube)
        self.assertEqual('error: invalid cube', theCube.get())
        
# Non unique cube (5th and 23rd match)        
    def testCubeNonUnique2(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbgbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        theCube = cube.Cube(encodedCube)
        self.assertEqual('error: invalid cube', theCube.get())
   
# Non unique cube (5th and 32nd match)     
    def testCubeNonUnique3(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbboooogoooowwwwwwwwwyyyyyyyyy'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        theCube = cube.Cube(encodedCube)
        self.assertEqual('error: invalid cube', theCube.get())
     
# Non unique cube (5th and 41st match)   
    def testCubeNonUnique4(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwgwwwwyyyyyyyyy'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        theCube = cube.Cube(encodedCube)
        self.assertEqual('error: invalid cube', theCube.get())
        
# Non unique cube (5th and 50th match)
    def testCubeNonUnique5(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyygyyyy'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        theCube = cube.Cube(encodedCube)
        self.assertEqual('error: invalid cube', theCube.get())
        
# Non unique cube (14th and 23rd match)
    def testCubeNonUnique6(self):
        encodedCube = 'gggggggggrrrrrrrrrbbbbrbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        theCube = cube.Cube(encodedCube)
        self.assertEqual('error: invalid cube', theCube.get())



#_init_ tests
#Happy path

# Normal cube
    def testNominalCube(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        theCube = cube.Cube(encodedCube)
        result = theCube.cube
        self.assertEqual(expectedResult, result)
        
#Sad path tests
#None since _init_ has to return none
#Cube error checking done in rotate.py
#See error checking tests in rotateTest.py

#get tests
#Happy path

    def testGet(self):
        encodedCube = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        expectedResult = 'orygbbyrbbyowrgrowwgoogrrwggogbowroowybwybygrbywywbyrg'
        theCube = cube.Cube(encodedCube)
        result = theCube.get()
        self.assertEqual(expectedResult, result)
        
#No sad path, cube is checked when initialized and rotated
    