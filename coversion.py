## Use the following conversion to convert a multispectral image to a NDVI image    

for image in dataset:
        imageRed = image[0][:,:,redChannel]
        imageNIR = image[0][:,:,nirChannel]

        NDVI = (imageNIR - imageRed)/(imageNIR + imageRed)
        scaledNDVI = np.clip(NDVI, 0, 255).astype(np.uint8)
        colormappedNDVI = cv.applyColorMap(scaledNDVI, cv.COLORMAP_JET)
        imagePlot.set_data(colormappedNDVI)

## Use the following conversion to convert a multispectral image to a CCCI image


## Use the following conversion to convert a multispectral image to a GLI (green leaf index) image

    GLI = (2Green - Red - Blue) / (2Green + Red + Blue)

## Use the following conversion to convert a multispectral image to a GNDVI image

## Use the following conversion to convert a multispectral image to a NDRE image

## Use the following conversion to convert a multispectral image to a SIPI image

## Use the following conversion to convert a multispectral image to a EXGI image

## Use the following conversion to convert a multispectral image to a VARI (Visible Atmospherically Resistant Index) image

  VARI = (Green - Red)/(Green + Red - Blue)

## Use the following conversion to convert a multispectral image to a TGI image

## Use the following conversion to convert a multispectral image to a AVRI image
