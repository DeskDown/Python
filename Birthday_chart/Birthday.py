"""
Birthday Dictionaries

https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html
https://www.practicepython.org/exercise/2017/04/02/36-birthday-plots.html

"""

import json
from collections import Counter as cnt
from bokeh.plotting import figure, show, output_file


def show_birthday(recs):
    inp = input("Who's birthday do you want to look up?").strip()
    if inp in recs:
        print(f"{inp}'s birthday is {recs[inp]}")
    else:
        print(f"Sorry, we don't have any record for {inp}")


def add_recs(recs):
    name = input("Enter name of the Person:").strip()
    if name not in recs:
        bd = input(f"Enter {name}'s birthday:").strip()
        recs[name] = bd.strip()
        print(f"{name}'s birthday added in the record.")
    else:
        print("Sorry! we already have this information.")


def update_recs(fname,recs):
    print(fname,recs.keys())
    with open(fname,"w") as f:
        json.dump(recs,f)


def plot(data, months):
    output_file("Birthdays_chart.html")
    x_axis = list(data.keys())
    y_axis = list(data.values())
    box = 1000
    p = figure(plot_width = box, plot_height = box//2, x_range = months)
    p.vbar(x=x_axis, top=y_axis, width=0.5)
    show(p)
    

if __name__ == "__main__":
    month_map = {
            1:"january",
            2:"fabruary",
            3:"march",
            4:"april",
            5:"may",
            6:"june",
            7:"july",
            8:"august",
            9:"september",
            10:"october",
            11:"november",
            12:"december"
            }
    fname = "recs.json"
    welcome = "Welcome to the birthday dictionary. We know the birthdays of:"
    print(welcome)
    with open(fname,"r") as f:
        recs = json.load(f)

    show_birthday(recs)
#    add_recs(recs)
#    update_recs(fname,recs)
    for k in  month_map:
        month_map[k] = month_map[k].capitalize()

    months = [month_map[int(a.split("/")[0])] for a in recs.values()]
    births_x_month = cnt(months)
    plot(births_x_month, list(month_map.values()))