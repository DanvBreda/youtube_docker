from pytube import YouTube
import ffmpeg, os, subprocess

location = 'files'
file_name = f'{location}/youtube_url.txt'

with open(file_name) as file:
    myList = [i for i in file.read().strip().split('\n')]

def Video_info(link):
    '''returns video info, this is helpfull if the current itags aren't working'''
    count = []
    for i in str(YouTube(link).streams.last).strip().split('<Stream:')[1:]:
        print(i)
        count.append(i)
    print(f"\nThere are {len(count)} ITAGS")

def Download_song(link):
    '''Downloads audio of youtube link'''
    mov_title = YouTube(link).title.replace('/','').replace('"','').replace("'",'').replace('|','').replace('(','').replace(')','')[0:35]
    filename_audio = f'{mov_title}.mp4'
    hd_aud = {258:'384kbps',141:'256kbps',251:'160kbps',140:'128kbps'}
    if filename_audio not in os.listdir(f'{location}/audio'):
        for key,value in hd_aud.items():
            try:
                YouTube(link).streams.get_by_itag(key).download(filename=filename_audio,output_path=f'/{location}/audio')
            except:
                pass

        print(f'Song {filename_audio}\n(itag {key} - {value}) download is completed successfully')
    else:
        print(f'No download needed, {filename_audio} already exists')

def Download_video(link):
    '''Downloads video of youtube link'''
    mov_title = YouTube(link).title.replace('/','').replace('"','').replace("'",'').replace('|','').replace('(','').replace(')','')[0:35]
    filename_video = f'{mov_title}_video.mp4'
    hd_vid = {401:'4k',313:'4k',271:'2k',399:'1080p',248:'1080p',137:'1080p'}
    if f'{mov_title}.mp4' not in os.listdir(f'files/video'):
        for key,value in hd_vid.items():
            try:
                YouTube(link).streams.get_by_itag(key).download(filename=filename_video,output_path=f'/{location}/video')
            except:
                pass
    
        print(f'Movie {filename_video},\n(itag {key} - {value}) download is completed successfully')
    else:
        print(f'No download needed, {mov_title}.mp4 already exists')

def Merge(link):
    '''Merges video and audio of youtube link'''
    mov_title = YouTube(str(link)).title
    mov_title = mov_title.replace('/','').replace('"','').replace("'","").replace('|','').replace('(','').replace(')','')[0:35]
    video = ffmpeg.input(f'/{location}/video/{mov_title}_video.mp4')
    audio = ffmpeg.input(f'/{location}/audio/{mov_title}.mp4')
    if f'{mov_title}.mp4' not in os.listdir(f'files/video'):
        # combines video and audio together
        try:
            ffmpeg.concat(video, audio, v=1, a=1).output(f'/files/video/{mov_title}.mp4').run(overwrite_output=True)
            print("Merge is completed successfully")
        
            # removes old video file
            os.remove(f'/files/video/{mov_title}_video.mp4') 

        except:
            print(f'''\nThere was an issue with combining the files.\ncheck if {mov_title}_video.mp4 and {mov_title}_audio.mp4 are available\nIf not try using info to find the right ITAGS!''')
    else:
        print(f'No download needed, {mov_title}.mp4 already exists')

for i in myList:
    print('\nDownloading audio....')
    Download_song(i)
    print('\nDownloading video....')
    Download_video(i)
    print('\nCombining files....')
    Merge(i)