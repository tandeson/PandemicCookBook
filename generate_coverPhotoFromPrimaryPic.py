#!/usr/bin/env python
#*****************************************************************************
#
"""
    Build up a cook book by pulling together all the pieces
"""
#
#*****************************************************************************
#   Use of the software source code and warranty disclaimers are
#   identified in the Software Agreement associated herewith.
#*****************************************************************************

#*  Imports ******************************************************************
import os
import time

import sys
from PIL import Image
import math

from pathlib import Path
import pickle

#*  Constants ****************************************************************
C_DATETIME_STR_FMT_RULES = "%I:%M%p on %B %d, %Y" 

# Exit codes - "no error" must be 0
EXIT_OK, EXIT_ERR, EXIT_CTRL_C = range(3)

#=============================================================================
def main(argv=None):
    """
    Parse arguments, report start & stop time, and run the test.
    """
    
    # Handle command line arguments
    if argv is None:
        argv = sys.argv

    args = parseCommandLine( argv[1:] )
    
    #Debug for now - may make an option or remove later.
    args.cache_primary_photos = True
    
    try:
        print( "Start date & time is " + time.strftime("%c") )

        # Do the work
        mainControl(args)

    except KeyboardInterrupt:
        # Assume Control-C is intentional, and just exit w/o alerts
        return EXIT_CTRL_C

    print( "End date & time is " + time.strftime("%c") )
    return EXIT_OK


#=============================================================================
def parseCommandLine(args = sys.argv[1:]):
    """
    Parse command-line options. Returns arguments.

    """

    ## Documentation: https://docs.python.org/2/howto/argparse.html
    import argparse

    ## Parse Input Options.
    parser = argparse.ArgumentParser(description='Front Page Builds from Primary Photos')
    
    ## -- Common Options
    parser.add_argument(
        '-i','--input_directory',
        action='store', default="recipes_for_book_input",
        help = "root directory where recipes are stored.")
        
    parser.add_argument(
        '-o','--output_directory',
        action='store', default="output",
        help = "root directory where recipes documents are generated.")
    
    parser.add_argument(
        '-v','--verbose',
        action='store_true',
        help = "Verbose progress messages. Progress messages are "
                "not displayed by default except for system error messages.")
    
    ## Parse the options
    args = parser.parse_args()

    return (args)

#=============================================================================
# Gen Code - 
#=============================================================================
def load_and_process_images(image_paths, target_width, target_height, dpi):
    """Load images, crop them to squares, and resize to fit target dimensions."""
    processed_images = []
    num_images = len(image_paths)
    
    do_gpt_way = False
    
    if do_gpt_way:
        num_images_x = math.ceil(math.sqrt(num_images * target_width / target_height))
        num_images_y = math.ceil(num_images / num_images_x)
    
        # Calculate size for individual images
        image_size_x = int(target_width * dpi / num_images_x)
        image_size_y = int(target_height * dpi / num_images_y)
        image_size = min(image_size_x, image_size_y)
    else:
        total_dpi = ( (target_height * dpi) * (target_width * dpi) )
        per_img_dpi = int(total_dpi / num_images) + 1
        image_size_x = image_size_y = image_size = int(math.sqrt(per_img_dpi)) + 1
        
        num_images_x = int((target_width * dpi) / image_size)
        num_images_y = int((target_height * dpi) / image_size)

    for path in image_paths:
        image = Image.open(path)
        # Crop to square
        min_side = min(image.width, image.height)
        left = (image.width - min_side) / 2
        top = (image.height - min_side) / 2
        right = (image.width + min_side) / 2
        bottom = (image.height + min_side) / 2
        image = image.crop((left, top, right, bottom))
        # Resize
        image = image.resize((image_size, image_size), Image.Resampling.LANCZOS)
        processed_images.append(image)

    return processed_images, (image_size_x, image_size_y), (num_images_x, num_images_y)

def create_collage(image_paths, output_path, collage_width_inch, collage_height_inch, dpi=300):
    """Create a rectangular collage from a list of image paths."""
    images, image_size, grid_size = load_and_process_images(image_paths, collage_width_inch, collage_height_inch, dpi)

    collage_width_px = grid_size[0] * image_size[0]
    collage_height_px = grid_size[1] * image_size[1]

    collage = Image.new('RGB', (collage_width_px, collage_height_px))

    x, y = 0, 0
    for image in images:
        collage.paste(image, (x, y))
        x += image_size[0]
        if x >= collage_width_px:
            x = 0
            y += image_size[1]

    collage.save(output_path)
#=============================================================================
#=============================================================================


#=============================================================================
def mainControl(args):
    """
    Main routine for the Cookbook Builder.

    Find all the recipe files, build a cookbook!
    """
    
    outAbsPath = Path( os.path.join( '.', args.output_directory ) )
    
    #Get Pickle Data
    AbsPathPklIn = Path( os.path.join(outAbsPath, 'img', 'Pandemic_Cookbook_primaryPhots.pkl') )
    with open(AbsPathPklIn, 'rb') as handle:
        dictPrimaryPhotos = pickle.load(handle)
    

    
    image_paths = []
    for i in dictPrimaryPhotos:
        image_paths.append(i['path'])
        
    create_collage(image_paths, 'output_collage.jpg', 8, 10)  # Width and height in inches
    
    return True

#*  Main Code Path ***********************************************************

if __name__ == "__main__":
    # Exit code is main() return value
    # (see http://www.artima.com/weblogs/viewpost.jsp?thread=4829)
    sys.exit(main())


#*****************************************************************************
#*****************************************************************************
