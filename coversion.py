## Use the following conversion to convert a multispectral image to a NDVI image    

for image in dataset:
        imageRed = image[0][:,:,redChannel]
        imageNIR = image[0][:,:,nirChannel]

        NDVI = (imageNIR - imageRed)/(imageNIR + imageRed)
        scaledNDVI = np.clip(NDVI, 0, 255).astype(np.uint8)
        colormappedNDVI = cv.applyColorMap(scaledNDVI, cv.COLORMAP_JET)
        imagePlot.set_data(colormappedNDVI)

## Another method for NDVI (Normalized Difference Vegetation Index)
## Source: Rouse 1974

  NDVI = (R800nm - R670nm)/(R800nm + R670nm)

## Use the following conversion to convert a multispectral image to a CCCI (canopy chlorophyll concentration index) image
## Source: Perry 2017
  CCCI = (NDRE - NDREmin)/(NDREmax - NDREmin)


## Use the following conversion to convert a multispectral image to a GLI (green leaf index) image

    GLI = (2Green - Red - Blue) / (2Green + Red + Blue)

## Use the following conversion to convert a multispectral image to a GNDVI (Green Normalized Difference Vegetation Index) image
## source Gitelson 1996

  GNDVI = (R_800nm - R_550nm)/(R_800nm + R_550nm)

## Another formula for GNDVI is

    GNDVI = (NIR - GREEN)/(NIR + GREEN)


## Use the following conversion to convert a multispectral image to a NDRE (Normalized Difference Red-edge Vegetation Index) image
## Source Fitzgerald 2010
## Note a paper citing most of these indexes in saved on the project literature review folder

  NDRE = (R800nm - R720nm)/(R800nm + R720nm)

## Use the following conversion to convert a multispectral image to a SIPI image

## Use the following conversion to convert a multispectral image to a EXGI (Excess Green Vegetation Index) image
## Source: Mengmeng Du 2017
  ExG of EXGI = 2G - B - R

## Use the following conversion to convert a multispectral image to a VARI (Visible Atmospherically Resistant Index) image

  VARI = (Green - Red)/(Green + Red - Blue)

## another method for VARI based on Gitelson 2002
  VARI = (R550nm - R670nm)/(R550nm + R670nm)

## Use the following conversion to convert a multispectral image to a TGI (Triangular Greenness Index) image

## Use the following conversion to convert a multispectral image to a AVRI image
