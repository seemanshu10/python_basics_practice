## 🎯 **AP. Practice QPixmap**

### Task Objective

By completing this task, you will:
* Use `QPixmap` to load and display an image from file
* Check if the image was loaded successfully using `isNull()`
* Scale and crop the image using `scaled()` and `copy()`
* Display the image inside a `QLabel`
* Use `QFileDialog` to select the image path
* Save the cropped image using `save()`
* Style the `QLabel` to make it look clean in the UI
* Use `QPushButton` and signal connections to control the flow

### Instructions

You will build an image viewer that allows the user to select an image and view it in the UI.
1. Create a `QWidget` window with a `QVBoxLayout`.
2. Add:
   * One `QPushButton` labeled **"Load Image"**
   * One `QLabel` to display the image
   * One `QPushButton` labeled **"Save Cropped Image"**
3. When the **"Load Image"** button is clicked:
   * Open a `QFileDialog` using `QFileDialog(self)`
   * Use `fileSelected` signal to pass the selected file path to a method
   * In that method:
     * Create a `QPixmap` object
     * Use `.load(path)` to load the image
     * Use `.isNull()` to check if loading succeeded
     * Use `.scaled(300, 300)` to resize the image
     * Use `.copy(x, y, w, h)` to crop a part of it (e.g., top-left 150x150)
     * Set the final pixmap to the QLabel using `.setPixmap()`
4. When the **"Save Cropped Image"** button is clicked:
   * Save the cropped image using `.save("cropped_output.jpg")`
5. Style the `QLabel` to have a black background and a light border:
   ```python
   label.setStyleSheet("QLabel { background-color: black; border: 1px solid #ccc; }")
   ```

### Sample Output
> Checkout output.gif for GUI preview

**Console Output Example:**
```
Image loaded: True
Image saved as cropped_output.jpg
```