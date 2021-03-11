def newRoadSystem(roadRegister):
    for x, y in zip(map(sum, roadRegister), map(sum, zip(*roadRegister))):
        if x != y:
            return False
    return True
