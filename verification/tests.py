expected_cowsay_one_line = r'''
 _______________________________________
< Checkio rulezz                        >
 ---------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
expected_cowsay_two_lines = r'''
 _________________________________________
/ aaaaaaaaaaaaaaaaaaaaaaaafjdhfgjhdfkhdgf \
\ khdgkfdgkfdfjgdljfg                     /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

expected_cowsay_many_lines = r'''
 _______________________________________
/ kdhfjdkfldhf dfjsdfhdskjfh            \
| dfbjdsfkdsjhf dsfbjdskflsdjfhlsdf d   |
| sfjsdfhkdsjhfdsjkf dskjfsdlfhsdlf sdf |
\ lsd flhsd fhlsdf hldsf                /
 ---------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''


cowsay_one_line =  'checkio rulezz'
cowsay_two_lines =  'aaaaaaaaaaaaaaaaaaaaaaaafjdhfgjhdfkhdgfkhdgkfdgkfdfjgdljfg'
cowsay_many_lines = ('kdhfjdkfldhf dfjsdfhdskjfh dfbjdsfkdsjhf dsfbjdskflsdjfhlsdf d sfjsdfhkdsjhfdsjkf  '
                     'dsk jfsdlfhsdlf sdf lsd flhsd fhlsdf hldsf')

TESTS = {
    "Basics": [
        {
            "input": cowsay_one_line,
            "answer": expected_cowsay_one_line,
        },
        {
            "input": cowsay_two_lines,
            "answer": cowsay_two_lines,
        },
        {
            "input": cowsay_many_lines,
            "answer": cowsay_many_lines,
        }
    ]
}
