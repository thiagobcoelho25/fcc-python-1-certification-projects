class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height

  def set_width(self,width):
    self.width = width

  def set_height(self,height):
    self.height = height

  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.width > 50:
      return "Too big for picture."
    else:
      string = ""
      for i in range(self.height):
        string = string + "*"*self.width + "\n"
    return string
  
  def get_amount_inside(self,shape):
    if shape.height <= self.height and shape.width <= self.width:
      heightFit = self.height//shape.height
      widthFit = self.width//shape.width
      return heightFit*widthFit
    else: return 0
  
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
  def __init__(self,side):
    self.width = side
    self.height = side
  
  def set_side(self,side):
    self.width = side
    self.height = side
  
  def __str__(self):
    return f"Square(side={self.width})"