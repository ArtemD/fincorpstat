from dotenv import load_dotenv
import glob
import csv
load_dotenv()

files = glob.glob("*.csv")

cur = con.cursor()