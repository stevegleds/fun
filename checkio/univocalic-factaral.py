def a_factaral(nmbr):
    if num == 0:
        return 1
    return num * a_factaral(num - 1)

# this assertion should be stripped after self-testing.
if __name__ == '__main__':
    assert a_factaral(0) == 1, "Zero"
    assert a_factaral(1) == 1, "One"
    assert a_factaral(2) == 2, "Two"
    assert a_factaral(3) == 6, "Six"
    assert a_factaral(100) == \
           93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000, "Infinity"
