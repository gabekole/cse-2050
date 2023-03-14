# Include your answers for this lab in the dictionary below.
# The keys of the dictionary are the pre-numbered algorithms.
# The values are your answers. Use:
#     'bubble'
#     'selction'
#     'insertion'
#     'merge'
#     'quick'

# #For instance, if you though all the algorithms  were bubble sort (they are not), this file should read:
# answers = {'alg_a': 'bubble',
#            'alg_b': 'bubble',
#            'alg_c': 'bubble',
#            'alg_d': 'bubble',
#            'alg_e': 'bubble'}

# Fill in your answers as the values in the dict below
answers = {'alg_a': 'quick',
           'alg_b': 'merge',
           'alg_c': 'insertion',
           'alg_d': 'selection',
           'alg_e': 'bubble'
          }

valid_ans = {'bubble', 'selection', 'insertion', 'merge', 'quick'}
# Run this file in terminal to see if you used the correct formatting in your answer.
for k, v in answers.items():
    if v not in valid_ans:
        raise ValueError(f"Value '{v}' for key '{k}' is not in {valid_ans}")

print("Valid answer! Find out if it's right after the due date.")