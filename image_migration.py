import os
import shutil
from pathlib import Path

def move_images_to_misc():
    """
    Move all direct image files from the main folder to image/misc folder
    """
    # Define image extensions
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.webp', '.tiff', '.ico'}
    
    # Get current directory
    current_dir = Path('.')
    
    # Create destination directory if it doesn't exist
    dest_dir = Path('image/misc')
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all direct image files in the main folder
    image_files = []
    for file_path in current_dir.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in image_extensions:
            image_files.append(file_path)
    
    print(f"Found {len(image_files)} image files to move:")
    
    # Move each image file
    moved_count = 0
    for image_file in image_files:
        try:
            dest_path = dest_dir / image_file.name
            
            # Check if file already exists in destination
            if dest_path.exists():
                print(f"⚠️  Skipping {image_file.name} - already exists in destination")
                continue
            
            # Move the file
            shutil.move(str(image_file), str(dest_path))
            print(f"✅ Moved: {image_file.name} -> image/misc/{image_file.name}")
            moved_count += 1
            
        except Exception as e:
            print(f"❌ Error moving {image_file.name}: {e}")
    
    print(f"\n📊 Summary: Successfully moved {moved_count} out of {len(image_files)} image files")

if __name__ == "__main__":
    print("🚀 Starting image migration to image/misc folder...")
    move_images_to_misc()
    print("✨ Migration complete!")