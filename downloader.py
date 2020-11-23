from urllib import request
from datetime import date, datetime, timedelta

sites = ['']

def multiple():
    index = 0
    for site in sites:
        response = request.urlopen(site)
        txt = response.read()
        txt_str = str(txt)
        lines = txt_str.split("\\n")
        today = datetime.now().strftime("%Y-%m-%d")
        destination = r'"File Path"' + '{}'.format(today) + '__({})' + '.pdf'
        fx = open(destination, "w")
        for line in lines:
            fx.write(line + "\n")
        fx.close()
        index += 1



   
def single(website):
    response = request.urlopen(website)
    txt = response.read()
    txt_str = str(txt)
    lines = txt_str.split("\\n")
    today = datetime.now().strftime("%Y-%m-%d")
    destination = r'"File Path"' + '{}.txt'.format(today)
    fx = open(destination, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()


#single(sites[2])
multiple()
#single(website)





