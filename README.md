### 📄 **README.md for WordPress Plugin Creator Script**
# 🛠️ WordPress Plugin Creator Script

A Python terminal program designed to quickly set up a **boilerplate WordPress plugin** with a structured folder layout, essential files, and sample code. This tool simplifies the initial setup phase of plugin development.

---

## 🚀 **Features**

- **Dynamic Plugin Naming:** Enter a custom plugin name; the folder and main file are named accordingly.  
- **Boilerplate Main File:** Includes WordPress plugin headers, activation, and deactivation hooks.  
- **Predefined Folder Structure:** Automatically creates:  
   - `assets/` → For CSS, JS, and media files  
   - `includes/` → For core PHP logic  
   - `templates/` → For frontend templates  
- **Sample Files Included:**  
   - `assets/style.css`  
   - `assets/script.js`  
   - `includes/class-main.php`  
   - `templates/template-main.php`  
- **Error Handling:** Ensures smooth creation and validation throughout the process.  

---

## 📦 **Folder Structure**

After running the script, the folder structure will look like this:

```
your-plugin-name/
├── your-plugin-name.php  # Main plugin file
├── assets/
│   ├── style.css         # Sample CSS file
│   ├── script.js         # Sample JS file
├── includes/
│   ├── class-main.php    # Core PHP logic
├── templates/
│   ├── template-main.php # Frontend template
```

---

## 🛠️ **Installation**

1. **Clone or Download the Script:**
   ```bash
   git clone https://github.com/your-repo/wordpress-plugin-creator.git
   cd wordpress-plugin-creator
   ```

2. **Run the Script:**
   ```bash
   python create_wp_plugin.py
   ```

3. **Follow the Prompt:**
   - Enter the desired plugin name.

---

## ✅ **Example Usage**

**Input:**  
```
Enter the name of your WordPress plugin: My Awesome Plugin
```

**Output:**  
```
✅ Plugin 'My Awesome Plugin' created successfully!
📂 Location: /path/to/My-Awesome-Plugin
📄 Main File: My-Awesome-Plugin.php
📁 Subfolders and Files created:
   - assets/style.css
   - assets/script.js
   - includes/class-main.php
   - templates/template-main.php
```

---

## ⚙️ **Customization**

- Edit the `style.css`, `script.js`, `class-main.php`, and `template-main.php` files to fit your plugin's needs.  
- Add more subfolders or files if necessary.

---

## 🐍 **Requirements**

- Python 3.x  
- Basic knowledge of WordPress plugin development.  

---

## 🤝 **Contributing**

Contributions are welcome!  
- Fork the repository.  
- Create a new branch (`git checkout -b feature-branch`).  
- Submit a pull request.  

---

## 📄 **License**

This project is licensed under the **MIT License**.

---

## 📧 **Contact**

For questions or feedback, feel free to reach out:  
**[Your Name]**  
**[Your Email Address]**  
**[Your Website]**

---

**Happy Coding! 🚀✨**

