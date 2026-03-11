def int_checker(to_check):
    """integer_checker to see if your equal to or more than 13 """

    while True:
        error = "please enter a numer that is 1 or more:"

        # check for infinte mode
        if to_check == "":
            return "infinite"


        try:
            response = int(to_check)

            if response < 1:
                # print(error)
                return "invalid"
            else:
                return response
        
        except ValueError:
                # print(error)
                return "invalid"



# Automated testing is below in the form (test_case, expected_value)
to_test = [
    ('xlii' ,'invalid'),
    ('0','invalid'),
    ('0.5' ,'invalid'),
    (1 ,1),
    (2 ,2),
    ('','infinite'),
]

# run tests!
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = int_checker(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")