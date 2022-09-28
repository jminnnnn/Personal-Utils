import os
import pickle

#read a pickle and divide its list into n different files

class divide_pkls():
    def __init__(self):
        self.merge_list = []
        self.output_folder_name = 'Pickle_division_result/'
        
    def set_output_folder(self):
        if not os.path.exists():
            os.makedirs(self.output_folder_name)    
        else:
            print('path already exists')
    
    def merge_several_pkls_and_divide(self, path_list, n):
        self.set_output_folder()
        for path in path_list:
            with open(path, 'rb') as f:
                pkl = pickle.load(f)
            
            for i in pkl:
                self.merge_list.append(i)
        
        self.divide_pkl(self.merge_list, n)
        
    def read_and_divide_pkls(self, path, n):
        self.set_output_folder()
        with open(path, 'rb') as f:
            base_pkl = pickle.load(f)
            
        self.divide_pkl(base_pkl, n)
    
    def divide_pkl(self, pkl_list, n):
        pkl_len = len(pkl_list)
        
        if pkl_len % n  == 0:
            num_files = pkl_len / n
        elif pkl_len % n != 0:
            num_files = (pkl_len / n) + 1
        else:
            print('division error')

        count = 0
        for i in range(0, pkl_len, num_files):
            file_list = pkl_list[i : i+num_files]
         
        with open(self.output_folder_name+ str(count)+'.pkl', 'wb') as f:
            pass

        with open(self.output_folder_name + str(count)+'.pkl', 'wb') as f:
            pickle.dump(file_list, f)   
        
    
    


# final_list= read_basic_pkls_from_hy()
# divide_pkls(final_list)

a =200
b = 20
# print(int(a/b))/
c = a/b
print(c)
if a%b == 0:
    print('d')
elif a%b != 0: 
    print('dd')