# Evaluating Machine Translation

A comprehensive pipeline for evaluating the quality of Machine Translation (MT) models using the FLORES dataset. This repository implements and compares various evaluation metrics to assess translation performance against reference datasets.

## Overview

 the representation of low-resource languages has long been hindered by the lack of
contextual and meaningful content that could help train large language models to deal with the translation of these
languages. Over the last few years, great strides have been made in trying to address this problem. One such stride
has been made by the University of Pretoria’s Data Science For Social Impact (DSFSI) research group with the
FLORES dataset for low-resource languages. The full dataset covers 101 to 200 languages and has been a valuable
resource in addressing the matter at hand; it has, however, also suffered from its bottlenecks. The dataset did well in
training models; however, models still showed signs of struggling with more convoluted phrases and words. The
DSFSI did see this problem and has since started to address it. They did s by providing deeper context to 4 African
low-resource languages: Xitsonga, Sepedi, Isizulu, and Hausa. Despite these significant advancements, it remains
crucial to assess these languages before applying the adaptations to other languages (Abdulmumin et al., 2024,
570). In this paper, we will be evaluating the corrections made to these four languages on the FLORES dataset.

## Features

*   **Lexical Metrics:** Implementation/integration of standard string-matching metrics:
    *   **BLEU** (Bilingual Evaluation Understudy) — measures n-gram precision.
    *   **TER** (translation edit rate) — measures n-gram recall (useful if looking at ROUGE-L).
*   **Semantic/Embedding Metrics:** Integration of modern trained metrics like **BERTScore** or **COMET** to capture semantic similarity beyond exact word matches.
    *   **COMET** (Crosslingual Optimized Metric for Evaluation of Translation) — includes stemming and synonym matching.

## Project Structure

```text
├── data/                  # Sample source, reference, and candidate translation files
│   ├── corrected/
│   │   ├── dev/
|   │   │   ├── hau_Latn.dev
|   │   │   ├── nso_Latn.dev
|   │   │   ├── zul_Latn.dev
|   │   |   └── .DS_Store
│   |   └── devtest/
|   │   │   ├── hau_Latn.devtest
|   │   │   ├── nso_Latn.devtest
|   │   │   ├── zul_Latn.devtest
|   │   │   ├── tso_Latn.devtest
|   │   |   └── .DS_Store
│   ├── original/
│   │   ├── dev/
|   │   │   ├── eng_Latn.dev
|   │   │   ├── hau_Latn.dev
|   │   │   ├── nso_Latn.dev
|   │   │   ├── zul_Latn.dev
|   │   |   └── tso_Latn.dev
│   |   └── devtest/
|   │   │   ├── eng_Latn.devtest
|   │   │   ├── hau_Latn.devtest
|   │   │   ├── nso_Latn.devtest
|   │   │   ├── zul_Latn.devtest
|   │   |   └── tso_Latn.devtest
│   ├── mon/
│   │   ├── corrected-nso.txt
│   │   ├── english_sentences.txt
│   │   ├── gemini-nso-sentences.txt
│   |   └── gpt-nso-sentences.txt
│   ├── wandile/
│   │   ├── Wandile_tsonga.txt
│   │   ├── english.txt
│   │   ├── gemini_xitsonga.txt
│   |   └── gpt_xitsonga.txt
├── scripts/                   # Source code for evaluation
│   ├── download_nltk_data.py      # Text normalization and tokenization pipeline
│   ├── compute_metrics.py         # Implementations/wrappers for evaluation metrics
│   ├── compute_metrics.ipynb         # Implementations/wrappers for evaluation metrics
|   ├── requirements.txt          # Python dependencies
│   └── utils.py        # Main execution script to run the evaluation
├── .gitignore
└── README.md
