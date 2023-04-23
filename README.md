# Stickynote

![demo gif](readme_images/demo_gif.gif)

## What is Stickynote Studio ?

This is a computer science project made with Python for my 2nd year in engineering school at the ENSC. My goal is to create a pixel art application to draw and animate, directly inspired by Flipnote Studio, an application available on the Nintendo DS.

## How do I install and run this project ?

If you only want to run the project, you can download the project executable [on that link](https://drive.google.com/file/d/1TA5sFe7A86OtN9kfzm421x26UZ5aVNVR/view?usp=sharing). After extracting the files, you can run Stickynote Studio by double-clikcing on dist/main.exe.

Few packages are needed to run Sticky. It includes Pygame, Pygame-GUI and OpenCV.
To install these packages, do the following request in a prompt :

```
pip install -r requirements.txt
```

Once it is done, you just have to launch the following file :

```
python main.py
```

Now you are ready to draw like a pro !!

## ...But how do I draw and animate ?

Let me describe the interface in front of you and the tools you can use.

![image info](readme_images/1.PNG)

The functionalities available on Stickynote Studio are :
Color choices, represented by squares of the color in question !

- ![image info](/scripts/icons/size_one.png) ![image info](/scripts/icons/size_two.png) ![image info](/scripts/icons/size_three.png) ![image info](/scripts/icons/size_four.png) ![image info](/scripts/icons/verti.png) ![image info](/scripts/icons/horiz.png) The different sizes and shapes of brushes
- ![image info](/scripts/icons/pipette.png) The eyedropper (or pipette), to get a color from your canvas
- ![image info](/scripts/icons/colorpick.png) The color picker, to choose from an infinite number of color choices
- ![image info](/scripts/icons/fill.png) The paint pot, to fill an entire cell with the color you want
- ![image info](/scripts/icons/gomme.png) The eraser, which erases the drawing with the selected brush size
- ![image info](/scripts/icons/clear.png) The clear function, which erases everything on the canva
- ![image info](/scripts/icons/undo.png) The undo button, represented by a backward arrow, to cancel a drawing
- ![image info](/scripts/icons/save.png) The save button, with a floppy disk for saving the video
- ![image info](/scripts/icons/gridpattern.png) The reference grid, to be activated at your leisure to help you
- ![image info](/scripts/icons/layer.png) The reference layer of the previous frame, to help you get a coherent and an even smoother animation
- ![image info](/scripts/icons/add.png) Adding an animation frame, with the + button
- ![image info](/scripts/icons/copy.png) Copying a frame, with the two images represented identically
- ![image info](/scripts/icons/remove.png) The deletion of a frame, where the image is thrown in the trash
- The animation speed choice
- ![image info](/scripts/icons/prev.png) The button to go back to a previous frame
- ![image info](/scripts/icons/next.png) The button to go to a next frame
- ![image info](/scripts/icons/play.png)And between these 2 buttons, the play button which gives a preview of the animation

You now have all the keys to create your masterpiece.

**So get ready, steady, draw !!**
