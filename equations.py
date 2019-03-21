import cmath

'''
def find_closest_three(points):
    difference = 1.7976931348623157e+308;
    costArray=[1,1,1];
    for point in points:
       for point2 in points:
         if point == point2:
            break;
       
       for point3 in points:
          if point == point3 or point3 == point2:
            break

          if difference > abs(point-point3):
             difference = abs(point-point3)
             costArray[0]=point;
             costArray[1]=point2;
             costArray[2]=point3;
          


    x_s = np.array([costArray[0], costArray[1], costArray[2]])
    gela = x_s.mean()
    return gela
        
'''
 
def y_axis_inter(a1, a2, a3):
    try:
        x1 = cmath.sqrt(-(a1*2.0-1.0)*(a1*2.0+1.0)*(a1*a1+a2*a2-(a1*a1*a1*a1*a1)*2.0-(a2*a2*a2*a2)*4.0-(a2*a2*a2*a2*a2)*2.0+(a2*a2*a2*a2*a2*a2*a2)*8.0-(a1*a1)*(a2*a2)*1.2E1+(a1*a1)*(a2*a2*a2)*2.0+(a1*a1*a1)*(a2*a2)*2.0+(a1*a1)*(a2*a2*a2*a2)*3.2E1-(a1*a1)*(a2*a2*a2*a2*a2)*8.0-(a1*a1*a1)*(a2*a2*a2*a2)*8.0+(a1*a1*a1*a1*a1)*(a2*a2)*8.0-a1*a2*cmath.sqrt(a2*2.0-1.0)*cmath.sqrt(a2*2.0+1.0)*cmath.sqrt(((a2*a2)*4.0-1.0)*(a1*(a2*a2)*2.0+(a1*a1)*a2*2.0-(a1*a1)*4.0-(a1*a1*a1)*2.0-(a2*a2)*4.0-(a2*a2*a2)*2.0+(a1*a1*a1*a1*a1)*8.0+(a2*a2*a2*a2*a2)*8.0+(a1*a1)*(a2*a2)*1.6E1-(a1*a1)*(a2*a2*a2)*8.0-(a1*a1*a1)*(a2*a2)*8.0+1.0))*2.0))/((a1*a1)*2.0-(a2*a2)*2.0);
        #x2 = cmath.sqrt(-(a1*2.0-1.0)*(a1*2.0+1.0)*(a1*a1+a2*a2-(a1*a1*a1*a1*a1)*2.0-(a2*a2*a2*a2)*4.0-(a2*a2*a2*a2*a2)*2.0+(a2*a2*a2*a2*a2*a2*a2)*8.0-(a1*a1)*(a2*a2)*1.2E1+(a1*a1)*(a2*a2*a2)*2.0+(a1*a1*a1)*(a2*a2)*2.0+(a1*a1)*(a2*a2*a2*a2)*3.2E1-(a1*a1)*(a2*a2*a2*a2*a2)*8.0-(a1*a1*a1)*(a2*a2*a2*a2)*8.0+(a1*a1*a1*a1*a1)*(a2*a2)*8.0+a1*a2*cmath.sqrt(a2*2.0-1.0)*cmath.sqrt(a2*2.0+1.0)*cmath.sqrt(((a2*a2)*4.0-1.0)*(a1*(a2*a2)*2.0+(a1*a1)*a2*2.0-(a1*a1)*4.0-(a1*a1*a1)*2.0-(a2*a2)*4.0-(a2*a2*a2)*2.0+(a1*a1*a1*a1*a1)*8.0+(a2*a2*a2*a2*a2)*8.0+(a1*a1)*(a2*a2)*1.6E1-(a1*a1)*(a2*a2*a2)*8.0-(a1*a1*a1)*(a2*a2)*8.0+1.0))*2.0))/((a1*a1)*2.0-(a2*a2)*2.0);
        '''
        intersection of h_1_2_y and h_2_3_y
        '''
        x3 = (cmath.sqrt(-(a3-1.0)*(a3+1.0)*((a2*a2)*4.0+a3*a3-(a2*a2*a2*a2)*1.6E1-(a2*a2*a2*a2*a2)*3.2E1-(a3*a3*a3*a3*a3)*8.0+(a2*a2*a2*a2*a2*a2*a2)*1.28E2-(a2*a2)*(a3*a3)*1.2E1+(a2*a2)*(a3*a3*a3)*3.2E1+(a2*a2*a2)*(a3*a3)*8.0+(a2*a2*a2*a2)*(a3*a3)*3.2E1+(a2*a2)*(a3*a3*a3*a3*a3)*3.2E1-(a2*a2*a2*a2)*(a3*a3*a3)*1.28E2-(a2*a2*a2*a2*a2)*(a3*a3)*3.2E1-a2*a3*cmath.sqrt(a2*2.0-1.0)*cmath.sqrt(a2*2.0+1.0)*cmath.sqrt(((a2*a2)*4.0-1.0)*(a2*(a3*a3)*2.0+(a2*a2)*a3*3.2E1-(a2*a2)*4.0-(a2*a2*a2)*8.0-a3*a3-(a3*a3*a3)*8.0+(a2*a2*a2*a2*a2)*3.2E1+(a3*a3*a3*a3*a3)*8.0+(a2*a2)*(a3*a3)*4.0-(a2*a2)*(a3*a3*a3)*3.2E1-(a2*a2*a2)*(a3*a3)*8.0+1.0))*4.0))*(-1.0/2.0))/((a2*a2)*4.0-a3*a3);
        #x4 = (cmath.sqrt(-(a3-1.0)*(a3+1.0)*((a2*a2)*4.0+a3*a3-(a2*a2*a2*a2)*1.6E1-(a2*a2*a2*a2*a2)*3.2E1-(a3*a3*a3*a3*a3)*8.0+(a2*a2*a2*a2*a2*a2*a2)*1.28E2-(a2*a2)*(a3*a3)*1.2E1+(a2*a2)*(a3*a3*a3)*3.2E1+(a2*a2*a2)*(a3*a3)*8.0+(a2*a2*a2*a2)*(a3*a3)*3.2E1+(a2*a2)*(a3*a3*a3*a3*a3)*3.2E1-(a2*a2*a2*a2)*(a3*a3*a3)*1.28E2-(a2*a2*a2*a2*a2)*(a3*a3)*3.2E1+a2*a3*cmath.sqrt(a2*2.0-1.0)*cmath.sqrt(a2*2.0+1.0)*cmath.sqrt(((a2*a2)*4.0-1.0)*(a2*(a3*a3)*2.0+(a2*a2)*a3*3.2E1-(a2*a2)*4.0-(a2*a2*a2)*8.0-a3*a3-(a3*a3*a3)*8.0+(a2*a2*a2*a2*a2)*3.2E1+(a3*a3*a3*a3*a3)*8.0+(a2*a2)*(a3*a3)*4.0-(a2*a2)*(a3*a3*a3)*3.2E1-(a2*a2*a2)*(a3*a3)*8.0+1.0))*4.0))*(-1.0/2.0))/((a2*a2)*4.0-a3*a3);

        '''
        intersection of h_1_3_y and h_2_3_y
        '''
        
        
        x5 = -(cmath.sqrt(-(a3-1.0)*(a3+1.0)*((a1*a1)*4.0-(a1*a1*a1*a1)*1.6E1+a3*a3-(a1*a1*a1*a1*a1)*3.2E1+(a1*a1*a1*a1*a1*a1*a1)*1.28E2-(a3*a3*a3*a3*a3)*8.0-(a1*a1)*(a3*a3)*1.2E1+(a1*a1)*(a3*a3*a3)*3.2E1+(a1*a1*a1)*(a3*a3)*8.0+(a1*a1*a1*a1)*(a3*a3)*3.2E1+(a1*a1)*(a3*a3*a3*a3*a3)*3.2E1-(a1*a1*a1*a1)*(a3*a3*a3)*1.28E2-(a1*a1*a1*a1*a1)*(a3*a3)*3.2E1-a1*a3*cmath.sqrt(a1*2.0-1.0)*cmath.sqrt(a1*2.0+1.0)*cmath.sqrt(((a1*a1)*4.0-1.0)*(a1*(a3*a3)*2.0+(a1*a1)*a3*3.2E1-(a1*a1)*4.0-(a1*a1*a1)*8.0-a3*a3+(a1*a1*a1*a1*a1)*3.2E1-(a3*a3*a3)*8.0+(a3*a3*a3*a3*a3)*8.0+(a1*a1)*(a3*a3)*4.0-(a1*a1)*(a3*a3*a3)*3.2E1-(a1*a1*a1)*(a3*a3)*8.0+1.0))*4.0))*(-1.0/2.0))/((a1*a1)*4.0-a3*a3);
        #x6 = -(cmath.sqrt(-(a3-1.0)*(a3+1.0)*((a1*a1)*4.0-(a1*a1*a1*a1)*1.6E1+a3*a3-(a1*a1*a1*a1*a1)*3.2E1+(a1*a1*a1*a1*a1*a1*a1)*1.28E2-(a3*a3*a3*a3*a3)*8.0-(a1*a1)*(a3*a3)*1.2E1+(a1*a1)*(a3*a3*a3)*3.2E1+(a1*a1*a1)*(a3*a3)*8.0+(a1*a1*a1*a1)*(a3*a3)*3.2E1+(a1*a1)*(a3*a3*a3*a3*a3)*3.2E1-(a1*a1*a1*a1)*(a3*a3*a3)*1.28E2-(a1*a1*a1*a1*a1)*(a3*a3)*3.2E1+a1*a3*cmath.sqrt(a1*2.0-1.0)*cmath.sqrt(a1*2.0+1.0)*cmath.sqrt(((a1*a1)*4.0-1.0)*(a1*(a3*a3)*2.0+(a1*a1)*a3*3.2E1-(a1*a1)*4.0-(a1*a1*a1)*8.0-a3*a3+(a1*a1*a1*a1*a1)*3.2E1-(a3*a3*a3)*8.0+(a3*a3*a3*a3*a3)*8.0+(a1*a1)*(a3*a3)*4.0-(a1*a1)*(a3*a3*a3)*3.2E1-(a1*a1*a1)*(a3*a3)*8.0+1.0))*4.0))*(-1.0/2.0))/((a1*a1)*4.0-a3*a3);

        '''
        intersection of h_1_3_y and h_1_2_y
        '''
        
        
        
        
        array = [abs(x1.real),
         #abs(x2.real),
         abs(x3.real),
         #abs(x4.real),
         abs(x5.real)
         #abs(x6.real)]
         ]
 
        array.sort()
        
        #x = find_closest_three(array)
        x = (array[0] + array[1] + array[2])/3
        y = abs((a3*cmath.sqrt(2*a3**3 - 2*a3 - x**2))/cmath.sqrt(a3**2 - 1))
    except ZeroDivisionError:
        pass
    
    
    return x, y.real
        


