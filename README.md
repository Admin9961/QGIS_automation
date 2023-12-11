I initially thought of this project as a plugin to integrate directly into QGIS (since the platform is open source), but since the QGIS Python interpreter has limitations that I didn't feel like dealing with, I created an independent script successfully tested using Python 3.12 (but even slightly older versions of Python should be fine) which connects to the Natural Earth site and downloads publicly accessible files contained in the site's repositories, namely: vector and raster data, at different geographical scales . This data can obviously be imported into QGIS for educational purposes, but also useful for lazy engineers who want to start working on GIS projects without having to start from scratch.

Included in this project are the original .py file (program code) that will need to be run through Python 3.12 (basic Windows doesn't have it unfortunately), and will require the requests beautifulsoup4 tqdm dependencies to run, which can be installed individually through the pip install command.

However, for convenience reasons in the folder I have included a PE compiled from the source code through Pyinstaller, compatible with any Windows 10 equipped with an AMD64 processor. This PE will allow you to get access to the app's features without having to install Python 3.12 or other dependencies, with the only flaw being that you will have to test it on VMware or VirtualBox to make sure it's clean (some very stupid people have compiled malware with Pyinstaller and forgotten to protect them with a packer: as a result, antiviruses are reporting all apps generated with Pyinstaller as "suspicious". In particular, Avast generates false positives). Technically the EP is clean, but since I'm a stranger here anyone is entitled to be suspicious.

Let's now move on to the technical part, that is, to describe in a granular way what the routine of this app does:

    Upon opening, the app will send an HTTP request with a specific User-Agent to obtain and print the website details on the screen and verify the authenticity of the source;
    A list is proposed including 4 samples to download from the site, specifying their weight, expressed in MegaBytes (MB), and the user must choose which one to download;
    Once you've chosen the sample, tqdm plays its part here, showing a progress bar for the download;
    Once the download is complete, the script locates the "Downloads" folder via the %userprofile% variable present in Windows, saves the file there, and then opens the folder with the downloaded file ready for use in front of the user. A syscall through the subprocess module is exploited for this;

Something strange happened when downloading the "Prisma Shaded Relief" sample but I solved it by having him download it with another method. Basically it appeared that the section of the site containing Prisma Shaded Relief used "more security" than the other sections, so to download it needed to emulate the behavior of a browser more faithfully, otherwise the download would fail. To do this, in addition to the "User-Agent" parameter, I had to specify "Accept", "Accept-Language", "Referef", and "Upgrade-Insecure-Requests", as well as having to redefine the download bar due of another bug. These endpoint changes caused a Traceback at line 123 because I would have to change other parameters accordingly, but luckily it was harmless, allowing me to complete the app successfully.

The purpose of this app is to detect a site that offers ready-made geospatial data samples, further optimizing the work times of analysts or teachers.

The files are offered for download separately, but I have still compressed them into a ZIP in case you want to download all the samples at once.

As you can imagine, the app only works for Windows (also from the fact that it uses the %userprofile% variable to manage the download, which can only be used on Windows) and I don't plan to release a version for Unix because it's not my main OS. In that case, however, it would be enough to launch the .py directly after installing the indicated dependencies, and redefine the method used to download and save the files.

