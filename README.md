# verify.py
`verify.py` is a utility to verify your EmotionX 2019 submission file and make sure it's in the correct format.

To use, simply run:

`% python3 verify.py --evalfile eval --predfile pred`

where

`eval` is the **unlabeled** evaluation file in JSON format

`pred` is your submission file (with predicted labels) in JSON format

## Misc.
If Python complains about a missing module, install it using pip (or pip3).
