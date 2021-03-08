import wx
import json
from schedule import *
import wx.grid as grid
import wx.adv as adv

timechoice = ["0:00","1:00","2:00","3:00","4:00","5:00","6:00","7:00","8:00","9:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"]

class first_panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)

        text1 = 'Welcome to revision timetable generator'
        text2 = 'This program will generate timetable based on the several questions that you will answered throughout this program'
        self.SetSize((800,480))
        
        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, text1, (20,10)).SetFont(font)
        wx.StaticText(self, -1, text2, (20,35)).SetFont(font)

        self.btn1 = wx.Button(self, -1, "Next", (200, 400))
        self.btn2 = wx.Button(self, -1, "Load Preset", (300, 400))


class second_panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        text11 = 'Sleep Time Confirmation'
        font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, text11, (250, 10)).SetFont(font)
        text12 = 'What time do you usually sleep?'
        font2 = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, text12, (20, 50)).SetFont(font2)
        self.SleepTimeStart = wx.ComboBox(self, pos=(20, 75), choices=timechoice, style=wx.CB_READONLY)
        self.SleepTimeEnd = wx.ComboBox(self, pos=(80, 75), choices=timechoice, style=wx.CB_READONLY)

        self.btn = wx.Button(self, -1, "Next", (300, 400))


class third_panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        text21 = 'School Time Confirmation'
        font1 = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, text21, (250, 10)).SetFont(font1)
        text22 = 'What time do you usually go to school?'
        text23 = 'Monday'
        text24 = 'Tuesday'
        text25 = 'Wednesday'
        text26 = 'Thursday'
        text27 = 'Friday'
        text28 = 'Saturday'
        font2 = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, text22, (20, 50)).SetFont(font2)
        wx.StaticText(self, -1, text23, (20, 75)).SetFont(font2)
        wx.StaticText(self, -1, text24, (20, 100)).SetFont(font2)
        wx.StaticText(self, -1, text25, (20, 125)).SetFont(font2)
        wx.StaticText(self, -1, text26, (20, 150)).SetFont(font2)
        wx.StaticText(self, -1, text27, (20, 175)).SetFont(font2)
        wx.StaticText(self, -1, text28, (20, 200)).SetFont(font2)
        self.MondayTimeStart = wx.ComboBox(self, pos=(100, 75), choices=timechoice, style=wx.CB_READONLY)
        self.MondayTimeEnd = wx.ComboBox(self, pos=(160, 75), choices=timechoice, style=wx.CB_READONLY)
        self.TuesdayTimeStart = wx.ComboBox(self, pos=(100, 100), choices=timechoice, style=wx.CB_READONLY)
        self.TuesdayTimeEnd = wx.ComboBox(self, pos=(160, 100), choices=timechoice, style=wx.CB_READONLY)
        self.WednesdayTimeStart = wx.ComboBox(self, pos=(100, 125), choices=timechoice, style=wx.CB_READONLY)
        self.WednesdayTimeEnd = wx.ComboBox(self, pos=(160, 125), choices=timechoice, style=wx.CB_READONLY)
        self.ThursdayTimeStart = wx.ComboBox(self, pos=(100, 150), choices=timechoice, style=wx.CB_READONLY)
        self.ThursdayTimeEnd = wx.ComboBox(self, pos=(160, 150), choices=timechoice, style=wx.CB_READONLY)
        self.FridayTimeStart = wx.ComboBox(self, pos=(100, 175), choices=timechoice, style=wx.CB_READONLY)
        self.FridayTimeEnd = wx.ComboBox(self, pos=(160, 175), choices=timechoice, style=wx.CB_READONLY)
        self.SaturdayTimeStart = wx.ComboBox(self, pos=(100, 200), choices=timechoice, style=wx.CB_READONLY)
        self.SaturdayTimeEnd = wx.ComboBox(self, pos=(160, 200), choices=timechoice, style=wx.CB_READONLY)

        self.btn = wx.Button(self, -1, "Next", (300, 400))

