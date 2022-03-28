'''

ordered_dict buildt for finding index and managing keys

in initialization part ,raw_total collect all of keys and values of parameters
then

the list of all keys ( sorted_keys ) made through raw_total
with sorted_keys we create list with tuples

== [(key1,value1),(key2,value2)]

this way help to create simply


//iteration part
is consist of sortedkeys 
if you want to use it with values you should use it with self.raw_total[key]
//

'''



class ordered_dict:
    """in fact ordered_dict is a list consist of tuples in order == [(key1,value1),(key2,value2)]"""
    
    
    def __init__(self,dictionary={},**kwargs):
        #able to get info fastly, scen`ffffarios is written below

       
                               
        
        self.kwargs = dict(kwargs)
        self.raw_total = {}
        self.sorted_keys = []
        self.sorted_dict = []
        
        if len(dictionary) ==  0 : 
            if len(kwargs)!= 0:

                self.append_dict(self.kwargs)

        elif len(dictionary)>0 :
            if len(kwargs) == 0:
                self.append_dict(dictionary)
            
            else:
         
                
                self.raw_total =dict(dictionary)
                self.append_dict(self.kwargs)
                

    '''item methods'''
    def __getitem__(self,i):

            return self.raw_total[i]
    def index(self,position=0):
        if type(position) != int:
            raise ValueError
        if position >len(self.sorted_keys)+1 :
            raise ValueError
        return self.sorted_dict[position]
                        
    '''pair methods'''          
    
    def __setitem__(self, key, value):
        
        if key in self.raw_total:
            self.raw_total[key] = value
            self.sorted_dict.pop(self.sorted_keys.index(key))
            self.sorted_dict.insert(self.sorted_keys.index(key),(key,value) )
            """there is already in keys"""
        else:
            self.raw_total[key] = value
            self.sorted_keys.append(key) 
            self.sorted_keys.sort()
            self.sorted_dict.insert(self.sorted_keys.index(key), (key,value) )
            
    def __delitem__(self, key):
        
        """self.sorted_keys.index(key)= position of key"""
        del self.raw_total[key]
        
        del  self.sorted_keys[key]
        
        index = self.sorted_keys.index(key)
        self.sorted_dict.pop(index)
        self.sorted_dict = self.sorted_dict[:index]
        
        for i in self.sorted_keys[index:]:
            self.sorted_dict.append((i,self.raw_total[i]))

    def index(self,_position):
        if type(_position) != int:
            raise ValueError
        if _position>len(self.sorted_keys)+1 :
            raise ValueError
        return self.sorted_keys[_position]
                        

    ''' dictionary methods '''  
    def append_dict(self,a_dictionary={}):
        '''this method in use in init. part'''
        if type(a_dictionary) == dict :
            
            self.raw_total.update(a_dictionary)
            self.sorted_keys = sorted(self.raw_total)
            
            self.sorted_dict.clear()#in order to not see duplication
            for i in self.sorted_keys:
                self.sorted_dict.append((i  , self.raw_total[i]) )
        else:
            raise ValueError('input is supposed to be a dictionary')
  
  
  
    
    
    '''key methods''' 
    def whole_keys(self):
        return self.sorted_keys    

    def show_number_of_keys(self):
        return len(self.sorted_keys)



    '''iterable'''
    def __iter__(self):

        self.index = 0
        return self
        
        
    def __next__(self):
        '''iterable part is keys'''
        if self.index==len(self.sorted_keys) :
            raise StopIteration
        result = self.sorted_keys[self.index]
        self.index += 1 
        
        return result
    
