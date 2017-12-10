# Potential goals to bring about a solution to your problems


# The ScrollView portion is sliced in the middle of the screen
# ^ ID factors associated with it, and do a Latin-squares modification with it .

# Don't remember the solutions to my past problems.
# ^ Redo some of the goals
# ^ Write down what I did to make the problem "solved"




# Can I have the welcome screen "pop up" on top of the main screen, instead
# of showing a totally new screen?


from imports import App, Builder, Image, BoxLayout, ScrollView, Window, \
    GridLayout, Label, Button
from kivy.config import Config

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.write()

class WrappedLabel(object):
    """docstring for WrappedLabel."""
    def __init__(self, arg):
        super(WrappedLabel, self).__init__()
        self.arg = arg

linestring = open('text.txt', 'r').read()

#rootLayout
rootLayout = BoxLayout(orientation="vertical", padding = (Window.width * ((1-0.618)/2), 20))

#imageLayout
imageLayout = BoxLayout()
imageLayout.add_widget(Image(source="assets/UnderstatedLogo.png"))

#layoutWithinSV
layoutWithinSV = GridLayout(cols=1, spacing=10, size_hint_y=None, padding = (0, 200))
layoutWithinSV.bind(minimum_height=layoutWithinSV.setter('height'))
aoeu = Label(text=linestring, text_size=(Window.width * 0.618, None), size_hint_y=None, height = Window.height * 1.618, width = Window.height * 0.618, \
                valign="bottom")
layoutWithinSV.add_widget(aoeu)

#(sv)
sv = ScrollView(size_hint=(0.618, None), size=(Window.width, Window.height * (0.618+0.236)))
sv.add_widget(layoutWithinSV)

# rootLayout
rootLayout.add_widget(imageLayout)
rootLayout.add_widget(sv)




class WelcomeApp(App):
    def build(self):
        # height = Window.height
        # width = Window.width
        return rootLayout

if __name__ == '__main__':
	WelcomeApp().run()

# SOLVED The top of the text isn't on the screen.
# ^ Set the position of the scrollview to have a negative position
# ^ Add the scrollview to a BoxLayout, and set a size hint for the scroll ScrollView

# SOLVED There's no logo in the text.
# ^ Implement the second goal of the above and add the image to the BoxLayout

# SOLVED Can't scroll through the text on the welcome screen
# ^ Look at how I did it before, and model that approach
# ^ Put the BoxLayout inside a ScrollView and get it in there.

# SOLVED There's something I* don't get about ScrollView that I* should get
# ^ Play with it in my mind... what are the conditions needed for the ScrollView
#   to work?

# SOLVED Screen has to be smaller than the content
# Content cannot shrink
# Content has to switch what's focused on based on user swipe

# SOLVED (How?) Basically the text is scrolling left to right, and
# ^ Look up other, basic examples of the ScrollView

# SOLVED (Maybe?) Don't have a "self" to refer to when considering text_size

# SOLVED it shows black after scrolling past a certain limit.
# ^ Update the canvas behind the ScrollView

# SOLVED Don't really get how to properly use Git
# ^ Get a Repo created and get everything on there
# ^ Follow a flow from there

# SOLVED Don't know haw to connect Kivy files and Python files functionally--don't
# know how to intermingle data between the two

# SOLVED (Connected, above) Don't know how to access the Window properties from
# Kivy files
# ^ Keep reading SO docs and Kivy docs
# ^ Read the Traceback a bit more.

# SOLVED Can I have a separate file that imports all this, then import that one file
# to get all the imports?

# ^ Look this up on Google
# ^ Try it

# SOLVED Don't know how to change the font family
# ^ Look this up on Google/Kivy documentation

# SOLVED Don't know how to set the background to white.
# ^ Look it up on Kivy.org

# SOLVED The background isn't showing up white.
# ^ Go back to the box layoutWithinSV, and copy everything word for word.

# SOLVED Don't know what to put on the welcome screen
# ^ Put a lorem ipsum - model Tesla's website or the... hmmm

# SOLVED Don't know how to wrap label text
# ^ Ask Google and SO and search the archive

# - SOLVED Don't know how to add a logo
# ^ Ask Google how to add an image in kivy
# ^ Read documentation
# ^ Post a request on SO
# ^ Ask the Kivy forum/IRC/usergroup

# SOLVED Don't know how to resize the logo
# ^ Add the image to its own layoutWithinSV and add padding to it
# ^ Look up the above on Google if that doesn't work

# SOLVED Don't know how to add margin around the text
# ^ Do the same as the above solution
