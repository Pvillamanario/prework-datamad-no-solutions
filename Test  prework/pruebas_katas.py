print ('Hello World!')def is_valid_walk(walk):
    if len(walk)!=10:
        return False  
    else:    
        if walk.count('n')==walk.count('s') and  walk.count('e')==walk.count('w'):
            return True
        
        else:
            return False

print(is_valid_walk(['s', 's', 'w', 'n', 'n', 'n', 'e', 's']))