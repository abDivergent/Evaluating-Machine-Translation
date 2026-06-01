# Project Setup Instructions

## Quick Setup (First Time Only)

### Step 1: Create Python 3.10 Virtual Environment
From the project root directory, run:
```powershell
py -3.10 -m venv .venv
```

### Step 2: Activate Environment
```powershell
.venv\Scripts\activate
```
You should see `(.venv)` at the start of your terminal prompt.

### Step 3: Install Dependencies
```powershell
python -m pip install --upgrade pip setuptools wheel
pip install nltk pandas evaluate "transformers<5.0" "unbabel-comet" torch pytorch-lightning
pip install "numpy<2.0.0" "torchmetrics<0.11.0" entmax "jsonargparse==3.13.1" "protobuf<5.0.0" scipy sentencepiece "huggingface-hub<1.0" "sacrebleu<3.0.0" click joblib
```

That's it! The environment is ready to use.

---

## Running the Metrics Script

### Basic Usage
```powershell
.venv\Scripts\activate
python scripts/compute_metrics.py -f data/mon/gpt-nso-sentences.txt
```

### Example with Different Files
```powershell
python scripts/compute_metrics.py -f data/mon/gemini-nso-sentences.txt
```

### Exit Environment
```powershell
deactivate
```

---

## Project Structure
```
760/
├── data/
│   ├── corrected/     # Corrected datasets
│   ├── mon/           # Translation files
│   │   ├── english_sentences.txt
│   │   ├── corrected-nso.txt
│   │   ├── gpt-nso-sentences.txt
│   │   └── gemini-nso-sentences.txt
│   ├── original/      # Original datasets
│   └── wandile/       # Alternative datasets
├── scripts/
│   ├── compute_metrics.py    # Main evaluation script
│   ├── utils.py              # Helper functions
│   ├── requirements.txt       # Dependencies
│   └── compute_metrics.ipynb  # Jupyter notebook
└── .venv/             # Virtual environment (created by setup)
```

---

## Important Notes

- **COMET Model**: Located at `../comet_model` (parent directory). The script will automatically find it.
- **Run Location**: Always run scripts from the project root (`760/` directory)
- **Python Version**: Python 3.10.11 (created automatically with `py -3.10 -m venv`)

---

## Troubleshooting

**Problem**: `python: The term 'python' is not recognized`
- **Solution**: Activate the environment first: `.venv\Scripts\activate`

**Problem**: Module not found errors
- **Solution**: Ensure you're in the project root and the environment is activated

**Problem**: Permission denied when activating
- **Solution**: Open PowerShell as Administrator, run:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
