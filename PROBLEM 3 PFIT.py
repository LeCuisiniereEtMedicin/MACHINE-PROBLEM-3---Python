import numpy as np
points = np.array(eval(input('Enter data points in form of [x,y]i:\n ex. [1,2],[3,4],[5,6]: \n')))
x = points[:,0]
y = points[:,1]
p1 = np.polyfit(x,y,1)
p2 = np.polyfit(x,y,2)
p3 = np.polyfit(x,y,3)
p4 = np.polyfit(x,y,4)
p5 = np.polyfit(x,y,5)
p6 = np.polyfit(x,y,6)
p7 = np.polyfit(x,y,7)
p8 = np.polyfit(x,y,8)
p9 = np.polyfit(x,y,9)
p10 = np.polyfit(x,y,10)
e1 = np.linalg.norm(y - np.polyval(p1,x))
e2 = np.linalg.norm(y - np.polyval(p2,x))
e3 = np.linalg.norm(y - np.polyval(p3,x))
e4 = np.linalg.norm(y - np.polyval(p4,x))
e5 = np.linalg.norm(y - np.polyval(p5,x))
e6 = np.linalg.norm(y - np.polyval(p6,x))
e7 = np.linalg.norm(y - np.polyval(p7,x))
e8 = np.linalg.norm(y - np.polyval(p8,x))
e9 = np.linalg.norm(y - np.polyval(p9,x))
e10 = np.linalg.norm( y - np.polyval(p10,x))
error = np.array([(e1),(e2),(e3),(e4),(e5),(e6),(e7),(e8),(e9),(e10)],dtype=float)
error.sort()
if round(error[0],100)==round(e1,100):
    print('\n The coefficients of best fit curve are ',p1)
if round(error[0],100)==round(e2,100):
    print('\n The coefficients of best fit curve are ',p2)
if round(error[0],100)==round(e3,100):
    print('\n The coefficients of best fit curve are ',p3)
if round(error[0],100)==round(e4,100):
    print('\n The coefficients of best fit curve are ',p4)
if round(error[0],100)==round(e5,100):
    print('\n The coefficients of best fit curve are ',p5)
if round(error[0],100)==round(e6,100):
    print('\n The coefficients of best fit curve are ',p6)
if round(error[0],100)==round(e7,100):
    print('\n The coefficients of best fit curve are ',p7)
if round(error[0],100)==round(e8,100):
    print('\n The coefficients of best fit curve are ',p8)
if round(error[0],100)==round(e9,100):
    print('\n The coefficients of best fit curve are ',p9)
if round(error[0],100)==round(e10,100):
    print('\n The coefficients of best fit curve are ',p10)
