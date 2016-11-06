from tkinter import *

top = Tk()

# initialize the score
wharton_score = 0
harvard_score = 0
stanford_score = 0
mit_score = 0

def vote_wharton():
    global wharton_score
    wharton_score += 1
    score_wharton["text"] = wharton_score
    results["text"] = result()

def vote_harvard():
    global harvard_score
    harvard_score += 1
    score_harvard["text"] = harvard_score
    results["text"] = result()

def vote_stanford():
    global stanford_score
    stanford_score += 1
    score_stanford["text"] = stanford_score
    results["text"] = result()

def vote_mit():
    global mit_score
    mit_score += 1
    score_mit["text"] = mit_score
    results["text"] = result()

def result():
    if wharton_score > harvard_score and wharton_score > stanford_score and wharton_score > mit_score:
        return 'Wharton'
    elif harvard_score > wharton_score and harvard_score > stanford_score and harvard_score > mit_score:
        return 'Harvard'
    elif stanford_score > wharton_score and stanford_score > harvard_score and stanford_score > mit_score:
        return 'Stanford'
    elif mit_score > wharton_score and mit_score > harvard_score and mit_score > stanford_score:
        return 'MIT'
    else:
        return 'Tied'


# frame1
frame1 = Frame(top)
frame1.pack(side='top')
top_label = Label(frame1, text="Vote for your favorite MBA school!")
top_label.pack()

# frame 2
frame2 = Frame(top, bg='light gray')
frame2.pack(side='bottom', fill=BOTH)
school_label = Label(frame2, bg='light gray', text="Schools")
school_label.grid(row=0, column=0, padx=40)
vote_label = Label(frame2, bg='light gray', text="Votes")
vote_label.grid(row=0, column=1, padx=40)
winner = Label(frame2, bg='light gray', text="Winner so far:")
winner.grid(row=5, column=0)
results = Label(frame2, bg='light gray', text="Tied")
results.grid(row=5, column=1)

# buttons show up
Button(frame2, text="Wharton", command=vote_wharton).grid(row=1, column=0, sticky=W+E)
Button(frame2, text="Harvard",  command=vote_harvard).grid(row=2, column=0, sticky=W+E)
Button(frame2, text="Stanford", command=vote_stanford).grid(row=3, column=0, sticky=W+E)
Button(frame2, text="MIT", command=vote_mit).grid(row=4, column=0, sticky=W+E)

# scores show up
score_wharton = Label(frame2, text=wharton_score, bg='light gray')
score_wharton.grid(row=1, column=1)
score_harvard = Label(frame2, text=harvard_score, bg='light gray')
score_harvard.grid(row=2, column=1)
score_stanford = Label(frame2, text=harvard_score, bg='light gray')
score_stanford.grid(row=3, column=1)
score_mit = Label(frame2, text=harvard_score, bg='light gray')
score_mit.grid(row=4, column=1)

mainloop()
