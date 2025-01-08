import os
import re

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
function {plugin_slug_php}_activate() {{
    // Activation logic here
}}
register_activation_hook(__FILE__, '{plugin_slug_php}_activate');

// Deactivation Hook
function {plugin_slug_php}_deactivate() {{
    // Deactivation logic here
}}
register_deactivation_hook(__FILE__, '{plugin_slug_php}_deactivate');

// Main Plugin Code Starts Here
function {plugin_slug_php}_init() {{
    // Initialization code here
}}
add_action('init', '{plugin_slug_php}_init');
'''

# Sample file templates
SAMPLE_FILES = {
    'assets/style.css': '''/* Main stylesheet for {plugin_name} plugin */''',
    'assets/script.js': '''// Main JavaScript file for {plugin_name} plugin''',
    'includes/class-main.php': '''<?php
// Main class for {plugin_name} plugin

class {plugin_slug_php}_Main {{
    public function __construct() {{
        // Initialization code here
    }}
}}''',
    'templates/template-main.php': '''<?php
// Main template file for {plugin_name} plugin
echo "Hello from {plugin_name} Template!";
?>'''
}

# Sanitize plugin slug for folder names
def sanitize_slug(name):
    slug = name.lower().replace(' ', '-').replace('_', '-')
    slug = re.sub(r'[^a-z0-9-]', '', slug)  # Remove invalid characters
    slug = re.sub(r'-+', '-', slug)  # Replace multiple hyphens with one
    if not re.match(r'^[a-z]', slug):  # Ensure it starts with a letter
        raise ValueError("Slug must start with a letter.")
    return slug

# Sanitize plugin slug for PHP code
def sanitize_php_slug(slug):
    return slug.replace('-', '_')

# Create folders and files
def create_folders_and_files(plugin_folder, plugin_name, plugin_slug, plugin_slug_php):
    subfolders = ['assets', 'includes', 'templates']
    for folder in subfolders:
        folder_path = os.path.join(plugin_folder, folder)
        os.makedirs(folder_path, exist_ok=True)
    
    # Create sample files
    for file_path, content in SAMPLE_FILES.items():
        full_path = os.path.join(plugin_folder, file_path)
        with open(full_path, 'w') as file:
            file.write(content.format(
                plugin_name=plugin_name, 
                plugin_slug=plugin_slug, 
                plugin_slug_php=plugin_slug_php
            ))

# Create plugin
def create_plugin():
    while True:
        plugin_name = input("Enter the name of your WordPress plugin: ").strip()
        if not plugin_name:
            print("❌ Plugin name cannot be empty!")
            continue
        
        try:
            plugin_slug = sanitize_slug(plugin_name)
            plugin_slug_php = sanitize_php_slug(plugin_slug)
            break
        except ValueError as e:
            print(f"❌ {e} Please try again.")
    
    # Get save directory
    save_directory = input("Enter the directory to save your plugin (leave blank for current directory): ").strip()
    if not save_directory:
        save_directory = os.getcwd()
    
    if not os.path.exists(save_directory):
        create_dir = input(f"Directory '{save_directory}' does not exist. Create it? (y/n): ").strip().lower()
        if create_dir == 'y':
            os.makedirs(save_directory)
        else:
            print("❌ Operation cancelled. Directory does not exist.")
            return
    
    plugin_folder = os.path.join(save_directory, plugin_slug)
    
    try:
        # Create main plugin folder
        os.makedirs(plugin_folder, exist_ok=True)
        
        # Create subfolders and sample files
        create_folders_and_files(plugin_folder, plugin_name, plugin_slug, plugin_slug_php)
        
        # Create main plugin file
        main_file = os.path.join(plugin_folder, f"{plugin_slug}.php")
        with open(main_file, 'w') as file:
            file.write(PLUGIN_TEMPLATE.format(
                plugin_name=plugin_name, 
                plugin_slug=plugin_slug, 
                plugin_slug_php=plugin_slug_php
            ))
        
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
