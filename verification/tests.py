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

expected_cowsay_two_lines_simple = r'''
 _____________________________
/ onehundredtwentytwo and one \
\ hundredfiftyone             /
 -----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

expected_cowsay_two_lines_with_small_start = r'''
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


expected_cowsay_dzen = r'''
 _________________________________________
/ Gur Mra bs Clguba, ol Gvz Crgref        \
| Ornhgvshy vf orggre guna htyl. Rkcyvpvg |
| vf orggre guna vzcyvpvg. Fvzcyr vf      |
| orggre guna pbzcyrk. Pbzcyrk vf orggre  |
| guna pbzcyvpngrq. Syng vf orggre guna   |
| arfgrq. Fcnefr vf orggre guna qrafr.    |
| Ernqnovyvgl pbhagf. Fcrpvny pnfrf nerag |
| fcrpvny rabhtu gb oernx gur ehyrf.      |
| Nygubhtu cenpgvpnyvgl orngf chevgl.     |
| Reebef fubhyq arire cnff fvyragyl.      |
| Hayrff rkcyvpvgyl fvyraprq. Va gur snpr |
| bs nzovthvgl, ershfr gur grzcgngvba gb  |
| thrff. Gurer fubhyq or bar-- naq        |
| cersrenoyl bayl bar --boivbhf jnl gb qb |
| vg. Nygubhtu gung jnl znl abg or        |
| boivbhf ng svefg hayrff lbher Qhgpu.    |
| Abj vf orggre guna arire. Nygubhtu      |
| arire vf bsgra orggre guna *evtug* abj. |
| Vs gur vzcyrzragngvba vf uneq gb        |
| rkcynva, vgf n onq vqrn. Vs gur         |
| vzcyrzragngvba vf rnfl gb rkcynva, vg   |
| znl or n tbbq vqrn. Anzrfcnprf ner bar  |
| ubaxvat terng vqrn -- yrgf qb zber bs   |
\ gubfr!                                  /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

cowsay_one_line =  'Checkio rulezz'
cowsay_two_lines_simple = 'onehundredtwentytwo and one hundredfiftyone'
cowsay_two_lines_with_small_start = 'A longtextwithonlyonespacetofittwolines.'
cowsay_many_lines = ('Lorem ipsum dolor sit amet, consectetur adipisicing elit, '
                     'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
cowsay_with_multiple_spaces = '    With  multiple  spaces                                     '
cowsay_dzen = """Gur Mra bs Clguba, ol Gvz Crgref  Ornhgvshy vf orggre guna htyl. Rkcyvpvg vf orggre guna vzcyvpvg. Fvzcyr vf orggre guna pbzcyrk. Pbzcyrk vf orggre guna pbzcyvpngrq. Syng vf orggre guna arfgrq. Fcnefr vf orggre guna qrafr. Ernqnovyvgl pbhagf. Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf. Nygubhtu cenpgvpnyvgl orngf chevgl. Reebef fubhyq arire cnff fvyragyl. Hayrff rkcyvpvgyl fvyraprq. Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff. Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg. Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu. Abj vf orggre guna arire. Nygubhtu arire vf bsgra orggre guna *evtug* abj. Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn. Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn. Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""
TESTS = {
    "Basics": [
        {
            "input": cowsay_one_line,
            "answer": expected_cowsay_one_line,
        },
        {
            "input": cowsay_two_lines_simple,
            "answer": expected_cowsay_two_lines_simple,
        },
        {
            "input": cowsay_two_lines_with_small_start,
            "answer": expected_cowsay_two_lines_with_small_start,
        },
        {
            "input": cowsay_many_lines,
            "answer": expected_cowsay_many_lines,
        },
        {
            "input": cowsay_with_multiple_spaces,
            "answer": expected_cowsay_with_multiple_spaces
        },
        {
            "input": cowsay_dzen,
            "answer": expected_cowsay_dzen
        },
    ]
}
