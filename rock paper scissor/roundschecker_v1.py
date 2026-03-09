def integer_checker():
    """integer_checker to see if your equal to or more than 13 """


    error = "please enter a numer more or equle to 13:"

    while True:
        try:
            response = int(input("what is the game goal? "))

            if response < 13:
                print(error)
            else:
                return response
        
        except ValueError:
            print(error)



# Automated testing is below in the form (test_case, expected_value)
to_test = [
    ('xlii' ,'invalid'),
    ('0','invalid'),
    ('0.5' ,'invalid'),
    ('1, 1'),
    ('2, 2'),
    ('<enter>' ,'infinite'),
]

# run tests!
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = integer_checker(case, ["yes", "no"])

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")