import ffmpeg

def embedd(audio: str, subtitles: list):
    #Define vars
    video=audio

    for sub in subtitles:
        sub1= sub
        l1="en"
        t1="English"


    sub2="Introduction.srt"
    l2="fr"
    t2="French"
    
    output_file="output.mkv"

    #Define input values
    input_ffmpeg = ffmpeg.input(video)
    input_ffmpeg_sub1 = ffmpeg.input(sub1)
    input_ffmpeg_sub2 = ffmpeg.input(sub2)

    #Define output file
    input_video = input_ffmpeg['v']
    input_audio = input_ffmpeg['a']
    input_subtitles1 = input_ffmpeg_sub1['s']
    input_subtitles2 = input_ffmpeg_sub2['s']
    output_ffmpeg = ffmpeg.output(
        input_video, input_audio, input_subtitles1, input_subtitles2, output_file,
        vcodec='copy', acodec='copy', 
        **{'metadata:s:s:0': "language="+l1, 'metadata:s:s:0': "title="+t1, 'metadata:s:s:1': "language="+l2, 'metadata:s:s:1': "title="+t2 }
    )

    # If the destination file already exists, overwrite it.
    output_ffmpeg = ffmpeg.overwrite_output(output_ffmpeg)

    # Print the equivalent ffmpeg command we could run to perform the same action as above.
    print(ffmpeg.compile(output_ffmpeg))

    # Do it! transcode!
    ffmpeg.run(output_ffmpeg)
