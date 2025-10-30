import click
from dotenv import load_dotenv
import os

load_dotenv() 

from .extract import extract_and_validate
from .transform import transform_data
from .load import load_data

DEFAULT_FILE_ID = "1yQeGe-12L8FFZ-cdwGnRZm_LrzdKrN4J"

@click.command()
@click.option('--file-id', 
              default=DEFAULT_FILE_ID, 
              help='Google Drive File ID для загрузки CSV.')
def main(file_id):
    """Сборка и запуск ETL-процесса."""
    print(f"--- Запуск ETL-процесса для Google Drive ID: {file_id} ---")

    raw_df = extract_and_validate(file_id)

    processed_df = transform_data(raw_df)

    load_data(processed_df)

if __name__ == '__main__':
    main()