def task():
    print('Program started')
    a=int(input('Enter a: '))
    b=int(input('Enter b: '))
    nos=[1,2,3]
    try:
        result=a/b
        print('Processing done')
        print('Result:',result)
        print('nos[2]=',nos[2])
    except ZeroDivisionError as e:
        print('Exception occured:',e.__class__)
    except IndexError as e:
        print('Error:List index out of bounds')
    finally:
        print('Finally executed')
        print('End of Program')
task()