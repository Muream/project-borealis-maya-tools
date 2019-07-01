# Setup

* Navigate to the folder you want the tools to be (next to the `pb` directory is a good idea but not necessary).

* Right click in an empty space > open git bash here

* Type `git clone https://projectborealisgitlab.site/project-borealis/creatives/animation/tools.git` and press enter.

* There should now be a `tools` directory. Inside there you will find a file named `StartMayaUser.bat` Use this one to open Maya when you want to work on some Project Borealis Assets.
  Update the tools automatically, and then open Maya with PB's tools loaded.

* The first time you open Maya this way, you will be asked to locate the `raw-asset` directory. 
  This is really important, without this Maya will not be able to resolve the textures, references and any other path.
  We need this to be able to share files without having to constantly re-link all the files.
  You can always change this later via the Project Borealis menu in general > Set Assets Directory.

  > If you don't have the `raw-asset` directory yet, you can get it at the root of our google drive. If you don't have access to that, ask a project administrator to give you access.
  > Inside it there's a PDF explaining how we organize files.

If you run into any problem, ping me (@Muream) in the #tech-support channel on discord.