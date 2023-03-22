from app.api import ApiClient
from app.transform import DataTransform
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize objects
    api_client = ApiClient()
    data_transform = DataTransform()

    # Fetch data
    raw_data = api_client.fetch_data(dateFrom='2022-01-01')

    # Transform data
    flattened_df = data_transform.flatten_data(raw_data)

    # Save data
    data_transform.save_to_parquet(flattened_df, "flattened_timetrack_data.parquet")

if __name__ == '__main__':
    main()
