from pytube import YouTube
import ffmpeg, os, subprocess

location = 'files'

def Open_url(folder):
    '''Opens .txt files with YouTube urls'''

    with open(f'{location}/{folder}.txt') as file:
        myList = filter(None, [i for i in file.read().strip().split('\n')])
    
    return myList

def Create_dir():
    '''Checks if audio and video is available in files, if not, add the directories'''
    if not os.path.exists(location+'/audio'):
        os.makedirs(location+'/audio')
    if not os.path.exists(location+'/video'):
        os.makedirs(location+'/video')

def Video_info(link):
    '''returns video info, this is helpfull if the current itags aren't working'''
    count = []
    for i in str(YouTube(link).streams.last).strip().split('<Stream:')[1:]:
        print(i)
        count.append(i)
    print(f"\nThere are {len(count)} ITAGS")

def Download_song(link,folder = 'audio',merge = None):
    '''Downloads audio of youtube link'''
    title = YouTube(link).title.replace('/','').replace('"','').replace("'",'').replace('|','').replace('(','').replace(')','')[0:35]
    filename_audio = f'{title}.mp4'
    hd_aud = {258:'384kbps',141:'256kbps',251:'160kbps',140:'128kbps'}
    if filename_audio not in os.listdir(f'{location}/{folder}'):
        if merge != None:
            filename_audio = f'{title}_audio.mp4'
            for key,value in hd_aud.items():
                try:
                    YouTube(link).streams.get_by_itag(key).download(filename=filename_audio,output_path=f'/{location}/{folder}')
                except:
                    pass

            print(f'''Song '{filename_audio}' download is completed''')
        else:
            print(f'No download needed, {filename_audio} already exists')

def Download_video(link):
    '''Downloads video of youtube link'''
    title = YouTube(link).title.replace('/','').replace('"','').replace("'",'').replace('|','').replace('(','').replace(')','')[0:35]
    filename_video = f'{title}_video.mp4'
    hd_vid = {401:'4k',313:'4k',271:'2k',399:'1080p',248:'1080p',137:'1080p'}
    if f'{title}.mp4' not in os.listdir(f'files/video'):
        for key,value in hd_vid.items():
            try:
                YouTube(link).streams.get_by_itag(key).download(filename=filename_video,output_path=f'/{location}/video')
            except:
                pass
    
        print(f'''Movie '{filename_video}' download is completed''')
    else:
        print(f'No download needed, {title}.mp4 already exists')

def Merge(link):
    '''Merges video and audio of youtube link'''
    title = YouTube(str(link)).title
    title = title.replace('/','').replace('"','').replace("'","").replace('|','').replace('(','').replace(')','')[0:35]
    video = ffmpeg.input(f'/{location}/video/{title}_video.mp4')
    audio = ffmpeg.input(f'/{location}/video/{title}_audio.mp4')
    if f'{title}.mp4' not in os.listdir(f'files/video'):
        # combines video and audio together
        try:
            ffmpeg.concat(video, audio, v=1, a=1).output(f'/files/video/{title}.mp4').run(overwrite_output=True)
            print("Merge is completed successfully")
        
            # removes old video file
            for i in ['video','audio']:
                os.remove(f'/files/video/{title}_{i}.mp4') 

        except:
            print(f'''\nThere was an issue with combining the files.\ncheck if {title}_video.mp4 and {title}_audio.mp4 are available\nIf not try using info to find the right ITAGS!''')
    else:
        print(f'No download needed, {title}.mp4 already exists')

Create_dir()

# for a in Open_url('audio_url'):
#     print('\nDownloading audio....')
#     Download_song(a)

for v in Open_url('video_url'):
#     print('\nDownloading audio....')
#     Download_song(v,'video','merge')
#     print('\nDownloading video....')
#     Download_video(v)
    # print('\nCombining files....')
    # Merge(v)



    title = YouTube(v).title
    print(title)
    hd_vid = {401:'4k',313:'4k',271:'2k',399:'1080p',248:'1080p',137:'1080p'}
    d = YouTube(v).streams.get_highest_resolution
    print(d)