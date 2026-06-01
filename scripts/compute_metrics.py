import os
import sys
import argparse
from comet import load_from_checkpoint
from utils import compute_metrics, compute_token_counts, compute_token_divergence, display_results, get_comet_model_path, get_different_sentences

COMET_MODEL = get_comet_model_path()

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, help="Path to the prediction file to evaluate")
    return parser.parse_args()

def main():
    args = get_args()
    pred_path = args.file

    # Check if the given file exists
    if not os.path.exists(pred_path):
        sys.exit(f"Error: The file '{pred_path}' does not exist.")

    if not COMET_MODEL:
        sys.exit('COMET model not found at "../comet_model". Please download the model.')

    print(f'COMET model: {COMET_MODEL}')

    model = load_from_checkpoint(COMET_MODEL)

    # Hardcoded reference and source paths (adjust if necessary)
    src_path = '../data/mon/english_sentences.txt'
    ref_path = '../data/mon/corrected-nso.txt'

    src = open(src_path, 'r', encoding='utf-8').read().splitlines()
    ref = open(ref_path, 'r', encoding='utf-8').read().splitlines()
    pred = open(pred_path, 'r', encoding='utf-8').read().splitlines()

    corrected_sentences = get_different_sentences(ref, pred)
    ref = [l[0] for l in corrected_sentences]
    pred = [l[1] for l in corrected_sentences]

    bleu_score, ter_score, comet_score = compute_metrics(src, ref, pred, model)

    # Passing "N/A" for lang_code and split since they are no longer parsed arguments
    display_results("N/A", "N/A", corrected_sentences, src, pred, ref, bleu_score, ter_score, comet_score)

if __name__ == '__main__':
    main()