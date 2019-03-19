import openpyxl

wk = openpyxl.Workbook()
sh = wk.active
#Write data into the sheet
sh.title = "HelloTesting World"
print(sh.title)

sh['A4'].value = "www.theTestingWorld.com"

#Second sheet is created
wk.create_sheet(title="TestingW")
sh1 = wk['TestingW']
sh1['A3']="+91-9876543210"


#Remove Sheet
wk.remove(wk['HelloTesting World'])

#Saving the data
wk.save("E:\\PySheet.xlsx")

