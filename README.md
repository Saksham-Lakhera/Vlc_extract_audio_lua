# VLC Extract Audio Plugin

This application is a VLC plugin that extracts audio from a video and saves it to a specified location. It is particularly useful for audio analysis or further processing, as the extracted audio is sliced into 20-second clips by default.

---

## 📋 Features
- **Audio Extraction**: Extract audio from any video file supported by VLC.
- **Customizable Storage Location**: Set the directory where the audio files will be stored.
- **Audio Slicing**: Audio is split into 20-second clips for easier handling and processing.

---

## 🛠️ Technologies Used
- **Python**: For scripting and processing tasks.
- **Lua**: Used to develop the VLC plugin extension.
- **Batch Files (BAT)**: For automation and directory setup.

---

## 🚀 Installation and Setup
1. **Update Storage Path**:  
   Modify the location of the directory where audio files should be stored. By default, the files are stored in the `audio` folder.
   
2. **Copy Plugin to VLC**:
   - Copy the `smarttitle.lua` file to the following directory:
     ```
     <VLC Installation Directory>/lua/extensions
     ```
   - If the `extensions` folder does not exist, create it manually.

3. **Restart VLC**:  
   Relaunch VLC to load the new plugin.

---

## 🎯 How to Use
1. Start VLC and open the video from which you want to extract audio.
2. Activate the plugin via VLC's **Extensions** menu.
3. The audio will be automatically extracted and stored in the specified directory as 20-second clips.

---

## 📂 Project Details
- **Objective**: Provide a starting point for creating VLC plugins, as detailed documentation is scarce.
- **Use Case**: Automating audio extraction and slicing for further processing tasks.
- **Learning Outcome**: Hands-on experience with VLC plugin development using Lua, Python, and Batch scripting.

---

## 🔧 Future Enhancements
- Add support for dynamic clip durations.
- Enable user-friendly configuration through a GUI.
- Extend compatibility with more video formats and advanced audio processing.

---

## 📧 Contact
Have questions or want to contribute?  
**linkedin**: [https://www.linkedin.com/in/sakshamlakhera/]  
