# openCV
import cv2
import numpy as np

# Load the existing image
image_path = 'pure_white_image.png'
existing_image = cv2.imread(image_path)

# Check if the image is loaded successfully
if existing_image is None:
    print(f"Error: Unable to load the image from {image_path}")
else:
    # Define vertices for the hexagon
    hexagon_vertices = np.array([[50, 50], [150, 50], [200, 150], [150, 250], [50, 250], [0, 150]], np.int32)

    # Reshape the vertices to a 3x1 array of vertices
    hexagon_vertices = hexagon_vertices.reshape((-1, 1, 2))

    # Draw the hexagon on the existing image
    cv2.polylines(existing_image, [hexagon_vertices], isClosed=True, color=(0, 0, 0), thickness=6)
    cv2.fillPoly(existing_image, [hexagon_vertices], color=(0, 128, 0))

    # Define vertices for the pentagon
    pentagon_vertices = np.array([[190,500], [190, 400], [290, 300], [390, 400], [390, 500]], np.int32)
    cv2.fillPoly(existing_image, [pentagon_vertices], color=(128, 0, 128))

    # Reshape the vertices to a 3x1 array of vertices
    pentagon_vertices = pentagon_vertices.reshape((-1, 1, 2))

    # Draw the pentagon on the existing image
    cv2.polylines(existing_image, [pentagon_vertices], isClosed=True, color=(0, 0, 0), thickness=2)

    # Define new vertices for the triangle
    new_triangle_vertices = np.array([[450, 150], [550, 150], [500, 50]], np.int32)

    # Reshape the vertices to a 3x1 array of vertices
    new_triangle_vertices = new_triangle_vertices.reshape((-1, 1, 2))

    # Draw the new triangle on the existing image (replacing the old triangle)
    cv2.polylines(existing_image, [new_triangle_vertices], isClosed=True, color=(0, 0, 0), thickness=6)
    cv2.fillPoly(existing_image, [new_triangle_vertices], color=(0, 0, 255))

    # Start coordinate for the rectangle, here (400, 200)
    start_point_rect = (400, 200)
    start_point_rects = (400, 200)

    # Ending coordinate for the rectangle, here (500, 300)
    end_point_rect = (500, 300)
    end_point_rects = (500, 300)

    # Using cv2.rectangle() method
    # Draw a rectangle with blue line borders of thickness of 2 px
    existing_image = cv2.rectangle(existing_image, start_point_rect, end_point_rect, (0, 0, 0), thickness=6)
    existing_image = cv2.rectangle(existing_image, start_point_rects, end_point_rects, (255, 0, 0), thickness=-1)

    # Center coordinates for the circle, here (700, 250)
    center_coordinates_circle = (700, 250)

    # Radius of circle
    radius_circle = 50

    # Using cv2.circle() method
    # Draw a circle with black line borders of thickness of 2 px
    existing_image = cv2.circle(existing_image, center_coordinates_circle, radius_circle, (0, 0, 0), 6)
    existing_image = cv2.circle(existing_image, center_coordinates_circle, radius_circle, (255, 255, 0), -1)

    # Font settings for text
    font = cv2.FONT_HERSHEY_SIMPLEX 
    org = (400, 500)  # Text starting position
    fontScale = 1
    color = (255, 0, 0)  # Blue color
    thickness = 2

    # Using cv2.putText() method 
    image = cv2.putText(existing_image, 'sumit kumar', org, font, fontScale, color, thickness, cv2.LINE_AA)

    # Display the image with the drawn shapes
    cv2.imshow('Image with Shapes', existing_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Extracting the height and width of an image
    h, w = existing_image.shape[:2]
    # Displaying the height and width
    print("Height = {},  Width = {}".format(h, w))
    print("start")

    This code uses OpenCV to draw various shapes (hexagon, pentagon, triangle, rectangle, and circle) on an existing image. It also adds text to the image. Here's a breakdown of the sections:

Image Loading:

Loads an existing image ('pure_white_image.png') using OpenCV.
Hexagon:

Defines vertices for a hexagon and draws it on the image using cv2.polylines and fills it with color using cv2.fillPoly.
Pentagon:

Defines vertices for a pentagon and draws it on the image using cv2.polylines and fills it with color using cv2.fillPoly.
Upside-Down Triangle:

Defines new vertices for an upside-down triangle and draws it on the image using cv2.polylines and fills it with color using cv2.fillPoly.
Rectangle:

Defines start and end coordinates for a rectangle and draws it on the image using cv2.rectangle. It also draws a filled rectangle with a different color.
Circle:

Defines center coordinates and radius for a circle and draws it on the image using cv2.circle. It also draws a filled circle with a different color.
Text:

Adds text to the image using cv2.putText.
Display and Output:

Displays the final image with the drawn shapes and prints the height and width of the image.
This code is a good example to showcase the drawing capabilities of OpenCV. Make sure to include the necessary image file ('pure_white_image.png') in your GitHub repository if you plan to share this code.
