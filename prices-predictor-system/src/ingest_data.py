import pandas as pd
import os
import json
import zipfile
from abc import ABC, abstractmethod

class DataIngestor(ABC):
    @abstractmethod
    def ingest_data(self, file_path: str) -> pd.DataFrame:
        """Abstract method to ingest data from a file and return a pandas DataFrame."""
        pass

class ZipDataIngestor(DataIngestor):
    def ingest_data(self, file_path: str) -> pd.DataFrame:
        """Extracts the contents of a zip file and returns a pandas DataFrame."""
        if not file_path.endswith('.zip'):
            raise ValueError("File must be a zip file.")
        
        extract_path = "extracted_files"
        os.makedirs(extract_path, exist_ok=True)  # Create directory if not exists
        
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        
        # List extracted files
        extracted_files = os.listdir(extract_path)
        csv_files = [f for f in extracted_files if f.endswith('.csv')]

        if len(csv_files) == 0:
            raise ValueError("No CSV file found in the zip file.")
        if len(csv_files) > 1:
            raise ValueError("Multiple CSV files found in the zip file.")
        
        # Read the CSV file
        csv_file_path = os.path.join(extract_path, csv_files[0])
        df = pd.read_csv(csv_file_path)
        return df
    
class JSONDataIngestor(DataIngestor):
    def ingest_data(self, file_path: str) -> pd.DataFrame:
        """Ingest data from a JSON file and return a pandas DataFrame."""
        if not file_path.endswith('.json'):
            raise ValueError("File must be a JSON file.")
        
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, 'r') as file:
            data = json.load(file)

        # Convert JSON to DataFrame
        df = pd.DataFrame(data)
        return df
    
class ExcelDataIngestor(DataIngestor):
    def ingest_data(self, file_path: str) -> pd.DataFrame;
        """Ingest data from a excel file and return a pandas DataFrame."""
        if not file_path.endswith('.xlsx'):
            raise ValueError("File must be a excel file.")
        
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        df = pd.read_excel(file_path)
        return df
    
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension: str) -> DataIngestor:
        """Returns the appropriate data ingestor based on the file extension."""
        if file_extension == '.zip':
            return ZipDataIngestor()
        elif file_extension == '.json':
            return JSONDataIngestor()
        elif file_extension == '.xlsx':
            return ExcelDataIngestor()
        else:
            raise ValueError(f"Unsupported file extension: {file_extension}")
        
    def ingest_data(self, file_path: str) -> pd.DataFrame:
        """Ingest data from a file and return a pandas DataFrame."""
        file_extension = os.path.splitext(file_path)[1]
        ingestor = self.get_data_ingestor(file_extension)
        return ingestor.ingest_data(file_path)
    

if __name__ == "__main__":
    ingestor = DataIngestorFactory()
    df = ingestor.ingest_data("data/data.zip")