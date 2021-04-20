from dotenv import load_dotenv
from sqlalchemy.orm import Session
import glob
import csv
from models import Tax, engine
load_dotenv()

files = glob.glob("data/tax/*.csv")

session = Session(engine)

for f in files:
    print('Processing: %s' % f)
    records = []
    with open(f, encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0

        for row in csv_reader:
            print(f'Row in progress: %s' % row)
            print(f'Length %i' % len(row))
            if len(row)==9:
                records.append(Tax(year=row[0], business_id=row[1], name=row[2],
                                municipality=row[3], tax_income=float(row[4].replace(',','.')), tax_total=float(row[5].replace(',','.')),
                                tax_advance=float(row[6].replace(',','.')), tax_return=float(row[7].replace(',','.')), tax_residual=float(row[8].replace(',','.'))))
            line_count+=1
             
        session.bulk_save_objects(records)
        session.commit()
        records = []
        print(f'Committing records')
        print(f'Processed {line_count} lines.')
session.commit()
session.close()