import pandas as pd
import requests
import csv

excel_file = '/home/arun/Downloads/File_Inventory.xlsx'
report_file = '/home/arun/Downloads/url_test_report.csv'

BASE_URL = 'https://webapi-static-fast.s3.amazonaws.com/product_document/'
base_path_prefix = '/home/vinod/Downloads/Organized_Compliance_Docs_2026_2/'

df = pd.read_excel(excel_file)

# Skip icon rows
df = df[df['subfolder'] != 'icon']

rows = []
total = len(df)

for i, (_, row) in enumerate(df.iterrows(), 1):
    product_code = row['product_code']
    subfolder    = row['subfolder']
    filename     = row['filename']
    full_path    = row['full_path']

    relative_url = str(full_path).replace(base_path_prefix, '')
    full_url     = BASE_URL + relative_url

    if str(subfolder).startswith('6-Sided-Packaging'):
        url_type = '6-Sided'
    elif str(subfolder).startswith('US/Amazon/'):
        url_type = 'Carousel'
    elif 'MSDS' in str(subfolder):
        url_type = 'MSDS'
    elif 'DG' in str(subfolder):
        url_type = 'DG'
    else:
        continue

    try:
        status = requests.get(full_url, timeout=10).status_code
    except Exception as e:
        status = f"ERROR: {str(e)}"

    print(f"[{i}/{total}] {product_code} | {url_type} | {status} | {filename}")
    rows.append([product_code, url_type, filename, full_url, status])

with open(report_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['product_code', 'type', 'filename', 'url', 'status'])
    writer.writerows(rows)

print(f"\nReport saved to {report_file}")
