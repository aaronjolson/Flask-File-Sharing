from .main import app

version = "1.0.0"
proc_name = "Flask_File_Sharing_API"

workers = 4

if __name__ == "__main__":
    app.run()
