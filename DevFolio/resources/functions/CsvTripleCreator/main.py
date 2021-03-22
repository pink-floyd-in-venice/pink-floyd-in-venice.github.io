import csv

if __name__== "__main__":
    csv_name=input("Inserire nome file csv: ")
    if csv_name[-4:] !=".csv":
        csv_name += ".csv"
    with open(csv_name, "w", newline="") as csv_file:
        writer=csv.writer(csv_file, delimiter=' ', quotechar='|')
        writer.writerow(["Subject", "Predicate", "Object"])
        while True:
            triple_string=input("Inserire tripla separata da un punto e virgola(;) o stop: ")
            if triple_string in"stopSTOP":
                break
            triple_list=list(triple_string.split(";"))
            if len(triple_list)!= 3:
                print("Errore nella definizione della tripla")
                continue
            writer.writerow(triple_list)