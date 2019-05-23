# evaluate.py

`evaluate.py` is a utility to evaluate your EmotionX 2019 submission file and calculate the model's performance.

To use, simply run:

`% python3 evaluate.py --goldfile goldfile.json --predfile predfile.json`

where

`goldfile.json` is the file with the gold labels

`predfile.json` is your submission file (with predicted labels)

You will need to run it once for every dataset. For example:

`% python3 evaluate.py --goldfile friends_eval_gold.json -predfile friends_pred.json`
`% python3 evaluate.py --goldfile emotionpush_eval_gold.json -predfile emotionpush_pred.json`

# verify.py
`verify.py` is a utility to verify your EmotionX 2019 submission file and make sure it's in the correct format.

To use, simply run:

`% python3 verify.py --testfile testfile.json --predfile predfile.json`

where

`testfile.json` is the **unlabeled** evaluation file

`predfile.json` is your submission file (with predicted labels)

## Misc.
If Python complains about a missing module, install it using pip (or pip3).
