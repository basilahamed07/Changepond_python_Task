def set_datatype():
    set_data_same = {1,2,3,4,5,6,7,8,9,10}
    set_data_mixed = {1,2,3,4,'basil','ahamed',3j}
    print(set_data_same)
    print(set_data_mixed)
    set_data_mixed = {1,2,3,4,'basil','basil',3j}
    print(set_data_mixed)
    set_data_mixed = {1,True,False,0}
          
# set_datatype()

def _task_1():
    set_data_mix = {'basil',25,124,True,124}
    for trash in set_data_mix:
        print(trash)
# _task_1()

#methods

def _set_methods():
    #add method
    set_data_mix = {'basil',25,124,True,124}
    
    #add method will add the element only one element
    
    def _add_method():
        set_data_mix
        set_data_mix.add('basil ahamed')
        print(set_data_mix)
        
     #update method will add the element more then onece in a time
    
    def _update_method():
        set_data_mix
        set_data_mix.update({'canada',1,2})
        print(set_data_mix)
        
        
     #update method will add the element more then onece in a time
    
    def discord_method():
        set_data_mix
        set_data_mix.discard({'canada'})
        print(set_data_mix)
    
     #update method will add the element more then onece in a time
    
    def remove_method():
        set_data_mix
        set_data_mix.remove(1)
        print(set_data_mix)
    
        
        
    _add_method()
    _update_method()
    discord_method()
    remove_method()
# _set_methods() 



#advance method

def _advance_method():
    company = {'spacex','google','facebook','apple'}
    add_company = {'facebook','apple','changepond','vdart'}
    print(company)
    print(add_company)
    
    #it will return the both the sets and different values
    def _union_method():
        union_method = company.union(add_company)
        print(union_method)
        #by using the oprtator
        print()
        union_method = company | add_company
        print(union_method)
    _union_method()
    
    
    #intersection will return the common element
    def intersection_method():
        intersection_method = company.intersection(add_company)
        print(intersection_method)
        print()
        intersection_method = company & add_company
        print(intersection_method)
        print()
    intersection_method()
    
    #different method will return the which are the element are not common
    def different_method():
        different_method = company.difference(add_company)
        print()
        print(different_method)
    different_method()
    
    #it willl return the uncommon element in the two set
    def sementric():
        sementric = company.symmetric_difference(add_company)
        print(sementric)
    sementric()
_advance_method()