class fourth_panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        text5 = "Input Schedule"
        font1 = font1 = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, text5, (275, 10)).SetFont(font1)
        text51 = "include your exam schedule here!"
        font2 = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, text51, (20, 50)).SetFont(font2)
        self.grid1 = grid.Grid(self, -1, (20,75), (325,250))
        self.grid1.CreateGrid(26,2)
        self.grid1.SetColSize(0, 100)
        self.grid1.SetColSize(1, 125)
        self.grid1.SetCellValue(0,0, "Lesson")
        self.grid1.SetCellValue(0,1, "Date")

        self.btn = wx.Button(self, -1, "Next", (300, 400))

class MyTarget(wx.TextDropTarget):
    def __init__(self, object):
        wx.TextDropTarget.__init__(self)
        self.object = object

    def OnDropText(self, x, y, data):
        self.object.InsertItem(0, data)
        return True

class fifth_panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        text6 = "Exam Prioritization"
        font1 = font1 = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, text6, (225, 10)).SetFont(font1)
        text61 = "please drag each lesson from this list to the new ones depending on how important it is"
        font2 = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, text61, (20, 50)).SetFont(font2)
        self.box1 = wx.ListBox(self, -1, (20,75), (150,250), style = wx.LB_SINGLE)
        self.btn1 = wx.Button(self, -1, ">>", (200, 150))
        self.btn2 = wx.Button(self, -1, "<<", (200, 200)) 
        self.box2 = wx.ListBox(self, -1, (300,75), (150,250), style = wx.LB_SINGLE)

        self.btn = wx.Button(self, -1, "Next", (300, 400))

class sixth_panel(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        text7 = "Preparation hours estimation"
        font1 = font1 = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, text7, (250, 10)).SetFont(font1)
        text71 = "how long could you prepare these exams?"
        font2 = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, text71, (20, 50)).SetFont(font2)
        self.grid1 = grid.Grid(self, -1, (20,75), (325,250))
        self.grid1.CreateGrid(26,2)
        self.grid1.SetColSize(0, 100)
        self.grid1.SetColSize(1, 125)
        self.grid1.SetCellValue(0,0, "Lesson")
        self.grid1.SetCellValue(0,1, "Hours of Preparation")

        self.btn = wx.Button(self, -1, "Next", (300, 400))

class seventh_panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        text4 = 'Input Confirmation'
        font1 = font1 = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, text4, (275, 10)).SetFont(font1)        
        font2 = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        text41="test"
        self.st1 = wx.StaticText(self, -1, label=text41, pos=(10, 50))
        self.st1.SetFont(font2)
        self.st2 = wx.StaticText(self, -1, label=text41, pos=(10, 75))
        self.st2.SetFont(font2)
        self.st3 = wx.StaticText(self, -1, label=text41, pos=(10, 100))
        self.st3.SetFont(font2)
        self.st4 = wx.StaticText(self, -1, label=text41, pos=(10, 125))
        self.st4.SetFont(font2)
        self.st5 = wx.StaticText(self, -1, label=text41, pos=(10, 150))
        self.st5.SetFont(font2)
        self.st6 = wx.StaticText(self, -1, label=text41, pos=(10, 175))
        self.st6.SetFont(font2)
        self.st7 = wx.StaticText(self, -1, label=text41, pos=(10, 200))
        self.st7.SetFont(font2)
        self.grid1 = grid.Grid(self, -1, (325,50), (375,300))
        self.grid1.CreateGrid(26,3)
        self.grid1.SetColSize(0, 100)
        self.grid1.SetColSize(1, 125)
        self.grid1.SetColSize(2, 125)

        self.btn1 = wx.Button(self, -1, "Next", (300, 400))
        self.btn2 = wx.Button(self, -1, "Save Preset", (400,400))

