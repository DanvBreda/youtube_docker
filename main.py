from pytube import YouTube
import ffmpeg, os

file_name           = 'files/youtube_url.txt'
audio_location      = 'files/audio'
raw_video_location  = 'files/video/raw'
video_location      = 'files/video'
caption_location    = 'files/caption'

def Create_dir():
    '''Checks if audio and video is available in files, if not, add the directories'''

    if not os.path.exists(audio_location):
        os.makedirs(audio_location)
    if not os.path.exists(video_location):
        os.makedirs(video_location)
    if not os.path.exists(raw_video_location):
        os.makedirs(raw_video_location)
    if not os.path.exists(raw_video_location):
        os.makedirs(caption_location)

def Video_info(link=str):
    '''returns video info, this is helpfull if the current itags aren't working'''
    count = []
    for i in str(YouTube(link).streams.last).strip().split('<Stream:')[1:]:
        print(i)
        count.append(i)
    print(f"\nThere are {len(count)} ITAGS")

def Video_title(link=str,format='mp4'):
    '''Creating a readable and writable name'''
    title = YouTube(link).title.replace('/','').replace('"','').replace("'",'').replace('|','').replace('(','').replace(')','')[0:35]
    if format == '':
        filename = f'{title}'
    else:
        filename = f'{title}.{format}'
    return filename

def Download_song(link=str):
    '''Downloads audio of youtube link'''

    hd_aud = {258:'384kbps',141:'256kbps',251:'160kbps',140:'128kbps'}

    if Video_title(link) not in os.listdir(f'{audio_location}'):
        for key,value in hd_aud.items():
            try:
                YouTube(link).streams.get_by_itag(key).download(filename=Video_title(link),output_path=f'/{audio_location}')
            except:
                pass

        print(f'{Video_title(link)} ({value}) is downloaded successfully')
    else:
        print(f'No download needed, {Video_title(link)} already exists')

def Download_video(link=str):
    '''Downloads video of youtube link'''

    hd_vid = {401:'4k',313:'4k',271:'2k'} #,399:'1080p',248:'1080p',137:'1080p'}

    if Video_title(link) not in os.listdir(f'{raw_video_location}'):
        for key,value in hd_vid.items():
            try:
                YouTube(link).streams.get_by_itag(key).download(filename=Video_title(link),output_path=f'/{raw_video_location}')
            except:
                pass
    
        print(f'{Video_title(link)} ({value}) is downloaded successfully')
    else:
        print(f'No download needed, {Video_title(link)} already exists')

def Merge(link=str):
    '''Merges video and audio of youtube link'''

    video = ffmpeg.input(f'/{raw_video_location}/{Video_title(link)}')
    audio = ffmpeg.input(f'/{audio_location}/{Video_title(link)}')

    if Video_title(link) not in os.listdir(f'{video_location}'):
        # combines video and audio together
        try:
            ffmpeg.concat(video, audio, v=1, a=1).output(f'/{video_location}/{Video_title(link)}').run(overwrite_output=True)
            print("Merge is completed successfully")
        
            # removes raw video file
            os.remove(f'/{raw_video_location}/{Video_title(link)}') 

        except:
            print(f'''\nThere was an issue with combining the files.\ncheck if {Video_title(link)} is available in both {audio_location} and {raw_video_location}''')
    else:
        print(f'No download needed, {Video_title(link)} already exists')

def Download_caption(link=str):
    '''Downloads captions of youtube link'''
    captions = ['en','ko']
    try:
        for l in captions:
            YouTube(link).captions[l].download(f'{Video_title(link,"")}',output_path=f'/{caption_location}')
    except:
        pass

def Scrapingtime():
    '''Code for scraping audio and video'''
    Create_dir()

    with open(file_name) as file:
        myList = [i for i in file.read().strip().split('\n')]

    for i in myList:
        print('\nDownloading audio....')
        Download_song(i)
        print('\nDownloading video....')
        Download_video(i)
        print('\nDownloading captions....')
        Download_caption(i)
        print('\nCombining files....')
        Merge(i)

#run code
Scrapingtime()