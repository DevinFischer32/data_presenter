import plotly.graph_objects as go 

open_file = open('CupcakeInvoices.csv')
for line in open_file:
    line = line.split(',')
    for type in line:
        if type == "Chocolate":
            print("Chocolate")
        elif type == "Vanilla":
            print("Vanilla")
        elif type == "Strawberry":
            print("Strawberry")
open_file.close()
chocolate = 0
vanilla = 0
strawberry = 0

open_file = open('CupcakeInvoices.csv')
for line in open_file:
    line = line.split(',')
    if line[2] =="Chocolate":
      chocolate += int(line[3]) * float(line[4])
    elif line[2] =="Vanilla":
      vanilla += int(line[3]) * float(line[4])
    elif line[2] =="Strawberry":
      strawberry += int(line[3]) * float(line[4])
    

total_invoices = chocolate + vanilla + strawberry
print(round(total_invoices,2))
print(chocolate,vanilla,strawberry)

fig = go.Figure(data=go.Bar(y=[chocolate, vanilla, strawberry],x=["Chocolate", "Vanilla", "Strawberry"]))
fig.show()
open_file.close()