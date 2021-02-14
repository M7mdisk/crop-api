# Crop-API
simple API for cropping images written in python (using FastAPI)

I could not find an API to crop images that "just works" and was simple and free, so I made one! :)

## Usage

`https://crop-api.herokuapp.com/crop/?url={image_url}&xmin={x1}&ymin={y1}&xmax={x2}&ymax={y2}`

where:
* `image_url`: your image url.
* `x1`: the x coodinate position of the upper left point of cropped area.
* `y1`: the y coodinate position of the upper left point of cropped area.
* `x2`: the x coodinate position of the lower right point of cropped area.
* `y2`: the y coodinate position of the lower right point of cropped area.

Note: for any given image (0,0) is the uppper left point of the image.

### Contributions

Please do! feel free to do a pull request anytime! 
