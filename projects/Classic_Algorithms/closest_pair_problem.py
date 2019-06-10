from math import pow, sqrt

#calculate the distance between 2 points
def distance(tuple1, tuple2):
    x1, y1 = tuple1[0], tuple1[1]
    x2, y2 = tuple2[0], tuple2[1]
    d = pow((x1 - x2), 2) + pow((y1 - y2), 2)
    d = sqrt(d)
    return d

def createPoint(x, y):
    point = ()
    """point.append"""

def compareDistance(points):
    if (len(points)/2)%2 == 0:
        #Create two sublist
        middle = int(len(points)/2)
        #left sublist
        left_points = [points[i] for i in range(middle)]
        # right sublist        
        right_points = [points[i] for i in range(middle, len(points))]

        for i in range(0, middle, 2):
            left_point = (left_points[i], left_points[i+1])
            right_point = (right_points[i], right_points[i+1])
            print(distance(left_point, right_point))
        
    print(left_points)
    print(right_points)

if __name__ == "__main__":
    points = list(map(int, input("Enter all points seperated with commas\n> ").split(', ')))
    compareDistance(points)