import os 

def create_file(filename):
    try:
        with open(filename, 'x') as file: #using with bcuz it will allow us to not write close again and again
            print(f"File '{filename}' created successfully.") 
    except FileExistsError: #error handling if any file is already exists of same name
            print(f"File '{filename}' already exist.")
    except Exception as e:
            print(f"An error occurred") #if any other error will occur 

def view_file():
    files=os.listdir() 
    if not files:
        print("No such files exist")
    else:
        print("The files in directory are") 
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"file named '{filename}' has been deleted")
    except FileNotFoundError:
        print("The file does not exist")
    except Exception as e:
        print("An error occured")

def read_file(filename):
    try:
        with open(filename,'r') as f:
            content=f.read()
            print(f"The content inside '{filename}' is:\n'{content}'")
    except FileNotFoundError:
        print("The file does not exist ")
    except Exception as e:
        print("An error occured")

def edit_file(filename):
    try:
        with open(filename,'a') as f:
            content=input("Enter the content you want to add: ")
            f.write(content+'\n')
            print(f"Content added to the file '{filename}' sucessfully")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist")
    except Exception as e:
        print("An error occured")

def main_fxn(): #fix input out 
    while True:
        print("WELCOME TO THE FILE MANAGMENT APP")
        print("1:CREATE FILE")
        print("2:VIEW FILE")
        print("3:DELETE FILE")
        print("4:READ FILE")
        print("5:EDIT FILE")
        print("6:EXIT")

        choice=input("ENTER YOUR CHOICE OF OPERATION(1-6): ")
        if(choice=='1'):
            filename=input("ENTER THE NAME OF YOUR FILE: ")
            create_file(filename)
        elif(choice=='2'):
            view_file()
        elif(choice=='3'):
            filename=input("ENTER THE NAME OF YOUR FILE: ")
            delete_file(filename)
        elif(choice=='4'):
            filename=input("ENTER THE NAME OF YOUR FILE: ")
            read_file(filename)
        elif(choice=='5'):
            filename=input("ENTER THE NAME OF YOUR FILE: ")
            edit_file(filename)
        elif(choice=='6'):
            print("Closing the program...")
            break
        else:
            print("Invalid input")

if __name__=="__main__":
    main_fxn()




#upgrade it to excel conversion something




