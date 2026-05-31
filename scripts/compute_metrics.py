import os
import sys
import argparse
from comet import load_from_checkpoint
from utils import compute_metrics, compute_token_counts, compute_token_divergence, display_results, get_comet_model_path, get_different_sentences

METADATA = {
  'hau': ['dev', 'devtest'],
  'nso': ['dev', 'devtest'],
  'tso': ['devtest'],
  'zul': ['dev', 'devtest'],
}
COMET_MODEL = get_comet_model_path()

def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-l', '--lang_code', choices=METADATA.keys(), required=True)
  parser.add_argument('-s', '--split', choices=set(value for values in METADATA.values() for value in values), required=True)
  return parser.parse_args()

def main():
  args = get_args()
  lang_code = args.lang_code
  split = args.split

  if not COMET_MODEL:
    sys.exit(f'COMET model not found at "../comet_model". Please download the model.')
  if split not in METADATA[lang_code]:
    sys.exit(f'{lang_code} does not have the split {split}.')

  print(f'COMET model: {COMET_MODEL}')

  model = load_from_checkpoint(COMET_MODEL)

  src_path = f'../data/mon/english_sentences.txt'
  ref_path = f'../data/mon/corrected-nso.txt'
  pred_path = f'../data/mon/gpt-nso-sentences.txt'

  src = open(src_path, 'r', encoding='utf-8').read().splitlines()
  ref = open(ref_path, 'r', encoding='utf-8').read().splitlines()
  pred = open(pred_path, 'r', encoding='utf-8').read().splitlines()

  corrected_sentences = get_different_sentences(ref, pred)
  ref = [l[0] for l in corrected_sentences]
  pred = [l[1] for l in corrected_sentences]

  bleu_score, ter_score, comet_score = compute_metrics(src, ref, pred, model)

  display_results(lang_code, split, corrected_sentences, src, pred, ref, bleu_score, ter_score, comet_score)

if __name__ == '__main__':
  main()