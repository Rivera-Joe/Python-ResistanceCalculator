import tkinter as tk


#user should be able to input both types of set ups
#resistance should be calculated as total

root = tk.Tk()
root.title("Resistor Calculator 2.0")
#set minimum window size
root.minsize(width=300, height=300)

#add instructions
instruct = tk.Label(root, text="\nCalculate resistance below by inputting each value in their respected boxes.\nPlease seperate each value with a comma\n" )
instruct.grid(rowspan=2, columnspan=3)

def calculate():
    seriesString = seriesBox.get()
    if seriesString:
        try:
            #create list based on comma delimiter
            seriesValues = seriesString.split(",")
            #change list of strings to int
            seriesValues = list(map(int, seriesValues))
            #add series
            totalSeries = 0
            for x in seriesValues:
                totalSeries += x
            #update total series resistance
            setSeries(totalSeries)
        except:
            print("error")            

#set series value            
def setSeries(value):
    resistance['series'] = value
    getSeries()

#display calculated series value
def getSeries():
    print(resistance["series"])
    seriesValueLabel = tk.Label(root, text=f"Series Total: {resistance["series"]}")
    seriesValueLabel.grid(row=5)
#create 2 input boxes for each set up

#series
seriesBox = tk.Entry(root)
seriesBox.insert(0, "Series Values")
seriesBox.grid(row=2, column=2, pady=20)
seriesLabel = tk.Label(root, text="Series Values")
seriesLabel.grid(row=2, column=1)

#parallel
parallelBox = tk.Entry(root)
parallelBox.insert(0, "Parallel Values")
parallelBox.grid(row=3, column=2)
parallelLabel = tk.Label(root, text="Parallel Values")
parallelLabel.grid(row=3, column=1)


subButton = tk.Button(root, text="Calculate", command=calculate)
subButton.grid(row=4, columnspan=2, column=0, pady=20)


#if box empty, count as zero
#initiate both resistance types as 0
resistance = {"series": 0, "parallel": 0, "total": 0}





root.mainloop()