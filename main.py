import sys
import os



# Initialise the new .vc folder
def init():
    vc_folder = ".vc"
    if not os.path.isdir(vc_folder): 
        os.mkdir(vc_folder);

        # Create nested folders
        with open(".vc/CONFIG", "w") as config:
            config.write("""
                file_created: RIGHT NOW
            """)

        print("Version control intialised successfully")
    else:
        print("Folder not created")

def add(): 
    pass
    # add a file to the staging area

def remove(): 
    pass

def commit(): 
    pass

# def push(): 
#     # push to remote repository
#     pass
     
def status():
    pass

def log():
    pass

if __name__ == "__main__": 
    # get command line arguments
    command = sys.argv[1]

    if command == "init":
        init()
    elif command == "add": 
        pass
    elif command == "remove": 
        pass
    elif command == "commit": 
        pass
    elif command == "status": 
        pass
    elif command == "log": 
        pass


