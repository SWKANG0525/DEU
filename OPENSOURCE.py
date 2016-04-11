from urllib.request import *
from tkinter import *
import re



def switch(*args):
    if (cityvar.get() == "서울"):
        cityvalue.set(get_current_teamperature("서울"))
    elif (cityvar.get() == "대구"):
        cityvalue.set(get_current_teamperature("대구"))
    elif (cityvar.get() == "부산"):
        cityvalue.set(get_current_teamperature("부산"))
    elif (cityvar.get() == "제주"):
        cityvalue.set(get_current_teamperature("제주"))
    elif (cityvar.get() == "광주"):
        cityvalue.set(get_current_teamperature("광주"))

def get_current_teamperature(cityname):
    sitesource = urlopen(SITE).read().decode('cp949')
    valueresult = []
    for i in weathervalue.finditer(sitesource):
        if i.groups()[0] in cityname:

            valueresult.append("일기: "+str( i.groups()[1]))
            valueresult.append("온도:"+str ((i.groups()[2])))

    return str(valueresult)


app = Tk()
SITE = "http://www.kma.go.kr/weather/observation/currentweather.jsp"
city_list=('부산', '서울', '광주', '대구', '제주')


weathervalue = re.compile(
    r'<tr>.*?<td><a.*?>(.*?)</a></td>.*?'
    r'<td>(.*?)</td>.*?'
    r'<td.*?/td>.*?'
    r'<td.*?/td>.*?'
    r'<td.*?/td>.*?'
    r'<td>(.*?)</td>'

    , re.DOTALL)

app.title("현재기온과 날씨")
app.geometry("400x200+100+100")

cityvalue = StringVar()
cityvalue.set(get_current_teamperature("부산"))
lab = Label(app,textvariable=cityvalue, height = 2)
lab.pack()

Label(app,text="도시명").pack(side="left")
cityvar = StringVar()
cityvar.set(city_list[0])

optionmenu= OptionMenu(app, cityvar, *city_list)
cityvar.trace("w",lambda *args: switch())
optionmenu.pack(side="right")

button = Button(app, text="Refresh", width=20, command= cityvar.trace("w",lambda *args: switch()))
button.pack(padx=5,pady=5)
app.mainloop()
