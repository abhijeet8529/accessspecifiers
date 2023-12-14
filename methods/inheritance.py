class movies():
    def __init__(self, moviename, imdb, *args, **kwargs):
        self.moviename = moviename
        self.imdb = imdb

    def showinfo(self, *args, **kwargs):
        print(f"{self.moviename} have an imdb rating of {self.imdb}")


class time(movies):
    def years(self, time):
        self.time = time
        print(f"it was aired from {self.time}")


class part(time):
    def part1(self, sea):
        self.sea = sea
        print(f"it consists of {self.sea}")


x = part("the office", 9.1)
x.showinfo()
x.years("2001-2019, still running")
x.part1("9 seasons\n..........................")
# ..
x1 = part("the walking dead", 8.6)
x1.showinfo()
x1.years("2005-2018")
x1.part1("11 seasons\n.........................")
# ...
x2 = part("harry potter", 8.9)
x2.showinfo()
x2.years("1998-2015")
x2.part1("8 parts\n.............................")
# ....
x3 = part("pirates of carribean", 8.6, "2005-2012")
x3.showinfo()
x3.years("2005-2012")
x3.part1("5 parts\n...............................")
# .....
x4 = part("the modern family", 8.0)
x4.showinfo()
x4.years("2003-2016")
x4.part1("9 seasons\n.............................")
