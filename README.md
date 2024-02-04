# Image Generator

This simple Python script generates random RGB images and saves them to a specified directory. The generated images are continuously overwritten, and a copy of the previous image is stored in a separate folder after a certain count.

## Requirements

- Python 3.x
- NumPy
- Pillow (PIL)

## Usage

1. Ensure you have Python installed on your system.
2. Install required dependencies:

```bash
pip install numpy pillow
```

3. Run the script:

```bash
python image_generator.py
```

## Configuration

You can modify the following parameters in the script according to your preferences:

- `size_h` and `size_w`: Set the height and width of the generated images, respectively.
- `img_max`: Define the maximum number of images to keep in the 'old' folder.
- `time.sleep(0.5)`: Adjust the sleep time between image generations (in seconds).

## Output

The script generates random RGB images and continuously saves them to the "imgs/output_image.jpg" file. Additionally, a copy of the previous image is stored in the "imgs/old" folder after reaching the specified image count.

**Note:** Make sure the "imgs" and "imgs/old" directories exist in the same location as the script before running it.
