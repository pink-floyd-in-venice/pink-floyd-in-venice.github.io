import pandas as pd

def main():
	name=input("inserire nome file csv: ")
	columns=input("inserire colonne separate da virgola: ")
	columns=list(columns.split(","))
	df = pd.read_csv(f"{name}.csv", names=columns)
	print(df.to_html(index=False, border=None))
if __name__=="__main__":
	main()