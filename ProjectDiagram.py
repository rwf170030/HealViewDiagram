from diagrams import Diagram, Cluster
from diagrams.custom import Custom

with Diagram("HealView Project System Diagram", show=True):
    # From: https://tabler-icons.io/
    #Desktop = Custom("Computer Host for Program", "./my_resources/devices-pc.png")
    #Menu = Custom("Program Main Menu", "./my_resources/menu-2.png")
    #Language = Custom("Language Options", "./my_resources/language.png")
    #File3D = Custom("3D DICOM Information", "./my_resources/file-3d.png")
    #FileUltrasound = Custom("Ultrasound Permeation Over Time", "./my_resources/file-time.png")
    #Loading = Custom("Loading UI", "./my_resources/loader.png")

    # From: MRTK
    #ARHeadset = Custom("HoloLens 2", "./my_resources/mixed_reality_icon.png")
    #Script = Custom("Script", "./my_resources/script_icon.png")
    Mesh = Custom("Rendered Mesh", "./my_resources/ux_icon.png")

    # From: Unity
    #UnityBlack = Custom("Unity Program", "./my_resources/U_Logo_MadeWith_RichBlack_RGB.png")
    #UnityWhite = Custom("Unity Program", "./my_resources/U_Logo_MadeWith_RichBlack_Knockout_RGB.png")

    # From: MathWorks
    #Matlab = Custom("MATLAB Code", "./my_resources/Matlab_Logo.png")

    #!!! Order that these are initialized is the order that they show up on the render
    with Cluster("Main Menu"):
        # From: https://tabler-icons.io/
        
        Question = Custom("Guide", "./my_resources/question-mark.png")
        Folder = Custom("Folder Selection", "./my_resources/folder-plus.png")

        # From: MRTK
        Toolkit = Custom("Toolkit", "./my_resources/toolkit_icon.png")

        with Cluster("Menu After Folder Reading"):
            # From: https://tabler-icons.io/
            Info = Custom("Information Menu", "./my_resources/info-circle.png")
            Mode = Custom("Mode Selection", "./my_resources/circle-half-2.png")

            # From: MRTK
            Options = Custom("Settings", "./my_resources/settings_icon.png")

            
            


    
    Folder >> Mode >> Options >> Mesh
    
    Folder >> Info
    Mode >> Info




    

