import cv2
import sys

def getSliceEnd(start, slice_size,width):
    slice_end = start+slice_size
    if(slice_end > width):
        slice_end = width
    return slice_end

def sliceImage(filename,  offset=0):
    img = cv2.imread(filename)
    height, width, channels = img.shape
    print('width:  ', width)
    print('height: ', height)
    print('channel:', channels)

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_image, s_image, v_image = cv2.split(hsv_img)

    v_image = (255-v_image)

    images  = []

    slices_size = 1024
    number_of_slices = int ((width-offset)/slices_size)

    if(width%slices_size>0):
        number_of_slices=number_of_slices+1

    slice_start = offset
    slice_end = getSliceEnd(slice_start,slices_size,width)

    print("Number of slices " + str(number_of_slices))

    for i in range(0,number_of_slices):
        slice_end = getSliceEnd(slice_start, slices_size, width)
        print(str(slice_start) + " " + str(slice_end))
        #temp_image = img
        #images.append(temp_image[0:height, slice_start:slice_end])
        images.append(v_image[0:height, slice_start:slice_end])
        slice_start = slice_start+slices_size

    counter = 0
    for image in images:
        cv2.imwrite(str(offset)+"_"+str(counter)+".png", image)
        counter = counter+1






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("Usage: script image.png")
        sys.exit(1)
    sliceImage(sys.argv[1])
    sliceImage(sys.argv[1],256)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
