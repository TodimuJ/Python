from urllib import request
from datetime import date, datetime, timedelta


def multiple():
    sites = []
    mySite = input("Type the URL to the link: ")
    sites.append(mySite)
    print("")
    fmts = ['txt', 'doc', 'xlsx', 'pdf', 'xml']
    print("Type the number of a format below:")
    print("")
    for i in range(len(fmts)):
        print(i, fmts[i])

    print("")
    fmt = int(input(""))

    for site in sites:
        response = request.urlopen(site)
        txt = response.read()
        txt_str = str(txt)
        lines = txt_str.split("\\n")
        today = datetime.now().strftime("%Y-%m-%d")
        destination = r'./' + '{}'.format(today) + '.' + fmts[fmt]
        fx = open(destination, "w")
        for line in lines:
            fx.write(line + "\n")
        fx.close()



   
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





