"""

Tests for pigify functions

Author(s):
Version:

Skeleton by Lillian Lee (LJL2) and Walker White (wmw2), Feb 2025

"""


import pigify
import cornellasserts 


##### TEST PROCEDURES


def test_pigify():
    print("Running test_pigify to test pigify.pigify()")


    cornellasserts.assert_equals("askhay", pigify.pigify("ask"))
    cornellasserts.assert_equals("usehay", pigify.pigify("use"))
    cornellasserts.assert_equals("ietquay", pigify.pigify("quiet"))
    cornellasserts.assert_equals("ayquay", pigify.pigify("quay"))
    cornellasserts.assert_equals("quay", pigify.pigify("qu"))
    cornellasserts.assert_equals("omatotay", pigify.pigify("tomato"))
    cornellasserts.assert_equals("oolschay", pigify.pigify("school"))
    cornellasserts.assert_equals("ouyay", pigify.pigify("you"))
    cornellasserts.assert_equals("pssstay", pigify.pigify("pssst"))
    cornellasserts.assert_equals("xay", pigify.pigify("x"))

    print("Finished test_pigify")


# CODE TO EXECUTE

print("Beginning tests of pigify code")
test_pigify()
print("All test cases for pigify passed")
