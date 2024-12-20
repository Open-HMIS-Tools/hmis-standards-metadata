from meta_dictionary_tools.csv.csv_tools import (
    HMIS_CSVLoader,
    OneBigCSV,
)
from meta_dictionary_tools.csv.lsa_csv_tools import LSA_HMIS_CSVLoader, OneBigLSACSV

OUTPUT_DIR = "<TEST>"

csvs_to_exclude = ["Services"]

csv_loader = LSA_HMIS_CSVLoader(OUTPUT_DIR)
df = OneBigLSACSV.load(csv_loader, csvs_to_exclude)
