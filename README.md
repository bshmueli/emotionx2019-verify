# verify.py
`verify.py` is a utility to verify your EmotionX 2019 submission file and make sure it's in the correct format.

To use, simply run:

`% python3 verify.py --testfile testfile.json --predfile predfile.json`

where

`testfile.json` is the **unlabeled** test file

`predfile.json` is your submission file (with predicted labels)

For example, for the Friends dataset, use:
`% python3 verify.py --testfile friends_eval.json --predfile friends_pred.json`

## Misc.
If Python complains about a missing module, install it using `pip` (or `pip3`).
