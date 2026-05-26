# Student Notes Pro

A simple desktop notes application built with PySide2. Student Notes Pro lets users enter student name, subject, category, and note content, then save or export it with styled text and quick actions.

Student Notes Pro is designed to help students write and organize quick study notes. The app includes a clean form layout, editable note area, toolbar shortcuts, text styling controls, and save/export capabilities.

## Features

- Enter student name, subject, and category
- Write or edit note content in a rich text field
- Change note font and text color
- Save notes and export them as a `.txt` file
- Use menu and toolbar actions for quick access
- Confirmation dialogs for new note creation and saving
- Status bar updates for live feedback

## Tech Stack

- Python 3
- PySide2 for the Qt GUI
- QtAwesome for toolbar icons
- CSS stylesheet for app styling

## How to Run

1. Open a terminal in this project folder.
2. Create and activate a virtual environment (recommended):
   - Windows PowerShell:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate
     ```
3. Install dependencies third party library:
   ```powershell
   pip install PySide2 qtawesome
   ```
4. Run the application:
   ```powershell
   python main.py
   ```

## Folder Structure

```text
student-notes-pro/
├── icons/               # toolbar and menu icons used by the app
├── main.py              # main application code
├── style.css            # stylesheet for the GUI
├── README.md            # project documentation
└── TASK.md              # task instructions and project requirements
```

## Usage

### App Overview

App layout, fields, menu and toolbar

![https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif width="20" height="10
"](assets/app-overview.gif)

### Notes Edit

Entering a note, changing font and color

![https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif width="20" height="10
"](assets/customize-note.gif)

### Export Notes

Exporting note in a .txt file and showing success message

![https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif width="20" height="10
"](assets/export-note.gif)


## What I Learned

- I gained confidence building a PySide2 desktop app with `QMainWindow`, layouts, and widgets.
- I learned how to wire signals and slots so the app responds naturally to clicks and text changes.
- I practiced using dialogs for choosing colors, fonts, and saving files, which improved the app usability.
- I also applied an external file CSS stylesheet to make the interface cleaner and more polished.
- I learned when Qt Designer is useful for fast prototypes and when writing the UI in code gives more control.
- I now understand that code-based UI is better for complex tools, while Qt Designer is great for small, quick prototypes.
- I understood when to use modeless and modal dialogs, which helps make the UI behave correctly.
- Explored Qta-browser CLI Tool to create icons for tools in UI. 


## 📌 Future Improvements
1. Add Notes History system.
2. Load already saved note in app so it is easy to edit.
3. Add bold italic , indentation and all the othher formatting tools. 


## 📜 License

> MIT License