class eighth_panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        text3 = 'Schedule Generation'
        font1 = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, text3, (295, 10)).SetFont(font1)
        text31 = 'which schedule do you want to generate?'
        font2 = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        font3 = wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, text31, (20, 50)).SetFont(font2)
        self.rb11 = wx.RadioButton(self, label="weekly",pos=(20, 75), style=wx.RB_GROUP)
        self.rb12 = wx.RadioButton(self, label="fixed (with date)",pos=(150, 75))
        text34 = 'which views do you want to choose?'
        wx.StaticText(self, -1, text34, (20, 100)).SetFont(font2)
        self.rb21 = wx.RadioButton(self, label="each 1 hour",pos=(20, 125), style=wx.RB_GROUP)
        self.rb22 = wx.RadioButton(self, label="each 30 minute(more detail)",pos=(150, 125))

        self.btn1 = wx.Button(self, -1, "Create Agenda", (300, 400))

class PresetDialog(wx.Dialog):

    def __init__(self, *args, **kw):
        super(PresetDialog, self).__init__(*args, **kw)

        self.InitUI()
        self.SetSize(400,150)
        self.SetTitle("Choose Preset")
        self.chose = ""

    def InitUI(self):

        pnl = wx.Panel(self)
        self.set1 = wx.Button(self, -1, "Preset 1", (50,50))
        self.set2 = wx.Button(self, -1, "Preset 2", (150,50))
        self.set3 = wx.Button(self, -1, "Preset 2", (250,50))
        
        self.set1.Bind(wx.EVT_BUTTON, self.ExecPre1)
        self.set2.Bind(wx.EVT_BUTTON, self.ExecPre2)
        self.set3.Bind(wx.EVT_BUTTON, self.ExecPre3)
    
    def ExecPre1(self, event):
        self.chose = "Pre1"
        self.Destroy()

    def ExecPre2(self, event):
        self.chose = "Pre2"
        self.Destroy()

    def ExecPre3(self, event):
        self.chose = "Pre3"
        self.Destroy()

