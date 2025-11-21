class employee:
    def __init__(self):
        print('super discovered')
    def __del__(self):
        print('an omnidroid has eliminated the threat')
def create_obj():
    print('searching for supers')
    obj = employee()
    print('omnidroid completing mission')
    del obj
print('creating new omnidroid')
obj = create_obj()
print('onmidroid v564x testing complete')