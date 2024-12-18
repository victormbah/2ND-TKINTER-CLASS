# Vic's Tkinter GUI Program

## Overview
Vic's Tkinter GUI Program is a simple Python application built using the Tkinter library. It provides a user-friendly interface for inputting and managing text with features like message display, clearing inputs, and customizable behavior. The application showcases fundamental Tkinter components, including menus, buttons, labels, checkboxes, and event handling.

## Features

### Menubar
- **File Menu**:
  - **Close Program**: Prompts the user to confirm before exiting.
  - **Close Without Question**: Exits the application immediately without confirmation.
- **Action Menu**:
  - **Show Message**: Displays the message entered in the textbox.

### Widgets
- **Label**: Displays a title ("Your Message") for the textbox.
- **Textbox**: Allows users to input multi-line text.
- **Checkbox**: Toggles between printing the message in the console or displaying it in a popup messagebox.
- **Buttons**:
  - **Show Message**: Displays the entered message based on the checkbox state.
  - **Clear Message**: Clears all content in the textbox.

### Keyboard Shortcuts
- `Ctrl+Enter`: Triggers the "Show Message" button action.

### Exit Behavior
- A custom exit handler ensures users are prompted for confirmation before closing the application unless they select the "Close Without Question" option.

## Requirements
- Python 3.x
- Tkinter library (included with most Python installations)

## Installation
1. Download or clone this repository.
2. Save the script as `gui_program.py`.
3. Ensure Python 3.x is installed on your machine.
4. Run the script using the command:
   ```bash
   python gui_program.py
   ```

## How to Use
1. Launch the program.
2. Enter your message in the textbox.
3. Check or uncheck the "Show Messagebox" checkbox:
   - **Unchecked**: The message is printed to the console.
   - **Checked**: The message is displayed in a popup messagebox.
4. Click the **Show Message** button or press `Ctrl+Enter` to display the message.
5. Use the **Clear Message** button to clear the textbox.
6. Use the menu options to exit the program with or without confirmation.

## Code Explanation
- **Menus**: Implements a menubar with `File` and `Action` menus for program controls.
- **Textbox**: Multi-line input field for the user's message.
- **Checkbox**: Toggles between displaying the message in a popup or printing it to the console.
- **Event Handling**:
  - `show_message`: Displays the entered message based on the checkbox state.
  - `on_closing`: Handles custom behavior when the user tries to close the application.
  - `clear`: Clears the content of the textbox.
  - `shortcut`: Enables `Ctrl+Enter` as a shortcut for the "Show Message" action.

## Customization
- Change the window size by modifying the `self.root.geometry("500x300")` line in the script.
- Customize fonts or colors by adjusting widget parameters, such as `font` or `bg`.
- Add new features by extending the menubar or adding more buttons.

## License
This project is open-source and available under the MIT License.

---

