def is_triangle(sides):
    a, b, c = sides
    if a + b < c:
        return False
    
    if b + c < a:
        return False
    
    if c + a < b:
        return False
    
    return True
        
def equilateral(sides):
    side_sets = set(sides)
    return is_triangle(sides) and (len(side_sets) == 1 and 0 not in side_sets)

def isosceles(sides):
    side_sets = set(sides)
    return is_triangle(sides) and (len(side_sets) in [1, 2]) 

def scalene(sides):
    side_sets = set(sides)
    return is_triangle(sides) and len(side_sets) == 3
