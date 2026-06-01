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
    *   **BLEU** (Bilingual Evaluation Understudy) — A basic string matching metric to evaluate the difference between machine-generated translation and high-quality human translation.
    *   **TER** (translation edit rate) — an automated measure of the amount of edits a human would have to make to make a high-quality human-translated translation.
*   **Semantic/Embedding Metrics:** Integration of modern trained metrics like **BERTScore** or **COMET** to capture semantic similarity beyond exact word matches.
    *   **COMET** (Crosslingual Optimized Metric for Evaluation of Translation) — For automatically evaluating the machine translation by calculating the similarity between the machine translation and a reference translation using tokens.
 
## Running Instructions
To run the program, one first needs to cd into the scripts directory, after cloning the repo, run the command:
```console
cd ./scripts
```


Then you need to  install dependencies. To do this, run the install command for all the requirements. This is run with the command:

```console
pip install -r requirements.txt
```
At the moment the code is pointing to the mon subdirectory, which is for Nso. To change the language, create your datasets, and put it in your folder in the data subdirectory, then update the paths in the code. To do this, in the compute_metrics.py file, navigate to lines 35 to 37, change the path to your source language dataset, reference dataset, and pred dataset. 

Once this is done, you can run the code by clicking the play button at the top of your IDE.

If you want to run it via terminal, then first thing is to create an environment and then following the same steps as above. Once the environment is created and the requirements are installed, then the following command needs to be ran:

```console
/opt/anaconda3/envs/comet-env/bin/python compute_metrics.py -f data/mon/gemini-nso-sentences.txt
```
 where "/opt/anaconda3/envs/comet-env/" needs to be your environment that has all the necessary requirements installed. Please see SETUP.md for more detail

 to run the different languages, update the language, to do this, change the language code in the command. for example:

 ```console
nso -> zul or tso.
```

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

