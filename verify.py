import json
import argparse

valid_labels = ['joy', 'sadness', 'anger', 'neutral']

def verify_one_dialogue(dialogue_no, test, pred):
    n_lines = len(test)
    assert n_lines == len(pred), "Dialogue {}: Number of utterances in test file ({}) different from pred file ({}).".format(dialogue_no, n_lines, len(pred))
    for line_no in range(0, n_lines):
        assert 'utterance'   in test[line_no], "Dialogue {}, line {}: missing utterance in test file.".format(dialogue_no, line_no)
        assert 'speaker'     in test[line_no], "Dialogue {}, line {}: missing speaker in test file.".format(dialogue_no, line_no)
        assert 'emotion' not in test[line_no], "Dialogue {}, line {}: emotion present in test file.".format(dialogue_no, line_no)
        assert 'utterance'   in pred[line_no], "Dialogue {}, line {}: missing utterance in pred file.".format(dialogue_no, line_no)
        assert 'speaker'     in pred[line_no], "Dialogue {}, line {}: missing speaker in pred file.".format(dialogue_no, line_no)
        assert 'emotion'     in pred[line_no], "Dialogue {}, line {}: missing emotion in pred file.".format(dialogue_no, line_no)
        assert test[line_no]['utterance'] == pred[line_no]['utterance'], "Dialogue {}, line {}: utterance mismatch in pred file, expected '{}', got '{}'.".format(dialogue_no, line_no, test[line_no]['utterance'], pred[line_no]['utterance'])
        assert test[line_no]['speaker'] == pred[line_no]['speaker'], "Dialogue {}, line {}: speaker mismatch in pred file, expected '{}', got '{}'.".format(dialogue_no, line_no, test[line_no]['speaker'], pred[line_no]['speaker'])
        assert pred[line_no]['emotion'] in valid_labels, "Dialogue {}, line {}: unexpected emotion: expected one of [{}], got '{}'.".format(dialogue_no, line_no, ', '.join(valid_labels), pred[line_no]['emotion'])

def verify_all_dialogues(test, pred):
  n_dialogues = len(test)
  assert n_dialogues == len(pred), 'Number of dialogues in test file ({}) different from pred file ({})'.format(n_dialogues, len(pred))

  for dialogue_no in range(0, n_dialogues):
    verify_one_dialogue(dialogue_no, test[dialogue_no], pred[dialogue_no])

def verify_files(testfile, predfile):
    test = json.load(testfile)
    ident_and_pred = json.load(predfile)

    assert len(ident_and_pred) == 2, 'Bad file format: top-level array should include exactly two items (the identifier, dialogues with predictions)'

    ident, pred = ident_and_pred
    assert 'name' in ident, '"name" value is missing from the identifier.'
    name = ident['name']

    assert 'email' in ident, '"email" value is missing from the identifier.'
    email = ident['email']

    print("Submission is by {} ({})".format(name, email))

    verify_all_dialogues(test, pred)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--testfile', required=True, type=argparse.FileType('r'), help="the original evaluation file (without labels)")
    parser.add_argument('--predfile', required=True, type=argparse.FileType('r'), help="your submission file (with predicted labels)")
    args = parser.parse_args()
    verify_files(args.testfile, args.predfile)
    print('Your file complies with the required submission format. Congratulations!')
