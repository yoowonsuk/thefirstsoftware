from flat import Bill, Flatmate, PdfReport FileSharer

a = float(input("Hey user, enter the bill amount: "))
print(type(a))
period = input("What is the bill period? E.g. December 2020: ")

name1 = input("What is your name? ")
days_in_house2 = int(input(f"how many days did ${name1} stay in the house during the bill period? "))

name2 = input("What is the name of the other flatmate? ")
days_in_house1 = int(input(f"how many days did ${name2} stay in the house during the bill period? "))

bill = Bill(amount=a, period=period)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)

print(f"${flatmate1.name} pays: ", flatmate1.pays(bill=bill, flatmate2=flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(bill=bill, flatmate2=flatmate1))

pdf_report = PdfReport(filename=f"Report.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())
