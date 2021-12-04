from flat import Bill, Flatemate
from report import PdfReport

# CLI enter bill amount and rent period
bill_amount =float(input("Please enter the bill amount:"))
bill_period = input("Please enter the month and year for the bill period. Ex. January 2020:")
month1_bill = Bill(amount=bill_amount, period=bill_period)

# Enter flatmates names and days in the house
flm1_name = input("Enter flatmate one's name:")
flm1_days = int(input(f"How many days did {flm1_name} stay in the house during {bill_period}? "))

flm2_name = input("Enter flatmate two's name:")
flm2_days = int(input(f"How many days did {flm2_name} stay in the house during {bill_period}? "))

flm1 = Flatemate(name=flm1_name, days_in_house=flm1_days)
flm2 = Flatemate(name=flm2_name, days_in_house=flm2_days)

print(flm1_name + " pays:" + "$", round(flm1.pays(bill=month1_bill, flatmate2=flm2), 2))
print(flm2_name + " pays:" + "$", round(flm2.pays(bill=month1_bill, flatmate2=flm1), 2))

bill_pdf = PdfReport(filename=f"{month1_bill.period}.pdf")
bill_pdf.generate(flatemate1=flm1, flatmate2=flm2, bill=month1_bill)