# 📁 MLOps Learning Journey

This repository contains all the code, files, and notes related to my journey of learning **MLOps.**

I am following the **FreeCodeCamp’s End-to-End Machine Learning Project (AI & MLOps) by Ayush Singh** as my primary learning resource.

I will be updating this repository daily with everything I learn along the way.


✅ **Current Progress**
	•	Learned about Data Ingestion, the first step in any ML pipeline.
	•	Built a modular and extensible Data Ingestion System using Object-Oriented Programming and Abstract Base Classes.
	•	Implemented the following components:

📦 ZipDataIngestor
	•	Extracts .csv files from a .zip archive.
	•	Validates the presence of exactly one .csv file and converts it into a pandas DataFrame.

🧾 JSONDataIngestor
	•	Reads a .json file directly from the given path.
	•	Loads the data and converts it into a pandas DataFrame.

📊 ExcelDataIngestor
	•	Handles .xlsx Excel files.
	•	Reads and returns the data as a pandas DataFrame.

🏭 DataIngestorFactory
	•	Detects the file extension automatically.
	•	Instantiates the appropriate ingestor class (.zip, .json, or .xlsx).
	•	Provides a unified ingest_data() method for ingestion.
