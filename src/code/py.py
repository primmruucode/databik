import pandas as pd
import gcsfs

# Set up GCS credentials (replace with your own GCS credentials)
gcs_project_id = 'totemic-carrier-389808'
gcs_bucket_name = 'databricket'

# Create a GCS filesystem object
fs = gcsfs.GCSFileSystem(project=gcs_project_id)

# Specify the path to your CSV file in the GCS bucket
csv_file_path = 'gs://databricket/datacsv/Electric_Vehicle_Population_Data.csv'.format(gcs_bucket_name)

# Read the CSV file using pandas
df = pd.read_csv(fs.open(csv_file_path))

# Display the DataFrame
display(df)
