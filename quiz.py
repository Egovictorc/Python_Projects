q = {
    '1. Where is the Federal capital of Nigeria?': 'A',
    '2. Which of these is odd in the list?': 'B',
    '3. Abuja is in which part of Nigeria?': 'C',
    '4. Who is the governor of Anambra State?': 'D'
}

options = [
    ['A. Abuja B.Enugu C.Awka D. Lagos'],
    ['A. Abuja B.USA C.Awka D. Lagos'],
    ['A. Abuja B.Enugu C.Awka D. Lagos'],
    ['A. Dave Umahi B.Obiano Wilie C.Peter Obiano D. Soludo']
]

def exam():
    guesses = []
    qn = 1
    cor_gueses = 0
    for k in q:
        print(k)
        for i in options[qn - 1]:
            print(i)
            print('--------------------------------------')
            guess = input('Enter A, B, C or D:')
            guess = guess.upper()
            cor_gueses += check_ans(q.get(k), guess)
    qn += 1
    display_score(cor_gueses, guesses)


def check_ans(ans, guess):
    if ans == guess:
        return 1
        print('Correct!')
    else:
        return 0

def display_score(cor_guesses, guesses):
    print('-------------------------------------------')
    print('Results:')
    print('----------------------------')
    print('Answer:', end='')
    for i in q:
        print(q.get(i), end='')
        print()
        score = int((cor_guesses / len(q) * 100))
    print('Your Score is:', str(score) + '%.')


def retakeexam():
    res = input('Do you want to retake test?(Yes/No)')
    res.upper()
    if res == 'YES':
        return True
    else:
        return False

exam()
while retakeexam:
    exam()
print('Print Byeeee!')