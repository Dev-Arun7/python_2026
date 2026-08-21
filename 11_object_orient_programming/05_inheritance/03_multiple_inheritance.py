"""
Learning: Multiple Inheritance with Different Child Classes

In this example:

Writer
   |
   |--- Novelist
   |
   |--- GraphicNovel
          |
          |
Artist     |
   |       |
   |-------+
   |
   |--- Painter


Novelist inherits from Writer.
Painter inherits from Artist.
GraphicNovel inherits from both Writer and Artist.

This shows that:

    One child can inherit from one parent.

And:

    Another child can inherit from a different parent.

And:

    One child can inherit from both parents.
"""


# ---------------------------------------------------
# Writer Class
# ---------------------------------------------------

class Writer:

    # Method
    def write(self):
        print("Writing a story.")


# ---------------------------------------------------
# Artist Class
# ---------------------------------------------------

class Artist:

    # Method
    def draw(self):
        print("Drawing a picture.")


# ---------------------------------------------------
# Novelist Class
# ---------------------------------------------------

# Novelist inherits from Writer
class Novelist(Writer):

    # Novelist has its own method
    def write_novel(self):
        print("Writing a novel.")


# ---------------------------------------------------
# Painter Class
# ---------------------------------------------------

# Painter inherits from Artist
class Painter(Artist):

    # Painter has its own method
    def paint(self):
        print("Painting a picture.")


# ---------------------------------------------------
# GraphicNovel Class
# ---------------------------------------------------

# GraphicNovel inherits from both Writer and Artist
class GraphicNovel(Writer, Artist):

    # GraphicNovel has its own method
    def create_graphic_novel(self):
        print("Creating a graphic novel.")


# ---------------------------------------------------
# Creating Objects
# ---------------------------------------------------

# Creating a Novelist object
novelist = Novelist()

# Creating a Painter object
painter = Painter()

# Creating a GraphicNovel object
graphic_novel = GraphicNovel()


# ---------------------------------------------------
# Using Novelist Object
# ---------------------------------------------------

print("Novelist:")

# write() comes from the Writer class
novelist.write()

# write_novel() comes from the Novelist class
novelist.write_novel()

print()


# ---------------------------------------------------
# Using Painter Object
# ---------------------------------------------------

print("Painter:")

# draw() comes from the Artist class
painter.draw()

# paint() comes from the Painter class
painter.paint()

print()


# ---------------------------------------------------
# Using GraphicNovel Object
# ---------------------------------------------------

print("Graphic Novel:")

# write() comes from the Writer class
graphic_novel.write()

# draw() comes from the Artist class
graphic_novel.draw()

# create_graphic_novel() comes from the GraphicNovel class
graphic_novel.create_graphic_novel()


"""
===================================================
DETAILED NOTE: MULTIPLE INHERITANCE
===================================================

This example demonstrates multiple inheritance
together with normal inheritance.

We have two parent classes:

    Writer
    Artist


---------------------------------------------------
1. Writer Class
---------------------------------------------------

The Writer class has a method:

    write()

Any class that inherits from Writer can use
the write() method.


---------------------------------------------------
2. Artist Class
---------------------------------------------------

The Artist class has a method:

    draw()

Any class that inherits from Artist can use
the draw() method.


---------------------------------------------------
3. Novelist Class
---------------------------------------------------

Novelist inherits from Writer:

    class Novelist(Writer):

So Novelist can use:

    write()

Novelist also has its own method:

    write_novel()

Therefore, a Novelist object can use:

    write()        -> Writer
    write_novel()  -> Novelist


---------------------------------------------------
4. Painter Class
---------------------------------------------------

Painter inherits from Artist:

    class Painter(Artist):

So Painter can use:

    draw()

Painter also has its own method:

    paint()

Therefore, a Painter object can use:

    draw()     -> Artist
    paint()    -> Painter


---------------------------------------------------
5. GraphicNovel Class
---------------------------------------------------

GraphicNovel is the important part.

It inherits from both Writer and Artist:

    class GraphicNovel(Writer, Artist):

This means GraphicNovel gets methods from:

    Writer
    Artist

So a GraphicNovel object can use:

    write()  -> Writer
    draw()   -> Artist

GraphicNovel also has its own method:

    create_graphic_novel()


---------------------------------------------------
The Important Structure
---------------------------------------------------

The inheritance structure is:

        Writer                 Artist
          |                      |
          |                      |
          ↓                      ↓
      Novelist                Painter

          Writer + Artist
                |
                ↓
          GraphicNovel


So we have:

    Novelist(Writer)

    Painter(Artist)

    GraphicNovel(Writer, Artist)


This is the main idea of this example.


---------------------------------------------------
Why is GraphicNovel using two parents?
---------------------------------------------------

A graphic novel needs both writing and drawing.

Writer provides:

    write()

Artist provides:

    draw()

So instead of writing those methods again inside
GraphicNovel, we can inherit both classes.

Therefore:

    GraphicNovel(Writer, Artist)


---------------------------------------------------
Three Different Types of Child Classes
---------------------------------------------------

In this example we can compare three cases.

Case 1:

    class Novelist(Writer):

One child inherits from one parent.


Case 2:

    class Painter(Artist):

Another child inherits from another parent.


Case 3:

    class GraphicNovel(Writer, Artist):

One child inherits from two parents.


---------------------------------------------------
Simple Definition
---------------------------------------------------

Multiple inheritance means:

    A class can inherit from more than one
    parent class.

In our example:

    GraphicNovel

inherits from:

    Writer
    Artist

Therefore GraphicNovel is an example of
multiple inheritance.


---------------------------------------------------
Important Point
---------------------------------------------------

Multiple inheritance does not mean that every
child class must have multiple parents.

A project can contain:

    One parent
        ↓
      Child

and also:

    Two parents
        ↓
      Child

at the same time.

That is exactly what we are showing here.


---------------------------------------------------
What happens when both parents have the same method?
---------------------------------------------------

Suppose both Writer and Artist have a method
with the same name:

    def work(self):

Then GraphicNovel would receive that method from
both parent classes.

Python needs to decide which method should be used.

Python solves this using:

    MRO

MRO means:

    Method Resolution Order

It defines the order Python follows when searching
for a method.

We will study MRO separately.
"""