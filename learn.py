import xlsxwriter
import display
import string
import random

isfilled = {}
# initializing dictionary 
for i in range (8):
    for j in range(26):
        isfilled[string.ascii_uppercase[i]+str(j)] = False

color = ['black', 'blue', 'brown', 'cyan', 'green', 'lime', 'magenta', 'navy', 'orange', 'pink', 'purple', 'silver', 'white', 'yellow']
n = random.randint(0,(len(color)-1))
print(color[n])

workbook = xlsxwriter.Workbook('Exam Revision Schedule.xlsx')
worksheet =  workbook.add_worksheet()

Bold = workbook.add_format({'bold': True})

worksheet.write('B1','Sunday', Bold)
worksheet.write('C1','Monday', Bold)
worksheet.write('D1','Tuesday', Bold)
worksheet.write('E1','Wednesday', Bold)
worksheet.write('F1','Thursday', Bold)
worksheet.write('G1','Friday', Bold)
worksheet.write('H1','Saturday', Bold)
colList = ['B','C','D','E','F','G','H']
shleep_format = workbook.add_format({'bg_color':'#808080','border_color':'#000080'})
school_format = workbook.add_format({'bg_color':'#FF0000','border_color':'#008000'})
lesson_format = []
lesson_format.append(workbook.add_format({'bg_color':color[n],'border_color':'#008000'}))

for i in range(8):
    isfilled[string.ascii_uppercase[i]+'0'] = True

slst = 20
slnd = 3
mnst = 5
mnnd = 10
tdst = 6
tdnd = 12
wdst = 8
wdnd = 10
thst = 8
thnd = 14
frst = 10
frnd = 14
stst = 9
stnd = 15

for x in range(24):
        worksheet.write(('A' + str(x + 2)),str(x)+':00')
        isfilled['A'+ str(x+1)] = True

for h in range(0,7):
    if slst > slnd:
        for l in range(0, slnd):
            worksheet.write((colList[h] + str(l + 2)),'',shleep_format)
            isfilled[colList[h] + str(l+1)] = True
        for i in range(slst, 24):
            worksheet.write((colList[h] + str(i + 2)),'',shleep_format)
            isfilled[colList[h] + str(i+1)] = True
    if slst < slnd:
        for l in range(slst, slnd):
            worksheet.write((colList[h] + str(l + 2)),'',shleep_format)
            isfilled[colList[h] + str(l+1)] = True

for a in range(mnst, mnnd):
    worksheet.write(('C' + str(a + 2)),'',school_format)
    isfilled['C' + str(a+1)] = True
for b in range(tdst, tdnd):
    worksheet.write(('D' + str(b + 2)),'',school_format)
    isfilled['D' + str(b+1)] = True
for c in range(wdst, wdnd):
    worksheet.write(('E' + str(c + 2)),'',school_format)
    isfilled['E' + str(c+1)] = True
for d in range(thst, thnd):
    worksheet.write(('F' + str(d + 2)),'',school_format)
    isfilled['F' + str(d+1)] = True
for e in range(frst, frnd):
    worksheet.write(('G' + str(e + 2)),'',school_format)
    isfilled['G' + str(e+1)] = True
for f in range(stst, stnd):
    worksheet.write(('H' + str(f + 2)),'',school_format)
    isfilled['H' + str(f+1)] = True

lesson = [2,5,10,8,4]

for k in range (0,len(lesson)):
    for m in range (1, lesson[k]+1):
        lessondone = False
        for i in range(1,8):
            for j in range(1,25):
                if (lessondone == False and isfilled[string.ascii_uppercase[i]+str(j)] == False):
                    print(m)
                    worksheet.write((string.ascii_uppercase[i]+str(j+1)),'',lesson_format[k])
                    isfilled[string.ascii_uppercase[i]+str(j)] = True
                    lessondone = True
    n = k
    lesson_format.append(workbook.add_format({'bg_color':color[n],'border_color':'#008000'}))
    print(color[n])

workbook.close()

