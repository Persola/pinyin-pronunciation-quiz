from textwrap import dedent
import random

from syllables import syllables
from initials import initials
from finals import finals

syllables_as_pinyin = [s['pinyin'] for s in syllables]
if len(syllables_as_pinyin) != len(set(syllables_as_pinyin)):
    raise Exception('The syllable list has at least one duplicate entry')

def answer(question_syllable):
    return(
        dedent(f'''
            initial
                pinyin: {initials[question_syllable['initial']]['pinyin']}
                IPA: {initials[question_syllable['initial']]['IPA']}
                classification: {initials[question_syllable['initial']]['classification']}
                hint: {initials[question_syllable['initial']]['hint']}
            final: ({finals[question_syllable['final']]})
        ''')
    )

while(True):
    question_syllable = random.choice(list(syllables))
    input(f'\n\n{question_syllable["pinyin"]}\n')
    print(answer(question_syllable))
