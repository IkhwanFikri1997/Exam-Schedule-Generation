import xlsxwriter
import display
import string

isfilled = {}

color = ['black', 'blue', 'brown', 'cyan', 'green', 'lime', 'magenta', 'navy', 'orange', 'pink', 'purple', 'silver', 'white', 'yellow']

workbook = xlsxwriter.Workbook('Exam Revision Schedule.xlsx')
worksheet =  workbook.add_worksheet()

Bold = workbook.add_format({'bold': True})

worksheet.write('B1','Monday', Bold)
worksheet.write('C1','Tuesday', Bold)
worksheet.write('D1','Wednesday', Bold)
worksheet.write('E1','Thursday', Bold)
worksheet.write('F1','Friday', Bold)
worksheet.write('G1','Saturday', Bold)
worksheet.write('H1','Sunday', Bold)
colList = ['B','C','D','E','F','G','H']
shleep_format = workbook.add_format({'bg_color':'#808080','border_color':'#000080'})
school_format = workbook.add_format({'bg_color':'#FF0000','border_color':'#008000'})
lesson_format = []
n = 0
lesson_format.append(workbook.add_format({'bg_color':color[n],'border_color':'#008000'}))

def MakeHourlySchedule(slst,slnd,mnst,mnnd,tdst,tdnd,wdst,wdnd,thst,thnd,frst,frnd,stst,stnd,lesson):

    for i in range (8):
        for j in range(26):
            isfilled[string.ascii_uppercase[i]+str(j)] = False

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
        worksheet.write(('B' + str(a + 2)),'',school_format)
        isfilled['B' + str(a+1)] = True
    for b in range(tdst, tdnd):
        worksheet.write(('C' + str(b + 2)),'',school_format)
        isfilled['C' + str(b+1)] = True
    for c in range(wdst, wdnd):
        worksheet.write(('D' + str(c + 2)),'',school_format)
        isfilled['D' + str(c+1)] = True
    for d in range(thst, thnd):
        worksheet.write(('E' + str(d + 2)),'',school_format)
        isfilled['E' + str(d+1)] = True
    for e in range(frst, frnd):
        worksheet.write(('F' + str(e + 2)),'',school_format)
        isfilled['F' + str(e+1)] = True
    for f in range(stst, stnd):
        worksheet.write(('G' + str(f + 2)),'',school_format)
        isfilled['G' + str(f+1)] = True

    for k in range (0,len(lesson)):
        for m in range (1, (lesson[k]+1)):
            lessondone = False
            for i in range(7,1,-1):
                for j in range(24,1,-1):
                    if (lessondone == False and isfilled[string.ascii_uppercase[i]+str(j)] == False):
                        print(m)
                        worksheet.write((string.ascii_uppercase[i]+str(j+1)),'',lesson_format[k])
                        isfilled[string.ascii_uppercase[i]+str(j)] = True
                        lessondone = True
        n = k+1
        lesson_format.append(workbook.add_format({'bg_color':color[n],'border_color':'#008000'}))
        print(color[n])

    workbook.close()

def MakeDetailedSchedule(slst,slnd,mnst,mnnd,tdst,tdnd,wdst,wdnd,thst,thnd,frst,frnd,stst,stnd,lesson):

    for i in range (8):
        for j in range(50):
            isfilled[string.ascii_uppercase[i]+str(j)] = False

    for x in range(48):
        if x % 2 == 0:
            worksheet.write(('A' + str(x + 2)),str(x//2)+':00')
            isfilled['A'+ str(x+1)] = True
        elif x % 2 == 1:
            worksheet.write(('A' + str(x + 2)),str((x-1)//2)+':30')
            isfilled['A'+ str(x+1)] = True
    
    for h in range(0,7):
        if slst > slnd:
            for l in range(0, slnd*2):
                worksheet.write((colList[h] + str(l + 2)),'',shleep_format)
                isfilled[colList[h] + str(l+1)] = True
            for i in range(slst*2, 48):
                worksheet.write((colList[h] + str(i + 2)),'',shleep_format)
                isfilled[colList[h] + str(i+1)] = True
        if slst < slnd:
            for l in range(slst*2, slnd*2):
                worksheet.write((colList[h] + str(l + 2)),'',shleep_format)
                isfilled[colList[h] + str(l+1)] = True

    for a in range(mnst*2, mnnd*2):
        worksheet.write(('B' + str(a + 2)),'',school_format)
        isfilled['B' + str(a+1)] = True
    for b in range(tdst*2, tdnd*2):
        worksheet.write(('C' + str(b + 2)),'',school_format)
        isfilled['C' + str(b+1)] = True
    for c in range(wdst*2, wdnd*2):
        worksheet.write(('D' + str(c + 2)),'',school_format)
        isfilled['D' + str(c+1)] = True
    for d in range(thst*2, thnd*2):
        worksheet.write(('E' + str(d + 2)),'',school_format)
        isfilled['E' + str(d+1)] = True
    for e in range(frst*2, frnd*2):
       worksheet.write(('F' + str(e + 2)),'',school_format)
       isfilled['F' + str(e+1)] = True
    for f in range(stst*2, stnd*2):
       worksheet.write(('G' + str(f + 2)),'',school_format)
       isfilled['G' + str(f+1)] = True

    for k in range (0,len(lesson)):
        for m in range (1, (lesson[k]+1)*2):
            lessondone = False
            for i in range(7,1,-1):
                for j in range(48,1,-1):
                    if (lessondone == False and isfilled[string.ascii_uppercase[i]+str(j)] == False):
                        print(m)
                        worksheet.write((string.ascii_uppercase[i]+str(j+1)),'',lesson_format[k])
                        isfilled[string.ascii_uppercase[i]+str(j)] = True
                        lessondone = True
        n = k+1
        lesson_format.append(workbook.add_format({'bg_color':color[n],'border_color':'#008000'}))
        print(color[n])

    workbook.close()