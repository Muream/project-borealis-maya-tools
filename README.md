This is the Maya Tools for Project Borealis

# Prerequisites

Before you get started with the tools, You need a few things.

* I recommend you set up the unreal project first because it covers everything you need to get the tools. Here's the wiki: https://projectborealisgitlab.site/project-borealis/main/pb/wikis/home
* You will need to have the `raw-assets` locally on your drive. It's located at the root of our google drive. If you don't have access to that, ask a project administrator to give you access.

# Setup

* Navigate to the folder you want the tools to be (next to the `pb` directory is a good idea but not necessary).
* Right click in an empty space > open git bash here
* Type `git clone https://github.com/Muream/project-borealis-maya-tools.git` and press enter.
* There should now be a `tools` directory. Inside there you will find a file named `StartMayaUser.bat` Use this one to open Maya when you want to work on some Project Borealis Assets.
  Update the tools automatically, and then open Maya with PB's tools loaded.
* The first time you open Maya this way, you will be asked to locate the `raw-asset` directory. 
  This is really important, without this Maya will not be able to resolve the textures, references and any other path.
  We need this to be able to share files without having to constantly re-link all the files.
  You can always change this later via the Project Borealis menu in general > Set Assets Directory.
  
