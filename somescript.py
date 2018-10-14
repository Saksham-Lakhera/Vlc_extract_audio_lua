import moviepy.editor as mp
file = open("C:\\Users\\saksham\\Desktop\\pytry\\vlc_add.txt","r") 
stringval=file.readline()
stringval=stringval[8:]
i=0
clip= mp.VideoFileClip(stringval)
a=clip.duration
a=int(a/20)*20
while i<a:
    clip2= clip.subclip(i,i+20)
    clip2.audio.write_audiofile("C:\\Users\\saksham\\Desktop\\pytry\\audio\\"+str(int(i/20)+1)+".wav")
    i=i+20