# Potential goals to bring about a solution to your problems

# Can't scroll through the text on the welcome screen
# ^ Look at how I did it before, and model that approach
# ^ Put the BoxLayout inside a ScrollView and get it in there.

# Basically the text is scrolling left to right, and
# ^ Look up other, basic examples of the ScrollView


# Can I have the welcome screen "pop up" on top of the main screen, instead
# of showing a totally new screen?


from imports import App, Builder, Image, BoxLayout, ScrollView, Window, \
    GridLayout

print("\n \n APP START \n \n ")

# print("HEY, LISTEN: \n\n Window.height:", Window.height)

class BestScrollView(ScrollView):
    """docstring for BestScrollView."""

    def __init__(self, **kwargs):
        super(BestScrollView, self).__init__(**kwargs)

    def getWindowSize():
        return Window.height, Window.width


root = Builder.load_file("welcome.kv")

# scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
# root.add_widget(layout)

class WelcomeApp(App):



    def build(self):
        # height = Window.height
        # width = Window.width
        return root
    def Window_Size():
        print("HEY, LISTEN: \n\n Window.height:", Window.height)
        window_size = Window.height, Window.width
        return window_size

if __name__ == '__main__':
	WelcomeApp().run()

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
# ^ Go back to the box layout, and copy everything word for word.

# SOLVED Don't know what to put on the welcome screen
# ^ Put a lorem ipsum - model Tesla's website or the... hmmm

# SOLVED Don't know how to wrap label text
# ^ Ask Google and SO and search the archive

# SOLVED Don't know how to add a logo
# ^ Ask Google how to add an image in kivy
# ^ Read documentation
# ^ Post a request on SO
# ^ Ask the Kivy forum/IRC/usergroup

# SOLVED Don't know how to resize the logo
# ^ Add the image to its own layout and add padding to it
# ^ Look up the above on Google if that doesn't work

# SOLVED Don't know how to add margin around the text
# ^ Do the same as the above solution
