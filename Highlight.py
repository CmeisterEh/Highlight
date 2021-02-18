# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:52:18 2021

@author: Main Floor
"""

from tkinter import *

####################################################################################################
###
###     Canvas for Highlighting: MouseoverHighlight
###
###        This class allows the text, and possibly nontext widgets in a canvas
###     to be highlighted. Highlighting can be one of the following:
###    1. Changing the Text Colour
###    2. Putting a box around the text
###    3. Changing the background behind the text
###
###
###     Author:  Chad Unterschultz
###
###     V 1.0.0    Feb 13, 2021



debugging = False
VERSION     = (1,0,0)
VERSION_s   = "%s.%s.%s" %VERSION



class MouseoverHighlight:
    """ Class Highlighting a Widget
        Usage: MouseoverHighlight(<widget>, <window>, <canvas>, <scrollbarX>, <scrollbarY>, <scrollregionX>, <scrollregionY>, <text>, <tooltipText>)
        <widget>         = required, widget you are trying to enclose or highlight
        <window>         = required,
        <canvas>         = required,
        <highlight>   = optional, 1 means Change colour, 2 means Surround with Box, 4 means Background Colour Change
                                   , combinations are also acceptable
                                   , 3 means Colour change and Box
                                   , 5 means Colour Change and Background Change
                                   , 6 means Box  and Background Change
                                   , 7 means Colour change and Box and Background change
        <fg>             = text highlight colour
        <bg>             = background highlight colour
        <bbg>            = box highlight colour
    """

    COLOURS  = ['black', 'snow', 'ghost white', 'white smoke', 'gainsboro',
                'floral white', 'old lace', 'linen', 'antique white',
                'papaya whip', 'blanched almond', 'bisque', 'peach puff',
                'navajo white', 'lemon chiffon', 'mint cream', 'azure',
                'alice blue', 'lavender', 'lavender blush', 'misty rose',
                'dark slate gray', 'dim gray', 'slate gray', 'light slate gray',
                'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue',
                'dark slate blue', 'slate blue', 'medium slate blue',
                'light slate blue', 'medium blue', 'royal blue',  'blue',
                'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue',
                'steel blue', 'light steel blue', 'light blue', 'powder blue',
                'pale turquoise', 'dark turquoise', 'medium turquoise',
                'turquoise', 'cyan', 'light cyan', 'cadet blue',
                'medium aquamarine', 'aquamarine', 'dark green',
                'dark olive green', 'dark sea green', 'sea green',
                'medium sea green', 'light sea green', 'pale green',
                'spring green', 'lawn green', 'medium spring green',
                'green yellow', 'lime green', 'yellow green', 'forest green',
                'olive drab', 'dark khaki', 'khaki', 'pale goldenrod',
                'light goldenrod yellow', 'light yellow', 'yellow', 'gold',
                'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
                'indian red', 'saddle brown', 'sandy brown', 'dark salmon',
                'salmon', 'light salmon', 'orange', 'dark orange', 'coral',
                'light coral', 'tomato', 'orange red', 'red', 'hot pink',
                'deep pink', 'pink', 'light pink', 'pale violet red', 'maroon',
                'medium violet red', 'violet red', 'medium orchid',
                'dark orchid', 'dark violet', 'blue violet', 'purple',
                'medium purple', 'thistle', 'snow2', 'snow3', 'snow4',
                'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1',
                'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4', 'bisque2',
                'bisque3', 'bisque4', 'PeachPuff2', 'PeachPuff3', 'PeachPuff4',
                'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4', 'LemonChiffon2',
                'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
                'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2',
                'honeydew3', 'honeydew4', 'LavenderBlush2', 'LavenderBlush3',
                'LavenderBlush4', 'MistyRose2', 'MistyRose3', 'MistyRose4',
                'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2',
                'SlateBlue3', 'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2',
                'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4', 'DodgerBlue2',
                'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
                'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3',
                'DeepSkyBlue4', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4',
                'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3',
                'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
                'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2',
                'LightSteelBlue3', 'LightSteelBlue4', 'LightBlue1',
                'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightCyan2',
                'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
                'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2',
                'CadetBlue3', 'CadetBlue4', 'turquoise1', 'turquoise2',
                'turquoise3', 'turquoise4', 'cyan2', 'cyan3', 'cyan4',
                'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3',
                'DarkSlateGray4', 'aquamarine2', 'aquamarine4', 'DarkSeaGreen1',
                'DarkSeaGreen2', 'DarkSeaGreen3', 'DarkSeaGreen4', 'SeaGreen1',
                'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
                'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3',
                'SpringGreen4', 'green2', 'green3', 'green4', 'chartreuse2',
                'chartreuse3', 'chartreuse4', 'OliveDrab1', 'OliveDrab2',
                'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
                'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2',
                'khaki3', 'khaki4', 'LightGoldenrod1', 'LightGoldenrod2',
                'LightGoldenrod3', 'LightGoldenrod4', 'LightYellow2',
                'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
                'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2',
                'goldenrod3', 'goldenrod4', 'DarkGoldenrod1', 'DarkGoldenrod2',
                'DarkGoldenrod3', 'DarkGoldenrod4', 'RosyBrown1', 'RosyBrown2',
                'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
                'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3',
                'sienna4', 'burlywood1', 'burlywood2', 'burlywood3',
                'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
                'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3',
                'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4',
                'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
                'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3',
                'LightSalmon4', 'orange2', 'orange3', 'orange4', 'DarkOrange1',
                'DarkOrange2', 'DarkOrange3', 'DarkOrange4', 'coral1', 'coral2',
                'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4',
                'OrangeRed2', 'OrangeRed3', 'OrangeRed4', 'red2', 'red3',
                'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4', 'HotPink1',
                'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3',
                'pink4', 'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4',
                'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3',
                'PaleVioletRed4', 'maroon1', 'maroon2', 'maroon3', 'maroon4',
                'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
                'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2',
                'orchid3', 'orchid4', 'plum1', 'plum2', 'plum3', 'plum4',
                'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
                'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3',
                'DarkOrchid4', 'purple1', 'purple2', 'purple3', 'purple4',
                'MediumPurple1', 'MediumPurple2', 'MediumPurple3',
                'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
                'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7',
                'gray8', 'gray9', 'gray10', 'gray11', 'gray12', 'gray13',
                'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
                'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25',
                'gray26', 'gray27', 'gray28', 'gray29', 'gray30', 'gray31',
                'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
                'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44',
                'gray45', 'gray46', 'gray47', 'gray48', 'gray49', 'gray50',
                'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
                'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62',
                'gray63', 'gray64', 'gray65', 'gray66', 'gray67', 'gray68',
                'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
                'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80',
                'gray81', 'gray82', 'gray83', 'gray84', 'gray85', 'gray86',
                'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
                'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

    Canvas_Items = ["arc", "bitmap", "image", "line", "oval", "polygon",
                    "rectangle", "text", "window"]



    def __init__(self, Widget, Root, Canvas_, highlightOption = 0x01, TextColour = 'red', highlight = 'red', defaultOutlineColour = 'black', OutlineWidth = 2, backgroundColour = 'gray' ):
        '''    '''

        self.config_check( Widget, Root, Canvas_, highlightOption, TextColour,
                          highlight, defaultOutlineColour, OutlineWidth,
                          backgroundColour )
        self.highlight()


        pass

    def config_check(self, Widget, Root, Canvas_, highlightOption, TextColour, highlight, defaultOutlineColour, OutlineWidth, backgroundColour ):

        if ( (Root.__class__.__name__ != Tk.__name__) &                        # Test to find out if the Root is a Window or Frame
            ( Root.__class__.__name__ != Frame.__name__) ):
            raise TypeError ("<Root> must be a Window or a Frame")
        else:
            self.Root = Root

        if (Canvas_.__class__.__name__ != Canvas.__name__) :                   # Test to find out if the Canvas is a tkinter Canvas Widget
            raise TypeError ("<Canvas_> must be a Canvas Widget")
        else:
            self.Canvas = Canvas_

        if self.Canvas.type(Widget) not in MouseoverHighlight.Canvas_Items:    # Test to find out if the the Widget is in or of the Canvas
            raise TypeError ("<Widget> must be a Canvas Widget")
        else:
            self.Widget = Widget

        if TextColour != None:                                                 # Test to Ensure TextColour is a string
            if type(TextColour) == str:
                if TextColour in MouseoverHighlight.COLOURS:
                    self.TextColour = TextColour
                else:
                    raise NameError("<TextColour> must be a valid tkinter colour")
            else:
                raise TypeError("<TextColour> must be a string")


        if highlightOption != None:                                            # Test to Ensure integer
            if type(highlightOption) == int:                                   # Test to see if highlightOption is a valid option
                if ( (highlightOption & 0x01 == 0x01) |
                    (highlightOption & 0x02 == 0x02)  |
                    (highlightOption & 0x04 == 0x04)  |
                    (highlightOption == 0) ):
                    self.highlightOption = highlightOption
                else:
                    raise NameError("<highlightOption> ")
            else:
                raise TypeError("<highlightOption> must be an integer")


        if defaultOutlineColour != None:                                       # Test to see if the box outline colour is valid
            if type(defaultOutlineColour) == str:
                if defaultOutlineColour in MouseoverHighlight.COLOURS:
                    self.defaultOutlineColour = defaultOutlineColour
                else:
                    raise NameError("<defaultOutlineColour> must be a valid tkinter colour")
            else:
                raise TypeError("<defaultOutlineColour> must be a string")

        if debugging == True: print("OutlineWidth: ", OutlineWidth)
        if debugging == True: print("Type: ", type(OutlineWidth))
        if debugging == True: print("*****")

        if OutlineWidth != None:
            if type(OutlineWidth) == int:
                self.OutlineWidth = OutlineWidth

            else:

                raise TypeError("<OutlineWidth> must be an integer")

        if backgroundColour != None:
            if type(backgroundColour) == str:
                if backgroundColour in MouseoverHighlight.COLOURS:
                    self.backgroundColour = backgroundColour
                else:
                    raise NameError("<backgroundColour> must be a valid tkinter colour")
            else:
                raise TypeError("<backgroundColour> must be a string")




    def highlight(self):
        ''' Run any and all matching highlight options. For instance, if 0x05
        then run 0x01 and 0x04 together '''
        if self.highlightOption & 0x01 == 0x01:                                      # Change  Colour
            self.changeTextColour()
        if self.highlightOption & 0x02 == 0x02:                                      # Surround with Box
            self.changeTextOutline()
        if self.highlightOption & 0x04 == 0x04:                                      # Background Colour Change
            self.changeTextBackground()

    def config(self, highlightOption = None, TextColour = None, highlight = None, defaultOutlineColour = None, OutlineWidth = None, background = None):
        ''' Allowing the widget and its highlight settings to be modified
        after the fact '''
        Widget = self.Widget
        Root = self.Root
        Canvas_ = self.Canvas

        self.config_check(Widget, Root, Canvas_, highlightOption, TextColour, highlight, defaultOutlineColour, OutlineWidth, background )



##############################################################################
    def changeTextColour(self):
        ''' Highlight by changing the colour of the Canvas Text '''

        if debugging == True: print("Colour Change initialized")

        self.defaultTextColour =  self.Canvas.itemcget(self.Widget, "fill")

        self.countEnter = 0

        self.Canvas.tag_bind(self.Widget, '<Enter>', self.changeTextColour_enter, add = '+')
        self.Canvas.tag_bind(self.Widget, '<Leave>', self.changeTextColour_leave, add = '+')
        self.Root.bind('<Motion>', self.changeTextColour_check, add = '+')

        if debugging == True: print("Change Colour Highlight Initialization Complete")

    def changeTextColour_enter(self, event = None):
        ''' Entering the Text Widget Region causes the text to change colour
        and changing of the text colour indicates the text can be selected '''
        if debugging == True: print("Text Colour Change" )
        self.countEnter = self.countEnter + 1
        if debugging == True: print("Enter count: ", self.countEnter)

        self.Canvas.itemconfig(self.Widget, fill = self.TextColour)

    def changeTextColour_leave(self, event = None):
        ''' Exiting the Text Widget Region should cause the text to change
        back to its default colour, indicated the text is not longer selectable'''

        if debugging == True: print("Text back to normal")

        self.Canvas.itemconfig(self.Widget, fill = self.defaultTextColour)



    def changeTextColour_check(self, event = None):

        mouse_X = event.x
        mouse_Y = event.y
        widget_position = self.Canvas.bbox(self.Widget)
        minX = widget_position[0]
        maxX = widget_position[2]
        minY = widget_position[1]
        maxY = widget_position[3]

        if debugging == True: print(mouse_X, mouse_Y)
        if debugging == True: print(widget_position)


        if minX <= mouse_X <= maxX:                                            # Mouse Cursor outside of Range?
            if debugging == True: print("Inside")
            pass
        else:
            self.changeTextColour_leave()


        if minY <= mouse_Y <= maxY:
            if debugging == True: print("Inside")
            pass
        else:
            self.changeTextColour_leave()






##############################################################################
    def changeTextOutline(self):
        ''' Entering the Text Widget Region causes a box to outline the text '''

        if debugging == True: print("Outline Box Initialized")
        self.Canvas.tag_bind(self.Widget, '<Enter>', self.changeOutline_enter, add = '+')
        self.Canvas.tag_bind(self.Widget, '<Leave>', self.changeOutline_leave, add = '+')
        self.Root.bind('<Motion>', self.changeOutline_check, add = '+')
        self.countEnter = 0

        if debugging == True: print("Outline Box Highlight Initialized")

    def changeOutline_enter(self, event = None) :
        ''' Entering the Text Widget Region Creates an Outline Box '''
        if debugging == True: print("Creating Highlight Box")
        self.countEnter = self.countEnter + 1
        if debugging == True: print("Enter count: ", self.countEnter)

        self.coordinates = self.Canvas.bbox(self.Widget)
        self.highlightBox = self.Canvas.create_rectangle(self.coordinates,
                                                         outline = self.defaultOutlineColour,
                                                         width = self.OutlineWidth)

    def changeOutline_leave(self, event = None):
        ''' Leaving the Text Widget Region Eliminates the Outline Box '''
        if debugging == True: print("Deleting Outline Box")
        self.Canvas.itemconfig(self.Widget, fill = "black")
        if "highlightBox" in self.__dict__.keys():
            self.Canvas.delete(self.highlightBox)
            self.Canvas.update()




    def changeOutline_check(self, event = None):

        mouse_X = event.x
        mouse_Y = event.y
        widget_position = self.Canvas.bbox(self.Widget)
        minX = widget_position[0]
        maxX = widget_position[2]
        minY = widget_position[1]
        maxY = widget_position[3]

        if debugging == True: print(mouse_X, mouse_Y)
        if debugging == True: print(widget_position)


        if minX <= mouse_X <= maxX:                                            # Mouse Cursor outside of Range?
            if debugging == True: print("Inside")
            pass
        else:
            self.changeOutline_leave()


        if minY <= mouse_Y <= maxY:
            if debugging == True: print("Inside")
            pass
        else:
            self.changeOutline_leave()




##############################################################################
    def changeTextBackground(self):
        ''' Passing the Mouse over the Text causes it to be highlighted by way
        of changing the background colour '''

        if debugging == True: print("background change initialized")
        self.coordinates = self.Canvas.bbox(self.Widget)
        self.Canvas.tag_bind(self.Widget, '<Enter>', self.changeBackground_enter, add = '+')
        self.Canvas.tag_bind(self.Widget, '<Leave>', self.changeBackground_leave, add = '+')
        self.Root.bind('<Motion>', self.changeBackground_check, add = '+')


    def changeBackground_enter(self, event = None):
        ''' Passing the  Mouse over the Text causes it to be highlighted by way
        of changing the background colour '''
        self.coordinates = self.Canvas.bbox(self.Widget)
        self.background = self.Canvas.create_rectangle(self.coordinates,
                                                       fill = self.backgroundColour,
                                                       outline = self.backgroundColour)
        self.Canvas.tag_lower(self.background)
        self.Canvas.tag_raise(self.Widget)
        self.Canvas.update()

    def changeBackground_leave(self, event = None):
        ''' Leaving the Text Widget Region Returns the background colour
        to its normal default state '''
        if "background" in self.__dict__.keys():

            self.Canvas.delete(self.background)
            self.Canvas.update()


    def changeBackground_check(self, event = None):

        mouse_X = event.x
        mouse_Y = event.y
        widget_position = self.Canvas.bbox(self.Widget)
        minX = widget_position[0]
        maxX = widget_position[2]
        minY = widget_position[1]
        maxY = widget_position[3]

        if debugging == True: print(mouse_X, mouse_Y)
        if debugging == True: print(widget_position)


        if minX <= mouse_X <= maxX:                                            # Mouse Cursor outside of Range?
            if debugging == True: print("Inside")
            pass
        else:
            self.changeBackground_leave()


        if minY <= mouse_Y <= maxY:
            if debugging == True: print("Inside")
            pass
        else:
            self.changeBackground_leave()



    def version(self):
        global VERSION_S
        global DATE
        if debugging == True: print(VERSION_S)
        if debugging == True: print( DATE )
        return VERSION_S, DATE



if __name__ == "__main__":

    if debugging == True: print("Library File Test")

    Root = Tk()
    Root.focus_set()

    canvas = Canvas(Root, width = 400, height = 400)
    canvas.pack()

    canvasText1 = canvas.create_text(10, 10, text = "Colour Change Highlight", anchor = NW)
    canvasText1_highlight = MouseoverHighlight(canvasText1, Root, canvas, highlightOption = 0x01)

    canvasText2 = canvas.create_text(10, 50, text = "Box Outline Highlight", anchor = NW)
    canvasText2_highlight = MouseoverHighlight(canvasText2, Root, canvas, highlightOption = 0x02)

    canvasText3 = canvas.create_text(10, 100, text = "Background Highlgiht", anchor = NW)
    canvasText3_highlight = MouseoverHighlight(canvasText3, Root, canvas, highlightOption = 0x04)

    canvasText4 = canvas.create_text(10, 160, text = "Background Highlight", anchor = NW)
    canvasText4_highlight = MouseoverHighlight(canvasText4, Root, canvas, highlightOption = 1)
    canvasText4_highlight2 = MouseoverHighlight(canvasText4, Root, canvas, highlightOption = 2)
    canvasText4_highlight3 = MouseoverHighlight(canvasText4, Root, canvas, highlightOption = 4)

    Root.mainloop()

