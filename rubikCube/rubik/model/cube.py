from rubik.model.constants import *

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        result = {}
        #Cube validation
        cubeLength = 54
        if len(encodedCube) != cubeLength:
            self.cube = 'error: invalid cube'
            return
        if (encodedCube.isalnum() == False):
            self.cube = 'error: invalid cube'
            return
        if ' ' in encodedCube:
            self.cube = 'error: invalid cube'
            return
        for char in encodedCube:
            if encodedCube.count(char) != 9:
                self.cube = 'error: invalid cube'
                return
    
        #Cube has correct amount of chars, make variable for shorter error checking
        inputCube = encodedCube
    
        #Checking for non-unique 5th, 14th, 23rd, 32nd, 41st, and 50th chars
        if (inputCube[FMM] == inputCube[RMM] or inputCube[FMM] == inputCube[BMM]
            or inputCube[FMM] == inputCube[LMM] or inputCube[FMM] == inputCube[UMM] 
            or inputCube[FMM] == inputCube[DMM]):
            self.cube = 'error: invalid cube'
            return 
        if (inputCube[RMM] == inputCube[BMM] or inputCube[RMM] == inputCube[LMM]
            or inputCube[RMM] == inputCube[UMM] or inputCube[RMM] == inputCube[DMM]):
            self.cube = 'error: invalid cube'
            return 
        if (inputCube[BMM] == inputCube[LMM] or inputCube[BMM] == inputCube[UMM]
            or inputCube[BMM] == inputCube[DMM]):
            self.cube = 'error: invalid cube'
            return
        if inputCube[LMM] == inputCube[UMM] or inputCube[LMM] == inputCube[49]:
            self.cube = 'error: invalid cube'
            return
        if inputCube[UMM] == inputCube[DMM]:
            self.cube = 'error: invalid cube'
            return 
        self.cube = encodedCube
        
    
    
    #Iterate through the directions and call utility methods
    def rotate(self, directions):
        for d in directions:
            if (d == 'F'):
                self._Frotate()
            elif (d == 'f'):
                self._frotate()
            elif (d == 'R'):
                self._Rrotate()
            elif (d == 'r'):
                self._rrotate()
            elif (d == 'B'):
                self._Brotate()
            elif (d == 'b'):
                self._brotate()
            elif (d == 'L'):
                self._Lrotate()
            elif (d == 'l'):
                self._lrotate()
            elif (d == 'U'):
                self._Urotate()
            elif (d == 'u'):
                self._urotate()
            else: #just a extra precaution, shouldn't be needed
                return 'error: invalid direction'
        return self.cube
        
    
    def get(self):
        return self.cube
    
    
    #Rotate functions
    
    #All numbers in comments before rotate methods are
    #the index switches for that specific rotation
    
    # 0 to 2
    # 1 to 5
    # 2 to 8
    # 5 to 7
    # 8 to 6
    # 7 to 3
    # 6 to 0
    # 3 to 1
    # 35 to 42
    # 32 to 43
    # 29 to 44
    # 42 to 9
    # 43 to 12
    # 44 to 15
    # 9 to 47
    # 12 to 46
    # 15 to 45
    # 47 to 35
    # 46 to 32
    # 45 to 29
    # 
    def _Frotate(self):
        original = list(self.cube)
        postList = original[:]
        postList[FTR] = original[FTL]
        postList[FMR] = original[FTM]
        postList[FBR] = original[FTR]
        postList[FBM] = original[FMR]
        postList[FBL] = original[FBR]
        postList[FML] = original[FBM]
        postList[FTL] = original[FBL]
        postList[FTM] = original[FML]
        postList[UBL] = original[LBR]
        postList[UBM] = original[LMR]
        postList[UBR] = original[LTR]
        postList[RTL] = original[UBL]
        postList[RML] = original[UBM]
        postList[RBL] = original[UBR]
        postList[DTR] = original[RTL]
        postList[DTM] = original[RML]
        postList[DTL] = original[RBL]
        postList[LBR] = original[DTR]
        postList[LMR] = original[DTM]
        postList[LTR] = original[DTL]
        self.cube = "".join(postList)
        return self

    # 2 to 0
    # 5 to 1
    # 8 to 2
    # 7 to 5
    # 6 to 8
    # 3 to 7
    # 0 to 6
    # 1 to 3
    # 42 to 35
    # 43 to 32
    # 44 to 29
    # 9 to 42
    # 12 to 43
    # 15 to 44
    # 47 to 9
    # 46 to 12
    # 45 to 15
    # 35 to 47
    # 32 to 46
    # 29 to 45
    # 
    def _frotate(self):
        original = list(self.cube)
        postList = original[:]
        postList[FTL] = original[FTR]
        postList[FTM] = original[FMR]
        postList[FTR] = original[FBR]
        postList[FMR] = original[FBM]
        postList[FBR] = original[FBL]
        postList[FBM] = original[FML]
        postList[FBL] = original[FTL]
        postList[FML] = original[FTM]
        postList[LBR] = original[UBL]
        postList[LMR] = original[UBM]
        postList[LTR] = original[UBR]
        postList[UBL] = original[RTL]
        postList[UBM] = original[RML]
        postList[UBR] = original[RBL]
        postList[RTL] = original[DTR]
        postList[RML] = original[DTM]
        postList[RBL] = original[DTL]
        postList[DTR] = original[LBR]
        postList[DTM] = original[LMR]
        postList[DTL] = original[LTR]
        self.cube = "".join(postList)
        return self.cube
    
    # 9 to 11
    # 10 to 14
    # 11 to 17
    # 14 to 16
    # 17 to 15
    # 16 to 12
    # 15 to 9
    # 12 to 10
    # 44 to 18
    # 41 to 21
    # 38 to 24
    # 18 to 53
    # 21 to 50
    # 24 to 47
    # 53 to 8
    # 50 to 5
    # 47 to 2
    # 2 to 38
    # 5 to 41
    # 8 to 44
    #
    def _Rrotate(self):
        original = list(self.cube)
        postList = original[:]
        postList[RTR] = original[RTL]
        postList[RMR] = original[RTM]
        postList[RBR] = original[RTR]
        postList[RBM] = original[RMR]
        postList[RBL] = original[RBR]
        postList[RML] = original[RBM]
        postList[RTL] = original[RBL]
        postList[RTM] = original[RML]
        postList[BTL] = original[UBR]
        postList[BML] = original[UMR]
        postList[BBL] = original[UTR]
        postList[DBR] = original[BTL]
        postList[DMR] = original[BML]
        postList[DTR] = original[BBL]
        postList[FBR] = original[DBR]
        postList[FMR] = original[DMR]
        postList[FTR] = original[DTR]
        postList[UTR] = original[FTR]
        postList[UMR] = original[FMR]
        postList[UBR] = original[FBR]
        self.cube = "".join(postList)
        return self.cube
    
    # 11 to 9
    # 14 to 10
    # 17 to 11
    # 16 to 14
    # 15 to 17
    # 12 to 16
    # 9 to 15
    # 10 to 12
    # 18 to 44
    # 21 to 41
    # 24 to 38
    # 53 to 18
    # 50 to 21
    # 47 to 24
    # 8 to 53
    # 5 to 50
    # 2 to 47
    # 38 to 2
    # 41 to 5
    # 44 to 8
    #
    def _rrotate(self):
        original = list(self.cube)
        postList = original[:]
        postList[RTL] = original[RTR]
        postList[RTM] = original[RMR]
        postList[RTR] = original[RBR]
        postList[RMR] = original[RBM]
        postList[RBR] = original[RBL]
        postList[RBM] = original[RML]
        postList[RBL] = original[RTL]
        postList[RML] = original[RTM]
        postList[UBR] = original[BTL]
        postList[UMR] = original[BML]
        postList[UTR] = original[BBL]
        postList[BTL] = original[DBR]
        postList[BML] = original[DMR]
        postList[BBL] = original[DTR]
        postList[DBR] = original[FBR]
        postList[DMR] = original[FMR]
        postList[DTR] = original[FTR]
        postList[FTR] = original[UTR]
        postList[FMR] = original[UMR]
        postList[FBR] = original[UBR]
        self.cube = "".join(postList)
        return self.cube
    
    # 18 to 20
    # 19 to 23
    # 20 to 26
    # 23 to 25
    # 26 to 24
    # 25 to 21
    # 24 to 18
    # 21 to 19
    # 36 to 33
    # 37 to 30
    # 38 to 27
    # 33 to 53
    # 30 to 52
    # 27 to 51
    # 53 to 11
    # 52 to 14
    # 51 to 17
    # 11 to 36
    # 14 to 37
    # 17 to 38
    #
    def _Brotate(self):
        original = list(self.cube)
        postList = original[:]
        postList[BTR] = original[BTL]
        postList[BMR] = original[BTM]
        postList[BBR] = original[BTR]
        postList[BBM] = original[BMR]
        postList[BBL] = original[BBR]
        postList[BML] = original[BBM]
        postList[BTL] = original[BBL]
        postList[BTM] = original[BML]
        postList[LBL] = original[UTL]
        postList[LML] = original[UTM]
        postList[LTL] = original[UTR]
        postList[DBR] = original[LBL]
        postList[DBM] = original[LML]
        postList[DBL] = original[LTL]
        postList[RTR] = original[DBR]
        postList[RMR] = original[DBM]
        postList[RBR] = original[DBL]
        postList[UTL] = original[RTR]
        postList[UTM] = original[RMR]
        postList[UTR] = original[RBR]
        self.cube = "".join(postList)
        return self.cube
    
    # 20 to 18
    # 23 to 19
    # 26 to 20
    # 25 to 23
    # 24 to 26
    # 21 to 25
    # 18 to 24
    # 19 to 21
    # 33 to 36
    # 30 to 37
    # 27 to 38
    # 53 to 33
    # 52 to 30
    # 51 to 27
    # 11 to 53
    # 14 to 52
    # 17 to 51
    # 36 to 11
    # 37 to 14
    # 38 to 17
    #
    def _brotate(self):
        original = list(self.cube)
        postList = original[:]
        postList[BTL] = original[BTR]
        postList[BTM] = original[BMR]
        postList[BTR] = original[BBR]
        postList[BMR] = original[BBM]
        postList[BBR] = original[BBL]
        postList[BBM] = original[BML]
        postList[BBL] = original[BTL]
        postList[BML] = original[BTM]
        postList[UTL] = original[LBL]
        postList[UTM] = original[LML]
        postList[UTR] = original[LTL]
        postList[LBL] = original[DBR]
        postList[LML] = original[DBM]
        postList[LTL] = original[DBL]
        postList[DBR] = original[RTR]
        postList[DBM] = original[RMR]
        postList[DBL] = original[RBR]
        postList[RTR] = original[UTL]
        postList[RMR] = original[UTM]
        postList[RBR] = original[UTR]
        self.cube = "".join(postList)
        return self.cube
    
    # 27 to 29
    # 28 to 32
    # 29 to 35
    # 32 to 34
    # 35 to 33
    # 34 to 30
    # 33 to 27
    # 30 to 28
    # 42 to 6
    # 39 to 3
    # 36 to 0
    # 6 to 51
    # 3 to 48
    # 0 to 45
    # 51 to 20
    # 48 to 23
    # 45 to 26
    # 20 to 42
    # 23 to 39
    # 26 to 36
    #
    def _Lrotate(self):
        original = list(self.cube)
        postList = original[:]
        postList[LTR] = original[LTL]
        postList[LMR] = original[LTM]
        postList[LBR] = original[LTR]
        postList[LBM] = original[LMR]
        postList[LBL] = original[LBR]
        postList[LML] = original[LBM]
        postList[LTL] = original[LBL]
        postList[LTM] = original[LML]
        postList[FBL] = original[UBL]
        postList[FML] = original[UML]
        postList[FTL] = original[UTL]
        postList[DBL] = original[FBL]
        postList[DML] = original[FML]
        postList[DTL] = original[FTL]
        postList[BTR] = original[DBL]
        postList[BMR] = original[DML]
        postList[BBR] = original[DTL]
        postList[UBL] = original[BTR]
        postList[UML] = original[BMR]
        postList[UTL] = original[BBR]
        self.cube = "".join(postList)
        return self.cube
    
    # 29 to 27
    # 32 to 28
    # 35 to 29
    # 34 to 32
    # 33 to 35
    # 30 to 34
    # 27 to 33
    # 28 to 30
    # 6 to 42
    # 3 to 39
    # 0 to 36
    # 51 to 6
    # 48 to 3
    # 45 to 0
    # 20 to 51
    # 23 to 48
    # 26 to 45
    # 42 to 20
    # 39 to 23
    # 36 to 26
    #
    def _lrotate(self):
        original = list(self.cube)
        postList = original[:]
        postList[LTL] = original[LTR]
        postList[LTM] = original[LMR]
        postList[LTR] = original[LBR]
        postList[LMR] = original[LBM]
        postList[LBR] = original[LBL]
        postList[LBM] = original[LML]
        postList[LBL] = original[LTL]
        postList[LML] = original[LTM]
        postList[UBL] = original[FBL]
        postList[UML] = original[FML]
        postList[UTL] = original[FTL]
        postList[FBL] = original[DBL]
        postList[FML] = original[DML]
        postList[FTL] = original[DTL]
        postList[DBL] = original[BTR]
        postList[DML] = original[BMR]
        postList[DTL] = original[BBR]
        postList[BTR] = original[UBL]
        postList[BMR] = original[UML]
        postList[BBR] = original[UTL]
        self.cube = "".join(postList)
        return self.cube
    
    # 36 to 38
    # 37 to 41
    # 38 to 44
    # 41 to 43
    # 44 to 42
    # 43 to 39
    # 42 to 36
    # 39 to 37
    # 27 to 18
    # 28 to 19
    # 29 to 20
    # 18 to 9
    # 19 to 10
    # 20 to 11
    # 9 to 0
    # 10 to 1
    # 11 to 2
    # 0 to 27
    # 1 to 28
    # 2 to 29
    #
    def _Urotate(self):
        original = list(self.cube)
        postList = original[:]
        postList[UTR] = original[UTL]
        postList[UMR] = original[UTM]
        postList[UBR] = original[UTR]
        postList[UBM] = original[UMR]
        postList[UBL] = original[UBR]
        postList[UML] = original[UBM]
        postList[UTL] = original[UBL]
        postList[UTM] = original[UML]
        postList[BTL] = original[LTL]
        postList[BTM] = original[LTM]
        postList[BTR] = original[LTR]
        postList[RTL] = original[BTL]
        postList[RTM] = original[BTM]
        postList[RTR] = original[BTR]
        postList[FTL] = original[RTL]
        postList[FTM] = original[RTM]
        postList[FTR] = original[RTR]
        postList[LTL] = original[FTL]
        postList[LTM] = original[FTM]
        postList[LTR] = original[FTR]
        self.cube = "".join(postList)
        return self.cube
    
    # 38 to 36
    # 41 to 37
    # 44 to 38
    # 43 to 41
    # 42 to 44
    # 39 to 43
    # 36 to 42
    # 37 to 39
    # 18 to 27
    # 19 to 28
    # 20 to 29
    # 9 to 18
    # 10 to 19
    # 11 to 20
    # 0 to 9
    # 1 to 10
    # 2 to 11
    # 27 to 0
    # 28 to 1
    # 29 to 2
    #
    def _urotate(self):
        original = list(self.cube)
        postList = original[:]
        postList[UTL] = original[UTR]
        postList[UTM] = original[UMR]
        postList[UTR] = original[UBR]
        postList[UMR] = original[UBM]
        postList[UBR] = original[UBL]
        postList[UBM] = original[UML]
        postList[UBL] = original[UTL]
        postList[UML] = original[UTM]
        postList[LTL] = original[BTL]
        postList[LTM] = original[BTM]
        postList[LTR] = original[BTR]
        postList[BTL] = original[RTL]
        postList[BTM] = original[RTM]
        postList[BTR] = original[RTR]
        postList[RTL] = original[FTL]
        postList[RTM] = original[FTM]
        postList[RTR] = original[FTR]
        postList[FTL] = original[LTL]
        postList[FTM] = original[LTM]
        postList[FTR] = original[LTR]
        self.cube = "".join(postList)
        return self.cube
    
    
    
    
        