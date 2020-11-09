#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template,  abort
from operator import itemgetter
import os
import io

stories = [
    {"id" : "dweller", "title" : "Dweller", "cat" : "short-stories"},
    {"id" : "sex-on-a-cloud", "title" : "Sex On A Cloud", "cat" : "short-stories"},
    {"id" : "julius-kingsley", "title" : "Julius Kingsley", "cat" : "short-stories"},
    {"id" : "outside-my-window", "title" : "Outside My Window", "cat" : "short-stories"},
    {"id" : "pomegranate", "title" : "Pomegranate", "cat" : "short-stories"},
    {"id" : "quantum-nothing", "title" : "Quantum Nothing", "cat" : "short-stories"},
    {"id" : "ripple", "title" : "Ripple", "cat" : "short-stories"},
    {"id" : "ten-oclock-bus", "title" : "Ten O'clock Bus", "cat" : "short-stories"},
    {"id" : "blades-blade", "title" : "Blade's Blade", "cat" : "short-stories"},
    {"id" : "the-lucky-card", "title" : "The Lucky Card", "cat" : "short-stories"},         
    {"id" : "the-surrogate", "title" : "The Surrogate", "cat" : "short-stories"},
    {"id" : "waiting-room", "title" : "Waiting Room", "cat" : "short-stories"},
    {"id" : "absence", "title" : "Absence", "cat" : "poems"},    
    {"id" : "on-your-birthday", "title" : "On Your Birthday", "cat" : "poems"},
    {"id" : "boomerang", "title" : "Boomerang", "cat" : "poems"},
    {"id" : "cat-heaven", "title" : "Cat Heaven", "cat" : "poems"},
    {"id" : "cool", "title" : "Cool (with audio)", "cat" : "poems"},
    {"id" : "colors", "title" : "Colors (with audio)", "cat" : "poems"},
    {"id" : "fantasy", "title" : "Fantasy", "cat" : "poems"},
    {"id" : "fight", "title" : "Fight", "cat" : "poems"},
    {"id" : "forbidden", "title" : "Forbidden", "cat" : "poems"},
    {"id" : "meditation", "title" : "Meditation", "cat" : "poems"},
    {"id" : "monsters", "title" : "Monsters", "cat" : "poems"},
    {"id" : "numb", "title" : "Numb", "cat" : "poems"},
    {"id" : "one", "title" : "One", "cat" : "poems"},
    {"id" : "strangers", "title" : "Strangers", "cat" : "poems"},
    {"id" : "sunshine", "title" : "Sunshine", "cat" : "poems"},
    {"id" : "vortex", "title" : "Vortex", "cat" : "poems"},
    {"id" : "want", "title" : "Want", "cat" : "poems"},
    {"id" : "zwei-schiffe", "title" : "Zwei Schiffe", "cat" : "poems"},
    {"id" : "bebokia", "title" : "Bebokia", "cat" : "novels"},
    {"id" : "a-place-called-earth", "title" : "A Place Called Earth", "cat" : "novels"},
    {"id" : "myself-as-ten-cents", "title" : "Myself as ten cents", "cat" : "short-stories"},
    {"id" : "the-clients-conscience", "title" : "The Client's Conscience", "cat" : "short-stories"},
    {"id" : "how-i-found-my-magic", "title" : "How I Found My Magic", "cat" : "short-stories"},
    {"id" : "wayward-rock", "title" : "Wayward Rock", "cat" : "short-stories"},
    {"id" : "falling", "title" : "Falling", "cat" : "poems"},
    {"id" : "touched", "title" : "Touched (with audio)", "cat" : "poems"},
    {"id" : "grandmothers-voice", "title" : "Grandmother's Voice", "cat" : "poems"},
    {"id" : "hole-in-my-pocket", "title" : "Hole In My Pocket (with audio)", "cat" : "poems"},
    {"id" : "one-of-them", "title" : "One Of Them", "cat" : "short-stories"},
    {"id" : "dragon-heart", "title" : "Dragon Heart", "cat" : "poems"},
    {"id" : "temptation", "title" : "Temptation", "cat" : "poems"},
    {"id" : "the-look", "title" : "The Look (with audio)", "cat" : "poems"},
    {"id" : "tocada", "title" : "Tocada", "cat" : "poems"},
    {"id" : "all-is-true", "title" : "All Is True", "cat" : "poems"},
    {"id" : "raindrops", "title" : "Raindrops", "cat" : "poems"},
    {"id" : "pride", "title" : "Pride", "cat" : "poems"},
    {"id" : "song-of-sirens", "title" : "Song Of Sirens (with audio)", "cat" : "poems"},
    {"id" : "unintentional", "title" : "Unintentional (with audio)", "cat" : "poems"},
    {"id" : "tap-on-your-door", "title" : "Tap On Your Door", "cat" : "poems"},
    {"id" : "used-to", "title" : "Used to (with audio)", "cat" : "poems"},
    {"id" : "the-tude-in-you", "title" : "The Tude In You (with audio)", "cat" : "poems"},
    {"id" : u"distância", "title" : u"Distância", "cat" : "poems"},
    {"id" : "breathe-into-me", "title" : "Breathe Into Me (with audio)", "cat" : "poems"},
    {"id" : "sequoia", "title" : "Sequoia (with audio)", "cat" : "poems"}
]

app = Flask(__name__)
app.config.update(
    DEBUG = False,
    TESTING = False
)

@app.route('/')
def home():
    return render_template('home.html', title = 'Poems, Novels and Short Stories')

@app.route('/poems/<storyid>/')
@app.route('/short-stories/<storyid>/')
@app.route('/novels/<storyid>/')
def show_story(storyid):
    story_file = "stories/" + storyid + ".html"
    if not os.path.isfile(story_file):
        abort(404)

    with io.open("stories/" + storyid + ".html", mode="r", encoding="utf-8") as f:
        story_html = f.read()

    story = (story for story in stories if story["id"] == storyid).next()
        
    return render_template('story.html', html = story_html, title = story['title'])

@app.route('/about/')
def about():
    return render_template('about.html', title = 'About')

@app.route('/poems/')
def show_poem_category():
    return render_template('category.html', 
        stories = filter_category('poems'), 
        category_title = 'Poems',
        title = 'Poems')

@app.route('/novels/')
def show_novel_category():
    return render_template('category.html', 
        stories = filter_category('novels'), 
        category_title = 'Novels',
        title = 'Novels')


@app.route('/short-stories/')
def show_shortstory_category():
    return render_template('category.html', stories = filter_category('short-stories'), category_title = 'Short Stories', title = 'Short Stories')

@app.route('/sitemap.txt')
def sitemap():
    return render_template('sitemap.txt', stories = stories)


def filter_category(category):
    result = []
    for story in stories:
        if story['cat'] == category:
            result.append(story)
    return sorted(result, key=itemgetter('id')) 


if __name__ == '__main__':
    app.debug = True
    app.run()
