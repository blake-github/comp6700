from rubik.model.cube import Cube

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    
    #Keys Validation
    if len(parms.keys()) > 2:
        result['status'] = 'error: too many keys'
        return result
    if 'cube' not in parms.keys():
        result['status'] = 'error: missing cube key'
        return result
    if (len(parms.keys()) == 2)  and ('dir' not in parms.keys()):
        result['status'] = 'error: invalid key'
        return result
    
    
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    if theCube.get().find('error') != -1:
        result['status'] = theCube.get()
        return result
    
    #Dir valdiation
    acceptableDirs = ['F', 'f', 'R', 'r', 'B', 'b', 'L', 'l', 'U', 'u']
    if 'dir' not in parms.keys():
        directions = 'F'
    elif parms.get('dir') == '':
        directions = 'F' 
    elif not all([i in acceptableDirs for i in parms.get('dir')]):
        result['status'] = 'error: invalid directions'
        return result
    else:
        directions = parms.get('dir')
        
    #If we get here directions are good to go
    #and we can call cube.rotate()
    theCube.rotate(directions)
    
    result['cube'] = theCube.get()
    result['status'] = 'ok'           
    return result
