import numpy as np
import pandas
from equations import y_axis_inter, x_axis_inter


class hyperbola(object):
    
    def __str__(self):
        self.f_and_shift()
        if self.type == 'Y_axis':
            return str('(y +' + str(self.shift) + '^2)/a' + ' - x^2/('+str(self.f**2) + ' - a^2) = 2*a)')
        else:
            return str('(x +' + str(self.shift) + '^2)/a' + ' - y^2/('+str(self.f**2) + ' - a^2) = 2*a)')
    
    def __init__(self, mic1, mic2, source):
        self.mic1 = mic1
        self.mic2 = mic2
        self.src = source
        self.a = abs(self.__dist(self.mic1, self.src) - self.__dist(self.mic2, self.src))/2
        self.settype()
        source = np.abs(source)
        self.f_and_shift()
        
    def __dist(self, a,b):
        sum_square = 0
        for ind in range(0, len(a)):
            sum_square += abs((a[ind] - b[ind])**2)
            
        return (sum_square)**(1/2)
    


    
    def settype(self):
        if self.mic1[0] == 0 and self.mic2[0] == 0:
            self.type = 'Y_axis'
            return 'Y_axis'
        else:
            self.type = 'X_axis'
        
    def f_and_shift(self):
        if self.type == 'Y_axis':
            self.f = abs((self.mic1[1] - self.mic2[1])/2)
            self.shift = (self.mic1[1] + self.mic2[1])/2
            
        else:
            self.f = (self.mic1[0] - self.mic2[0])/2
            self.shift = (self.mic1[0] + self.mic2[0])/2
        
    def intersect(object, instance, instance2, error = False):
        #This is the key functon
        #return x_axis(object.a, instance.a)
        if object.type == 'Y_axis' and instance.type == 'Y_axis':
            pseudo_cord_y_axis = y_axis_inter(object.a, instance.a , instance2.a)
            return pseudo_cord_y_axis
        elif object.type == 'X_axis' and instance.type == 'X_axis':
            if error:
                pseudo_cord_x_axis = x_axis_inter(object.a, instance.a + 0.001*instance.a, instance2.a)
                return pseudo_cord_x_axis
            else:
                pseudo_cord_x_axis = x_axis_inter(object.a, instance.a, instance2.a)
                return pseudo_cord_x_axis
        else:
            return 'CANNOT INTERSECT Y AND X AXIS HYPERBOLAS'
        
       

    
def addtoexcel(test_sources, predicted, error_array, sheetname = 'Test vs Predictions'):
    
    X_test = []
    Y_test = []
    Z_test = []
    for array in test_sources:
        X_test.append(array[0])
        Y_test.append(array[1])
        Z_test.append(array[2])
        
        
        
    X_pred = []
    Y_pred = []
    Z_pred = []    
    for array in predicted:
        X_pred.append(array[0])
        Y_pred.append(array[1])
        Z_pred.append(array[2])
        
    empty_list = [' ']*len(X_test)
    
    dataframe = pandas.DataFrame({'X Test': X_test,
                                  'Y Test': Y_test,
                                  'Z Test': Z_test,
                                  ' ': empty_list,
                                  'X Pred': X_pred,
                                  'Y Pred': Y_pred,
                                  'Z Pred': Z_pred,
                                  ' ': empty_list,
                                  'Avg % Error': error_array})
    
    
    writer_obj = pandas.ExcelWriter(sheetname+'.xlsx', engine='xlsxwriter')
    
    dataframe.to_excel(writer_obj, sheet_name = sheetname)
    writer_obj.save()
    writer_obj.close()


#to avoid priting too much digits


mic1y = (0, -1, 0)
mic2y = (0, 0, 0)
mic3y = (0, 1, 0)
mic1x = (-1, 0, 0)
mic2x = (0, 0, 0)
mic3x = (1, 0, 0)


test_sources = (
               
               np.array([10,150,20]),
               100*np.random.rand(3),
               100*np.random.rand(3),
               100*np.random.rand(3),
               100*np.random.rand(3),
               100*np.random.rand(3),
               100*np.random.rand(3),
               100*np.random.rand(3),
               100*np.random.rand(3),
               100*np.random.rand(3),
               100*np.random.rand(3),
               100*np.random.rand(3),
               100*np.random.rand(3),
               100*np.random.rand(3),
               100*np.random.rand(3),
               100*np.random.rand(3),
               100*np.random.rand(3),
               np.array([20,30,40])
               )

predicted = []
for source in test_sources:
    source = source; #just scaling source
    h_1_2_x = hyperbola(mic1x, mic2x, source)
    h_2_3_x = hyperbola(mic2x, mic3x, source)
    h_1_3_x = hyperbola(mic1x, mic3x, source)
    
    
    h_1_2_y = hyperbola(mic1y, mic2y, source)
    h_2_3_y = hyperbola(mic2y, mic3y, source)
    h_1_3_y = hyperbola(mic1y, mic3y, source)
    
    


    pseudo_cord_y = h_1_2_y.intersect(h_2_3_y, h_1_3_y)
    pseudo_cord_x = h_1_2_x.intersect(h_2_3_x, h_1_3_x)

   # print(pseudo_cord_x[0])
   #print(pseudo_cord_y[1])
    #print('')
     #px1 and px2 ae just componentsof pseudo x coordinates, I used them for readable code 

    px1, px2 = pseudo_cord_x
    py1, py2 = pseudo_cord_y
    dist_xpseu = np.sqrt(px1**2 + px2**2) 
    dist_ypseu = np.sqrt(py1**2 + py2**2)
    dist_squared = (dist_xpseu + dist_ypseu)/2
    dist_squared = dist_squared*dist_squared
    x = pseudo_cord_x[0]
    y = pseudo_cord_y[1]
    z = np.sqrt(abs(dist_squared - x**2 - y**2))
    
    predicted.append([x,y,z])
print('predicted ------------- test')
error_array = []
for index in range(len(predicted)):
    error = (predicted[index][0] - test_sources[index][0])*100/test_sources[index][0] + (predicted[index][1] - test_sources[index][1])*100/test_sources[index][1] + (predicted[index][2] - test_sources[index][2])*100/test_sources[index][2]
    error = error/3;
    error_array.append(abs(error))
    test_sources[index][0] = round(test_sources[index][0], 2)
    test_sources[index][1] = round(test_sources[index][1], 2)
    test_sources[index][2] = round(test_sources[index][2], 2)
    
    predicted[index][0] = round(predicted[index][0], 2)
    predicted[index][1] = round(predicted[index][1], 2)
    predicted[index][2] = round(predicted[index][2], 2)
    
    
    
    print(tuple(predicted[index]), ' --- ', tuple(test_sources[index]), 'error -', round(abs(error),5), '%');
    

addtoexcel(test_sources, predicted, error_array)




'''


error simualtion here







'''



