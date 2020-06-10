import os
from importlib import import_module

test_arrays = [
    [4, 6, 3, 2, 5, 7, 8, 9, 5, 3, 23, 1, 43, 6, 3, 5, 3, 2, 4, 2, 4],
    [1.4, 3.2, 4.2, 4.3, 7.6, 5.4, 3.2, 5.4444444, 5.4, 1.2],
    [
        "dfsdfs",
        "vbnvn",
        "fgsgsd",
        "qweqwe",
        "eqweqwe",
        "qwreqwrqwr",
        "2ewegweg",
        "gerwyery",
        "m.jm,h.hjk.,",
        "dfgsg",
        "",
        " ",
    ],
]

assertion_errors = 0
for sort_files in os.listdir(os.path.dirname(__file__)):
    if "sort.py" not in sort_files:
        continue
    print("=" * 50)
    print("TESTING {}".format(sort_files))
    print("-" * 50)
    file_as_module = import_module(sort_files[:-3])
    sort_function = getattr(file_as_module, "sort")
    for i in range(len(test_arrays)):
        expected_output = sorted(test_arrays[i])
        real_output = sort_function(test_arrays[i])
        try:
            assert expected_output == real_output
        except AssertionError:
            assertion_errors += 1
            print(
                "TEST #{} failed, \n\texpected: {} \n\tfrom input: {} \n\tgot: {}".format(
                    i, expected_output, test_arrays[i], real_output
                )
            )
        print("TEST #{} completed successfully".format(i))

    print("=" * 50)

if assertion_errors == 0:
    print("Zero errors, feel free to create a pull request")
else:
    print("Fix {} errors before creating a pull request".format(assertion_errors))
