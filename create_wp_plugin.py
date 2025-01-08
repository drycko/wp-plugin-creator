import os

# Plugin template
PLUGIN_TEMPLATE = '''<?php
/*
Plugin Name: {plugin_name}
Plugin URI: https://example.com/{plugin_slug}
Description: A custom WordPress plugin.
Version: 1.0
Author: Your Name
Author URI: https://example.com
License: GPLv2 or later
Text Domain: {plugin_slug}
*/

// Activation Hook
function {plugin_slug}_activate() {
    // Activation logic here
}
register_activation_hook(__FILE__, '{plugin_slug}_activate');

// Deactivation Hook
function {plugin_slug}_deactivate() {
    // Deactivation logic here
}
register_deactivation_hook(__FILE__, '{plugin_slug}_deactivate');

// Main Plugin Code Starts Here
function {plugin_slug}_init() {
    // Initialization code here
}
add_action('init', '{plugin_slug}_init');
'''

# Sample file templates
SAMPLE_FILES = {
    'assets/style.css': '''/* Main stylesheet for {plugin_name} plugin */''',
    'assets/script.js': '''// Main JavaScript file for {plugin_name} plugin''',
    'includes/class-main.php': '''<?php
// Main class for {plugin_name} plugin

class {plugin_slug}_Main {
    public function __construct() {
        // Initialization code here
    }
}''',
    'templates/template-main.php': '''<?php
// Main template file for {plugin_name} plugin
echo "Hello from {plugin_name} Template!";
?>'''
}

# Sanitize plugin slug
def sanitize_slug(name):
    return name.lower().replace(' ', '-').replace('_', '-')

# Create folders and files
def create_folders_and_files(plugin_folder, plugin_name, plugin_slug):
    subfolders = ['assets', 'includes', 'templates']
    for folder in subfolders:
        folder_path = os.path.join(plugin_folder, folder)
        os.makedirs(folder_path, exist_ok=True)
    
    # Create sample files
    for file_path, content in SAMPLE_FILES.items():
        full_path = os.path.join(plugin_folder, file_path)
        with open(full_path, 'w') as file:
            file.write(content.format(plugin_name=plugin_name, plugin_slug=plugin_slug))

# Create plugin
def create_plugin():
    plugin_name = input("Enter the name of your WordPress plugin: ").strip()
    if not plugin_name:
        print("Plugin name cannot be empty!")
        return
    
    plugin_slug = sanitize_slug(plugin_name)
    plugin_folder = os.path.join(os.getcwd(), plugin_slug)
    
    try:
        # Create main plugin folder
        os.makedirs(plugin_folder, exist_ok=True)
        
        # Create subfolders and sample files
        create_folders_and_files(plugin_folder, plugin_name, plugin_slug)
        
        # Create main plugin file
        main_file = os.path.join(plugin_folder, f"{plugin_slug}.php")
        with open(main_file, 'w') as file:
            file.write(PLUGIN_TEMPLATE.format(plugin_name=plugin_name, plugin_slug=plugin_slug))
        
        print(f"\n✅ Plugin '{plugin_name}' created successfully!")
        print(f"📂 Location: {plugin_folder}")
        print(f"📄 Main File: {main_file}")
        print("📁 Subfolders and Files created:")
        for file_path in SAMPLE_FILES.keys():
            print(f"   - {file_path}")
    except Exception as e:
        print(f"❌ Error: {e}")

# Run the program
if __name__ == "__main__":
    create_plugin()
