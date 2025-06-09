# 🧠 ML Project Template

A clean and modular template for building end-to-end Machine Learning systems using MLOps best practices.

This repository follows along with:
- **Ayush Singh's FreeCodeCamp MLOps Series**
- **Krish Naik's End-to-End ML System Design Tutorials**

---

## 📁 Project Structure

ML_PROJECT_TEMPLATE/
├── data/                  # Raw or processed data
├── ml_project.egg-info/   # Package metadata
├── src/                   # Source code
│   ├── components/        # Core ML components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/          # Train & predict pipeline scripts
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   ├── exception.py       # Custom exception handling
│   ├── logger.py          # Logging utility
│   ├── utils.py           # Utility functions
├── venv/                  # Virtual environment
├── .gitignore
├── README.md
├── requirements.txt       # Python dependencies
└── setup.py               # Installable Python package

---

## ✅ Current Progress

### 📦 Data Ingestion System

- Implemented using **OOP design** with **Abstract Base Classes**.
- Built a flexible factory that auto-detects file formats and loads them as `pandas.DataFrame`.

#### Ingestors:
- **`ZipDataIngestor`**: Extracts a `.zip` containing exactly one `.csv` and loads it.
- **`JSONDataIngestor`**: Reads a JSON file and converts it into a DataFrame.
- **`ExcelDataIngestor`**: Supports `.xlsx` files and returns a DataFrame.
- **`DataIngestorFactory`**: Automatically selects the correct ingestor class based on file extension.

---

## 🚧 Upcoming Modules

- 🔄 Data Transformation
- 🤖 Model Training
- 🧪 Evaluation
- 🚀 CI/CD & Deployment

---

## 📌 How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/sameer786-xyz/ML_project_template.git
   cd ML_project_template

	2.	Install dependencies:

pip install -r requirements.txt


	3.	Run the training pipeline:

python src/pipeline/train_pipeline.py



⸻

🙌 Acknowledgements
	•	Ayush Singh – FreeCodeCamp AI/MLOps
	•	Krish Naik – End-to-End ML Projects

⸻

📬 Contact

Feel free to reach out via GitHub Issues for feedback or collaboration.

---