def x_axis_inter(a1, a2, a3):
    try:
        #x1 = (a1*a1+a2*a2-(a1*a1)*(a2*a2)*8.0-a1*a2*cmath.sqrt(a1*(a2*a2)*2.0+(a1*a1)*a2*2.0-(a1*a1)*4.0-(a1*a1*a1)*2.0-(a2*a2)*4.0-(a2*a2*a2)*2.0+(a1*a1*a1*a1*a1)*8.0+(a2*a2*a2*a2*a2)*8.0+(a1*a1)*(a2*a2)*1.6E1-(a1*a1)*(a2*a2*a2)*8.0-(a1*a1*a1)*(a2*a2)*8.0+1.0)*2.0)/((a1*a1)*2.0-(a2*a2)*2.0);
        x2 = (a1*a1+a2*a2-(a1*a1)*(a2*a2)*8.0+a1*a2*cmath.sqrt(a1*(a2*a2)*2.0+(a1*a1)*a2*2.0-(a1*a1)*4.0-(a1*a1*a1)*2.0-(a2*a2)*4.0-(a2*a2*a2)*2.0+(a1*a1*a1*a1*a1)*8.0+(a2*a2*a2*a2*a2)*8.0+(a1*a1)*(a2*a2)*1.6E1-(a1*a1)*(a2*a2*a2)*8.0-(a1*a1*a1)*(a2*a2)*8.0+1.0)*2.0)/((a1*a1)*2.0-(a2*a2)*2.0);
        '''
        intersection of h_1_2 and h_2_3
        '''

        x3 = (a3*a3-(a1*a1)*(a3*a3)*4.0+a1*a3*cmath.sqrt(a1*(a3*a3)*2.0+(a1*a1)*a3*3.2E1-(a1*a1)*4.0-(a1*a1*a1)*8.0-a3*a3+(a1*a1*a1*a1*a1)*3.2E1-(a3*a3*a3)*8.0+(a3*a3*a3*a3*a3)*8.0+(a1*a1)*(a3*a3)*4.0-(a1*a1)*(a3*a3*a3)*3.2E1-(a1*a1*a1)*(a3*a3)*8.0+1.0)*2.0)/((a1*a1)*8.0-(a3*a3)*2.0);
        #x4 = -(-a3*a3+(a1*a1)*(a3*a3)*4.0+a1*a3*cmath.sqrt(a1*(a3*a3)*2.0+(a1*a1)*a3*3.2E1-(a1*a1)*4.0-(a1*a1*a1)*8.0-a3*a3+(a1*a1*a1*a1*a1)*3.2E1-(a3*a3*a3)*8.0+(a3*a3*a3*a3*a3)*8.0+(a1*a1)*(a3*a3)*4.0-(a1*a1)*(a3*a3*a3)*3.2E1-(a1*a1*a1)*(a3*a3)*8.0+1.0)*2.0)/((a1*a1)*8.0-(a3*a3)*2.0);



        '''
        intersection of h_1_3 and h_1_2
        '''
        
       # x5 = (-a3*a3+(a2*a2)*(a3*a3)*4.0+a2*a3*cmath.sqrt(a2*(a3*a3)*2.0+(a2*a2)*a3*3.2E1-(a2*a2)*4.0-(a2*a2*a2)*8.0-a3*a3-(a3*a3*a3)*8.0+(a2*a2*a2*a2*a2)*3.2E1+(a3*a3*a3*a3*a3)*8.0+(a2*a2)*(a3*a3)*4.0-(a2*a2)*(a3*a3*a3)*3.2E1-(a2*a2*a2)*(a3*a3)*8.0+1.0)*2.0)/((a2*a2)*8.0-(a3*a3)*2.0);
        x6 = -(a3*a3-(a2*a2)*(a3*a3)*4.0+a2*a3*cmath.sqrt(a2*(a3*a3)*2.0+(a2*a2)*a3*3.2E1-(a2*a2)*4.0-(a2*a2*a2)*8.0-a3*a3-(a3*a3*a3)*8.0+(a2*a2*a2*a2*a2)*3.2E1+(a3*a3*a3*a3*a3)*8.0+(a2*a2)*(a3*a3)*4.0-(a2*a2)*(a3*a3*a3)*3.2E1-(a2*a2*a2)*(a3*a3)*8.0+1.0)*2.0)/((a2*a2)*8.0-(a3*a3)*2.0);

        'intersection of h_2_3 and h_1_3'
        
        #, x5.real, x6.real
        arr = [#abs(x1.real), 
               abs(x2.real),
               abs(x3.real),
               #abs(x4.real),
               #abs(x5.real),
               abs(x6.real)]
        
      
        arr.sort()
        
        #x =  find_closest_three(arr)
        x = (arr[0] + arr[1] + arr[2])/3
        y = -(cmath.sqrt(a3**2 - 1)*cmath.sqrt(2*a3**3 - x**2))/a3
        
    except ZeroDivisionError:
         #now special case
         pass
    
    
    return x, y.real

