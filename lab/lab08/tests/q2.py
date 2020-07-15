test = {   'name': 'q2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> expected_l1 = np.array([0.10227265, 0.08448833, 0.38589475, 0.14509879, 0.46657416, 0.12471279, \n'
                                               '...                         0.24412693, 0.08026188, 0.21553762, 0.08644451, 0.12967361, 0.08278544]);\n'
                                               '>>> actual_l1 = np.array(minimize_average_loss(l1, linear_model, one_hot_X, tips));\n'
                                               '>>> np.isclose(one_hot_X @ expected_l1, one_hot_X @ actual_l1, rtol=0.1).all()\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> expected_l2 = np.array([ 0.09448698, 0.17599641, 0.49807344, 0.37660412, 0.47259411, 0.33577291,\n'
                                               '...                         -0.04567687, -0.07812309, 0.48733616, 0.40093077, -0.13592022, -0.06775829]);\n'
                                               '>>> actual_l2 = np.array(minimize_average_loss(l2, linear_model, one_hot_X, tips));\n'
                                               '>>> np.isclose(one_hot_X @ expected_l2, one_hot_X @ actual_l2, rtol=0.001).all()\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
