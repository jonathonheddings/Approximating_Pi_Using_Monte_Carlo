# Approximating Pi Using Monte Carlo
This python program creates thousands of random points in a coordinate plane and uses the fact that the 4 * ( Area_circle / Area_square) = pi. This follows from the equations for the areas of the circle and squares.

### Overview of The Approximation
This method of approximating Pi is not normal and not necessarily efficient or accurate, but nonetheless, it's still very interesting. The method relies on the relation between the area of a square and its inscribed circle. Pi is equal to four times the ratio of the Area_circle to the Area_square. To approximate Pi using this method, we start by centering the unit circle and unit square on (1,1). Then we generate thousands of completely random points with an even distribution. Because the points have an equal statistical liklihood of being in any particular spot, we can take the number of points as approximations for the Area of both shapes relative to each other. This is done by calculating the number of points that fit inside the circle equations boundaries, and dividing it by the total number of points. Multiplied that by 4 and you have your approximation for Pi.

Here is the core of the program that generates the random points and checks to see if they're in the circle or not:

```python
# Creates a set amount of random x and y coordinates 
#                    and checks if its in the circle
    for i in range(0, iterations):
    
      x = random() * 100
      y = random() * 100

      y_max = math.sqrt(2500 - ((x - 50)**2)) + 50
      y_min = 50 - math.sqrt(2500 - ((x - 50)**2))

      if(y <= y_max and y >= y_min):
          inside_x.append(x)
          inside_y.append(y)
      else:
          outside_x.append(x)
          outside_y.append(y)
          
# Approximates Pi using the area of the circle divided by the overall area of the square 
#                   times four Ac/As = pi * r^2 / 4 * r^2 = pi / 4
    pi_approx = len(inside_x) * 4 / (len(inside_x) + len(outside_x))
    print(pi_approx)
```
### Output Of The Program

The program then takes those random values and graphs the points with colors matching whether they're inside or outside the circle. Here is an example with iterations=100000

![Graph of The Approximation](/Figure_2.png)


Here is another example with a smaller number of iterations


![Another Graph of The Approximation](/Figure_1.png)
