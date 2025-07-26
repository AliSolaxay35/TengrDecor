def run_on_zoj(f):
    def wrapper():
        import datetime
        now = datetime.datetime.now()
        minute = now.minute
        if minute % 2 == 0:
            f()
        else:
            print('hisss')
            
    return wrapper
 
@run_on_zoj        
def say_hello():
    print("salam man injam")

@run_on_zoj      
def say_bye():
    print('bye bye')
    
say_hello()
say_bye()