class Program(wx.Frame):

    def __init__(self):
        no_resize = wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
        wx.Frame.__init__(self, None, title='Program', style=no_resize)

        sizer = wx.BoxSizer()
        self.SetSizer(sizer)
        
        self.wpnl = wx.Panel(self, pos=(0,0), size=(60,450))
        self.wpnl.SetBackgroundColour(wx.Colour(100,150,200))
        sizer.Add(self.wpnl, 0, wx.EXPAND)
        self.panel_one = first_panel(self)
        sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.panel_two = second_panel(self)
        self.panel_one.btn1.Bind(wx.EVT_BUTTON, self.show_panel_two)
        self.panel_one.btn2.Bind(wx.EVT_BUTTON, self.show_load_dialog)
        sizer.Add(self.panel_two, 1, wx.EXPAND)
        self.panel_two.btn.Bind(wx.EVT_BUTTON, self.show_panel_three)
        self.panel_two.Hide()
        self.panel_three = third_panel(self)
        sizer.Add(self.panel_three, 1, wx.EXPAND)
        self.panel_three.btn.Bind(wx.EVT_BUTTON, self.show_panel_four)
        self.panel_three.Hide()
        self.panel_four = fourth_panel(self)
        sizer.Add(self.panel_four, 1, wx.EXPAND)
        self.panel_four.btn.Bind(wx.EVT_BUTTON, self.show_panel_five)
        self.panel_four.Hide()
        self.panel_five = fifth_panel(self)
        sizer.Add(self.panel_five, 1, wx.EXPAND)
        self.panel_five.btn.Bind(wx.EVT_BUTTON, self.show_panel_six)
        self.panel_five.btn1.Bind(wx.EVT_BUTTON, self.bring_to_next)
        self.panel_five.btn2.Bind(wx.EVT_BUTTON, self.bring_back)
        self.panel_five.Hide()
        self.panel_six = sixth_panel(self)
        sizer.Add(self.panel_six, 1, wx.EXPAND)
        self.panel_six.btn.Bind(wx.EVT_BUTTON, self.show_panel_seven)
        self.panel_six.Hide()
        self.panel_seven = seventh_panel(self)
        sizer.Add(self.panel_seven, 1, wx.EXPAND)
        self.panel_seven.btn1.Bind(wx.EVT_BUTTON, self.show_panel_eight)
        self.panel_seven.btn2.Bind(wx.EVT_BUTTON, self.show_save_dialog)
        self.panel_seven.Hide()
        self.panel_eight = eighth_panel(self)
        sizer.Add(self.panel_eight, 1, wx.EXPAND)
        self.panel_eight.btn1.Bind(wx.EVT_BUTTON, self.createagenda)
        self.panel_eight.Hide()
        self.SetSize((800, 480))
        self.Centre()

    def show_panel_two(self, event):
        self.panel_two.Show()
        self.panel_one.Hide()
        self.Layout()

    def show_panel_three(self, event):
        self.panel_three.Show()
        self.panel_two.Hide()
        self.Layout()

    def show_panel_four(self, event):
        self.panel_four.Show()
        self.panel_three.Hide()
        self.Layout()
    
    def show_panel_five(self, event):
        listLessons = []
        for i in range (1,26):
            listLessons.append(self.panel_four.grid1.GetCellValue(i,0))
            if(self.panel_four.grid1.GetCellValue(i,0) == ''):
                break
        listLessons.remove('')
        for i in range (0,len(listLessons)):
            self.panel_five.box1.Append(listLessons[i])
            self.panel_six.grid1.SetCellValue(i+1,0,listLessons[i])
        print(listLessons)
        self.panel_five.Show()
        self.panel_four.Hide()
        self.Layout()
    
    def show_panel_six(self, event):
        self.panel_six.Show()
        self.panel_five.Hide()
        self.Layout()

    def show_panel_seven(self, event):
        STSstr = self.panel_two.SleepTimeStart.GetStringSelection()
        STEstr = self.panel_two.SleepTimeEnd.GetStringSelection()
        MTSstr = self.panel_three.MondayTimeStart.GetStringSelection()
        MTEstr = self.panel_three.MondayTimeEnd.GetStringSelection()
        TTSstr = self.panel_three.TuesdayTimeStart.GetStringSelection()
        TTEstr = self.panel_three.TuesdayTimeEnd.GetStringSelection()
        WTSstr = self.panel_three.WednesdayTimeStart.GetStringSelection()
        WTEstr = self.panel_three.WednesdayTimeEnd.GetStringSelection()
        ThTSstr = self.panel_three.ThursdayTimeStart.GetStringSelection()
        ThTEstr = self.panel_three.ThursdayTimeEnd.GetStringSelection()
        FTSstr = self.panel_three.FridayTimeStart.GetStringSelection()
        FTEstr = self.panel_three.FridayTimeEnd.GetStringSelection()
        SaTSstr = self.panel_three.SaturdayTimeStart.GetStringSelection()
        SaTEstr = self.panel_three.SaturdayTimeEnd.GetStringSelection()
        output1 = "You are sleeping from "+ str(STSstr) +" to "+ str(STEstr)
        self.panel_seven.st1.SetLabel(output1)
        output2 = "In monday, you have a school from "+ str(MTSstr) +" to "+ str(MTEstr)
        self.panel_seven.st2.SetLabel(output2)
        output3 = "In tuesday, you have a school from "+ str(TTSstr) +" to "+ str(TTEstr)
        self.panel_seven.st3.SetLabel(output3)
        output4 = "In wednesday, you have a school from "+ str(WTSstr) +" to "+ str(WTEstr)
        self.panel_seven.st4.SetLabel(output4)
        output5 = "In thursday, you have a school from "+ str(ThTSstr) +" to "+ str(ThTEstr)
        self.panel_seven.st5.SetLabel(output5)
        output6 = "In friday, you have a school from "+ str(FTSstr) +" to "+ str(FTEstr)
        self.panel_seven.st6.SetLabel(output6)
        output7 = "In saturday, you have a school from "+ str(SaTSstr) +" to "+ str(SaTEstr)
        self.panel_seven.st7.SetLabel(output7)
        self.panel_seven.grid1.SetCellValue(0,0, "Lesson")
        self.panel_seven.grid1.SetCellValue(0,1, "Date")
        self.panel_seven.grid1.SetCellValue(0,2, "Hours of Estimation")
        listLessons = []
        for i in range (1,26):
            listLessons.append(self.panel_four.grid1.GetCellValue(i,0))
            if(self.panel_four.grid1.GetCellValue(i,0) == ''):
                break
        listLessons.remove('')
        for i in range (0,len(listLessons)):
            self.panel_seven.grid1.SetCellValue(i+1,0,listLessons[i])
        listDates = []
        for i in range (1,26):
            listDates.append(self.panel_four.grid1.GetCellValue(i,1))
            if(self.panel_four.grid1.GetCellValue(i,1) == ''):
                break
        listDates.remove('')
        for i in range (0,len(listDates)):
            self.panel_seven.grid1.SetCellValue(i+1,1,listDates[i])
        listHours = []
        for i in range (1,26):
            listHours.append(self.panel_six.grid1.GetCellValue(i,1))
            if(self.panel_six.grid1.GetCellValue(i,1) == ''):
                break
        listHours.remove('')
        for i in range (0,len(listDates)):
            self.panel_seven.grid1.SetCellValue(i+1,2,listHours[i])
        self.panel_seven.Show()
        self.panel_six.Hide()
        self.Layout()
    
    def show_panel_eight(self, event):
        self.panel_eight.Show()
        self.panel_seven.Hide()
        self.Layout()
    
    def show_save_dialog(self,event):
        save_dialog = PresetDialog(None, title="Choose the preset that you want to save")
        save_dialog.SetTitle("Choose the preset that you want to save")
        save_dialog.ShowModal()
        if (save_dialog.chose == "Pre1"):
            Program.SavePreset(self, "Preset1")
        if (save_dialog.chose == "Pre2"):
            Program.SavePreset(self, "Preset2")
        if (save_dialog.chose == "Pre3"):
            Program.SavePreset(self, "Preset3")
        save_dialog.Destroy()
    
    def bring_to_next(self, event):
        self.panel_five.box2.Append(str(self.panel_five.box1.GetStringSelection()))
        self.panel_five.box1.Delete(self.panel_five.box1.GetSelection())

    def bring_back(self, event):
        self.panel_five.box1.Append(str(self.panel_five.box2.GetStringSelection()))
        self.panel_five.box2.Delete(self.panel_five.box2.GetSelection())

    def createagenda(self,event):
        Lessons = []
        for i in range (1,26):
            Lessons.append(self.panel_seven.grid1.GetCellValue(i,2))
            if(self.panel_seven.grid1.GetCellValue(i,2) == ''):
                break
        Lessons.remove('')
        for j in range(0,len(Lessons)):
            Lessons[j] = int(Lessons[j])
        print(Lessons)
        STSinput = self.panel_two.SleepTimeStart.GetCurrentSelection()
        STEinput = self.panel_two.SleepTimeEnd.GetCurrentSelection()
        MTSinput = self.panel_three.MondayTimeStart.GetCurrentSelection()
        MTEinput = self.panel_three.MondayTimeEnd.GetCurrentSelection()
        TTSinput = self.panel_three.TuesdayTimeStart.GetCurrentSelection()
        TTEinput = self.panel_three.TuesdayTimeEnd.GetCurrentSelection()
        WTSinput = self.panel_three.WednesdayTimeStart.GetCurrentSelection()
        WTEinput = self.panel_three.WednesdayTimeEnd.GetCurrentSelection()
        ThTSinput = self.panel_three.ThursdayTimeStart.GetCurrentSelection()
        ThTEinput = self.panel_three.ThursdayTimeEnd.GetCurrentSelection()
        FTSinput = self.panel_three.FridayTimeStart.GetCurrentSelection()
        FTEinput = self.panel_three.FridayTimeEnd.GetCurrentSelection()
        SaTSinput = self.panel_three.SaturdayTimeStart.GetCurrentSelection()
        SaTEinput = self.panel_three.SaturdayTimeEnd.GetCurrentSelection()
        choice11 = self.panel_eight.rb11.GetValue()
        choice12 = self.panel_eight.rb12.GetValue()
        choice21 = self.panel_eight.rb21.GetValue()
        choice22 = self.panel_eight.rb22.GetValue()
        if(choice11 == True & choice21 == True):
            MakeHourlySchedule(STSinput,STEinput,MTSinput,MTEinput,TTSinput,TTEinput,WTSinput,WTEinput,ThTSinput,ThTEinput,FTSinput,FTEinput,SaTSinput,SaTEinput,Lessons)
        if(choice11 == True & choice22 == True):
            MakeDetailedSchedule(STSinput,STEinput,MTSinput,MTEinput,TTSinput,TTEinput,WTSinput,WTEinput,ThTSinput,ThTEinput,FTSinput,FTEinput,SaTSinput,SaTEinput,Lessons)

    def SavePreset(self, Presetname):
        Presetinp = {
            'stssr' : str(self.panel_two.SleepTimeStart.GetStringSelection()),
            'stesr' : str(self.panel_two.SleepTimeEnd.GetStringSelection()),
            'mtssr' : str(self.panel_three.MondayTimeStart.GetStringSelection()),
            'mtesr' : str(self.panel_three.MondayTimeEnd.GetStringSelection()),
            'ttssr' : str(self.panel_three.TuesdayTimeStart.GetStringSelection()),
            'ttesr' : str(self.panel_three.TuesdayTimeEnd.GetStringSelection()),
            'wtssr' : str(self.panel_three.WednesdayTimeStart.GetStringSelection()),
            'wtesr' : str(self.panel_three.WednesdayTimeEnd.GetStringSelection()),
            'thtssr' : str(self.panel_three.ThursdayTimeStart.GetStringSelection()),
            'thtesr' : str(self.panel_three.ThursdayTimeEnd.GetStringSelection()),
            'ftssr' : str(self.panel_three.FridayTimeStart.GetStringSelection()),
            'ftesr' : str(self.panel_three.FridayTimeEnd.GetStringSelection()),
            'satssr' : str(self.panel_three.SaturdayTimeStart.GetStringSelection()),
            'satesr' : str(self.panel_three.SaturdayTimeEnd.GetStringSelection()),
            'stsinp' : self.panel_two.SleepTimeStart.GetCurrentSelection(),
            'steinp' : self.panel_two.SleepTimeEnd.GetCurrentSelection(),
            'mtsinp' : self.panel_three.MondayTimeStart.GetCurrentSelection(),
            'mteinp' : self.panel_three.MondayTimeEnd.GetCurrentSelection(),
            'ttsinp' : self.panel_three.TuesdayTimeStart.GetCurrentSelection(),
            'tteinp' : self.panel_three.TuesdayTimeEnd.GetCurrentSelection(),
            'wtsinp' : self.panel_three.WednesdayTimeStart.GetCurrentSelection(),
            'wteinp' : self.panel_three.WednesdayTimeEnd.GetCurrentSelection(),
            'thtsinp' : self.panel_three.ThursdayTimeStart.GetCurrentSelection(),
            'thteinp' : self.panel_three.ThursdayTimeEnd.GetCurrentSelection(),
            'ftsinp' : self.panel_three.FridayTimeStart.GetCurrentSelection(),
            'fteinp' : self.panel_three.FridayTimeEnd.GetCurrentSelection(),
            'satsinp' : self.panel_three.SaturdayTimeStart.GetCurrentSelection(),
            'sateinp' : self.panel_three.SaturdayTimeEnd.GetCurrentSelection(),
        }

        for i in range(1,26):
            Presetinp['lesson'+str(i)] = self.panel_four.grid1.GetCellValue(i,0)
            Presetinp['date'+str(i)] = self.panel_four.grid1.GetCellValue(i,1)
            Presetinp['hours'+str(i)] = self.panel_six.grid1.GetCellValue(i,1)
            if(self.panel_four.grid1.GetCellValue(i,0) == ''):
                break
        Presetinp.popitem()
        Presetinp.popitem()
        Presetinp.popitem()

        with open(str(Presetname)+'.json','w') as json_file:
            json.dump(Presetinp, json_file)

    def LoadPreset(self, Presetname):
        with open(str(Presetname)+'.json') as json_file:
            datas = json.load(json_file)
            print(datas)
            output1 = "You are sleeping from "+ str(datas['stssr']) +" to "+ str(datas['stesr'])
            self.panel_seven.st1.SetLabel(output1)
            output2 = "In monday, you have a school from "+ str(datas['mtssr']) +" to "+ str(datas['mtesr'])
            self.panel_seven.st2.SetLabel(output2)
            output3 = "In tuesday, you have a school from "+ str(datas['ttssr']) +" to "+ str(datas['ttesr'])
            self.panel_seven.st3.SetLabel(output3)
            output4 = "In wednesday, you have a school from "+ str(datas['wtssr']) +" to "+ str(datas['wtesr'])
            self.panel_seven.st4.SetLabel(output4)
            output5 = "In thursday, you have a school from "+ str(datas['thtssr']) +" to "+ str(datas['thtesr'])
            self.panel_seven.st5.SetLabel(output5)
            output6 = "In friday, you have a school from "+ str(datas['ftssr']) +" to "+ str(datas['ftesr'])
            self.panel_seven.st6.SetLabel(output6)
            output7 = "In saturday, you have a school from "+ str(datas['satssr']) +" to "+ str(datas['satesr'])
            self.panel_seven.st7.SetLabel(output7)
            self.panel_two.SleepTimeStart.SetSelection(datas['stsinp'])
            self.panel_two.SleepTimeEnd.SetSelection(datas['steinp'])
            self.panel_three.MondayTimeStart.SetSelection(datas['mtsinp'])
            self.panel_three.MondayTimeEnd.SetSelection(datas['mteinp'])
            self.panel_three.TuesdayTimeStart.SetSelection(datas['ttsinp'])
            self.panel_three.TuesdayTimeEnd.SetSelection(datas['tteinp'])
            self.panel_three.WednesdayTimeStart.SetSelection(datas['wtsinp'])
            self.panel_three.WednesdayTimeEnd.SetSelection(datas['wteinp'])
            self.panel_three.ThursdayTimeStart.SetSelection(datas['thtsinp'])
            self.panel_three.ThursdayTimeEnd.SetSelection(datas['thteinp'])
            self.panel_three.FridayTimeStart.SetSelection(datas['ftsinp'])
            self.panel_three.FridayTimeEnd.SetSelection(datas['fteinp'])
            self.panel_three.SaturdayTimeStart.SetSelection(datas['satsinp'])
            self.panel_three.SaturdayTimeEnd.SetSelection(datas['sateinp'])
            self.panel_seven.grid1.SetCellValue(0,0, "Lesson")
            self.panel_seven.grid1.SetCellValue(0,1, "Date")
            self.panel_seven.grid1.SetCellValue(0,2, "Hours of Estimation")
            for i in range(1,26):
                if(('lesson'+str(i)) in datas or ('date'+str(i)) in datas or ('hours'+str(i)) in datas):
                    self.panel_seven.grid1.SetCellValue(i,0,datas['lesson'+str(i)])
                    self.panel_seven.grid1.SetCellValue(i,1,datas['date'+str(i)])
                    self.panel_seven.grid1.SetCellValue(i,2,datas['hours'+str(i)])
                else:
                    break

    def show_load_dialog(self,event):
        load_dialog = PresetDialog(None, title="Choose the preset that you want to load")
        load_dialog.SetTitle("Choose the preset that you want to load")
        load_dialog.ShowModal()
        if (load_dialog.chose == "Pre1"):
            Program.LoadPreset(self, "Preset1")
        elif (load_dialog.chose == "Pre2"):
            Program.LoadPreset(self, "Preset2")
        if (load_dialog.chose == "Pre3"):
            Program.LoadPreset(self, "Preset3")
        load_dialog.Destroy()
        self.panel_seven.Show()
        self.panel_one.Hide()
        self.Layout()

if __name__ == "__main__":
    app = wx.App(False)
    frame = Program()
    frame.Show()
    app.MainLoop()