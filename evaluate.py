import json, os
from pathlib import Path
import argparse
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score, classification_report

valid_labels = ['neutral', 'joy', 'sadness', 'anger']

def evaluate(true, pred):
    y_true = []
    y_pred = []
    # flatten records
    true = [line for dialogue in true for line in dialogue]
    pred = [line for dialogue in pred for line in dialogue]


    if len(true) != len(pred):
        raise Exception('Number of utternaces in true ({}) different from pred ({})'.format(len(true), len(pred)))

    for i in range(0, len(true)):
        if true[i]['emotion'] not in valid_labels:
            # discard utterances with labels different from valid_labels
            continue

        if pred[i]['emotion'] not in valid_labels:
            raise Exception("Unexpected emotion: expected one of '{}', got '{}'".format(' '.join(valid_labels), pred[i]['emotion']))

        if true[i]['utterance'] != pred[i]['utterance']:
            raise Exception("Utterance mismatch: expected '{}' but got '{}'".format(true[i]['utterance'], pred[i]['utterance']))

        y_true.append(true[i]['emotion'])
        y_pred.append(pred[i]['emotion'])

    # sanity check
    if len(y_true) != len(y_pred):
        raise Exception('Internal error: different lengths for y_true, y_pred')

    results = dict()
    results['f1-micro'] = f1_score(y_true, y_pred, labels=valid_labels, average="micro")
    results['classification_report'] = classification_report(y_true, y_pred, labels=valid_labels, digits=3)

    return results

def print_report(results, isjson):
        if isjson:
            print(json.dumps(results, indent=4))
        else:
            if 'title' in report:
                print(report['title'])
            print("{} ({})".format(results['name'], results['email']))
            print('f1-micro: {:.1f}%\n'.format(results['f1-micro'] * 100))
            print(results['classification_report'])

def write_report(goldfile, predfile, title):
        gold = json.load(goldfile)
        identity, pred = json.load(predfile)
        name = identity['name']
        email = identity['email']

        results = evaluate(gold, pred)

        results['email'] = email
        results['name'] = name
        if title:
            results['title'] = title
        return results

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--title', type=str, help="optional report title")
    parser.add_argument("--json", action='store_true', help='return results in JSON format')
    parser.add_argument('--goldfile', required=True, type=argparse.FileType('r'), help="file with gold labels")
    parser.add_argument('--predfile', required=True, type=argparse.FileType('r'), help="file with predicted labels")

    args = parser.parse_args()

    report = write_report(args.goldfile, args.predfile, args.title)
    print_report(report, args.json)
