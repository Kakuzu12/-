import sys
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
if __name__ == '__main__':
    figure=sys.argv[1]
    point=sys.argv[2]
    with open(figure,'r') as ffigure:
        dataf = [list(map(float, line.strip().split(' '))) for line in ffigure]
    with open(point,'r') as fpoint:
        datap = [list(map(float, line.strip().split(' '))) for line in fpoint]
    polygon = Polygon([dataf[0], dataf[1], dataf[2], dataf[3]])
    for i in range(len(datap)):
        if datap[i] in dataf:
            print(0,end='\n')
        else:
            point = Point(datap[i][0], datap[i][1])
            if polygon.touches(point):
                print(1,end='\n')
            elif polygon.contains(point):
                print(2,end='\n')
            else:
                print(3,end='\n')