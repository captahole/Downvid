# Downvid
A simple, user-friendly tool for downloading videos from the web.

Table of Contents
Getting Started
Usage
Features
Getting Started

To get started with DownVid, simply clone this repository and run the DownVid.py script using Python.

Prerequisites
Python 3.6 or later
yt-dlp library (installable via pip: pip install yt-dlp)
Usage
Run the DownVid.py script.
Enter one or more video URLs when prompted.
Choose a download location and format (if available).
Click "Download" to start the process.
Command-Line Options
-h: Display help message
-v: Increase verbosity level
--download-dir: Specify custom download directory
--video-format: Specify custom video format

Features
Supports YouTube, Vimeo, and other popular video sharing sites
Allows users to choose between various video formats and quality settings
Includes built-in error handling for smoother downloads
Automated Uploads (Dropbox Integration)
If you have a Dropbox account, you can use the DownVid app to automatically upload your downloaded videos to Dropbox. To enable this feature:

Create a new file called dropbox_api_key.txt in the same directory as the script.
Enter your Dropbox API credentials into the file.
Troubleshooting
If you encounter any issues while using DownVid, please refer to our FAQ for troubleshooting tips and solutions.

Known Issues
yt-dlp library may require additional dependencies (e.g., ffmpeg) on some systems
Some video formats or quality settings may not be supported by certain platforms
Contributing
We welcome contributions from developers interested in improving DownVid. Please submit pull requests or create issues to report any bugs or feature requests.

License
DownVid is licensed under the MIT License. See LICENSE.md for details.
