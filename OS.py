import os
def shutdown():
    """Shuts down the computer,"""
    #os.system("shutdown/s/t 1")
    print("System will shut down.")

if __name__=="__main__":
    confirm=input("Do you really want to shut down your computer? (yes/no): ")
    if confirm.lower()=="yes":
        shutdown()
    else:
        print("Shutdown cancelled.")