import os 
from PIL import Image

os.chdir()
print(os.getcwd())
# # Load the two images
# image1 = Image.open('path_to_satisfied_plot.png')
# image2 = Image.open('path_to_dissatisfied_plot.png')

# # Get the dimensions of the images
# width1, height1 = image1.size
# width2, height2 = image2.size

# # Choose the height of the combined image (assuming the heights are the same)
# combined_height = max(height1, height2)

# # Create a new blank image with double the width
# combined_image = Image.new('RGB', (width1 + width2, combined_height), (255, 255, 255))

# # Paste the individual images onto the combined image
# combined_image.paste(image1, (0, 0))
# combined_image.paste(image2, (width1, 0))

# # Display the combined image
# combined_image.show()