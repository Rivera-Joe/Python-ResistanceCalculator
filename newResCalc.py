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

#create 2 input boxes for each set up
def createInputBoxes():
    #series
    seriesBox = tk.Entry(root)
    seriesBox.grid(row=2, column=2, pady=20)
    seriesBox.insert(0, "   Input Series Values")
    seriesLabel = tk.Label(root, text="Series Values")
    seriesLabel.grid(row=2, column=1)
    #parallel
    parallelBox = tk.Entry(root)
    parallelBox.grid(row=3, column=2)
    parallelBox.insert(0, "   Input Parallel Values")
    parallelLabel = tk.Label(root, text="Parallel Values")
    parallelLabel.grid(row=3, column=1 )

#if box empty, count as zero
#initiate both resistance types as 0
resistance = {"series": 0, "parallel": 0, "total": 0}



createInputBoxes()
root.mainloop()