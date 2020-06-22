def week(w):
    switcher={
        0:"Sunday",
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday"
    }
    return switcher.get(w,"Invalid week")

print(week(3))
print(week(7))