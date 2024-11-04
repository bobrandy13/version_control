import sys
import datetime
import hashlib
import os

# when we do git add, we are creating a blob object, and then a relevant tree object

# Initialise the new .vc folder
class VersionControl: 
    @staticmethod
    def init():
        vc_folder = ".vc"
        objects_folder = ".vc/objects"
        if not os.path.isdir(vc_folder): 
            os.mkdir(vc_folder);
            os.mkdir(objects_folder)

                # Create nested folders
            with open(".vc/CONFIG", "w") as config:
                config.write("""
                    file_created: ${0}
                """.format(datetime.datetime.now()))

            with open(".vc/description", "w") as description:
                description.write('Unnamed repository')

            print("Version control intialised successfully")
        else:
            print("Version control already exists")

    # add a file to the staging area
    @staticmethod
    def add(file): 
        # track all changes 
        # we need to create a SHA of all the changes that have occured since the last commit
        if file is None: 
            print("Please provide a file to add")
            return

        if file == ".":
            # add all files in the directory
            pass
        else:
            file_contents = open(file, "r").read()
            hash = hashlib.shake_256(file_contents.encode()).hexdigest(20)

            directory_name = hash[:2]
            object_name = hash[2:]

            os.mkdir(".vc/objects/{0}".format(directory_name))

            with open (".vc/objects/{0}/{1}".format(directory_name, object_name), "w") as object_file:
                object_file.write(file_contents)    

            print("Added {0} to staging area".format(file))

            # Now store them in the tree object for metadata


    @staticmethod
    def remove(): 
        pass

    @staticmethod
    def commit(): 
        pass
        
    @staticmethod
    def status():
        pass

    @staticmethod
    def log(): ...

    @staticmethod
    def checkout(): ...

if __name__ == "__main__": 
    # get command line arguments
    command = sys.argv[1]

    if command == "init":
        VersionControl.init()
    elif command == "add": 
        file_name = sys.argv[2]
        VersionControl.add(file_name)
    elif command == "remove": 
        pass
    elif command == "commit": 
        pass
    elif command == "status": 
        pass
    elif command == "log": 
        pass


