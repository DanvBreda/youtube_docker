# Youtube_docker
### Just a cute youtube downloader with help of pytube, ffmpeg and docker.

## Key Features

* Uses Docker 
* Downloads youtube urls to:
  - songs
  - videos

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Docker](https://www.docker.com/products/docker-desktop/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/DanvBreda/youtube_docker.git

# Go into the repository
$ cd youtube_docker

# Add YouTube urls to the youtube_url.txt file

# Build docker app
$ docker build -t youtube .

# Run the app
$ docker run -v ./files:/files -it youtube
```

Happy viewing cheers =)

> **Note**
> if you like YouTube don't forget to support them.
> I'm not affiliated to YouTube in any way.

## Credits

This software uses the following open source packages:

- [pytube](https://pytube.io/en/latest/)
- [ffmpeg-python](https://python-ffmpeg.readthedocs.io/en/latest/)

## Support

<a href="https://buymeacoffee.com/bredatjuh" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/yellow_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
