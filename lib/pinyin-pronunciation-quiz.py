from textwrap import dedent
import random

from syllables import syllables
from initials import initials
from finals import finals

syllables_as_pinyin = [s['pinyin'] for s in syllables]
if len(syllables_as_pinyin) != len(set(syllables_as_pinyin)):
    raise Exception('The syllable list has at least one duplicate entry')

def initial_answer(initial):
    if initial is None:
        return ''

    return(
        (f'''
            initial:
                pinyin: {initial['pinyin']}
                IPA: {initial['IPA']}
                classification: {initial['classification']}
                hint: {initial['hint']}'''
        )
    )

def answer(question_syllable):
    initial = initials[question_syllable['initial']]
    final_pinyin = question_syllable['final']
    final_hint = finals[final_pinyin]

    return(
        dedent(
            f'''{initial_answer(initial)}
            final: {final_pinyin} ({final_hint})'''
        )
    )

while(True):
    question_syllable = random.choice(list(syllables))
    input(f'\n\n\n{question_syllable["pinyin"]}\n')
    print(answer(question_syllable))
