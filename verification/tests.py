expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

expected_cowsay_with_multiple_spaces = r'''
 ________________________
<  With multiple spaces  >
 ------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''


cowsay_one_line =  'Checkio rulezz'
cowsay_two_lines =  'A longtextwithonlyonespacetofittwolines.'
cowsay_many_lines = ('Lorem ipsum dolor sit amet, consectetur adipisicing elit, '
                     'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
cowsay_with_multiple_spaces = '    With  multiple  spaces                                     '

TESTS = {
    "Basics": [
        {
            "input": [cowsay_one_line],
            "answer": expected_cowsay_one_line,
        },
        {
            "input": [cowsay_two_lines],
            "answer": expected_cowsay_two_lines,
        },
        {
            "input": [cowsay_many_lines],
            "answer": expected_cowsay_many_lines,
        },
        {
            "input": [cowsay_with_multiple_spaces],
            "answer": expected_cowsay_with_multiple_spaces
        }
    ]
}
