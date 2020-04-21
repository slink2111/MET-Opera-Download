# The only vars need edit are: 
# operaName
# subsurl
# urlSound
# urlMovie

import requests
import os
import subprocess
import shutil
import errno
import string
import io

operaName = "Elektra"

i=0
subsurl = "https://house-fastly-signed-us-east-1-prod.brightcovecdn.com/media/v1/hls/v4/clear/102076671001/0c832a03-2dc8-42df-a0a3-16de59ff4808/342ad130-7bbb-4aa9-9cd6-d7b6b848e5ce/segment10.vtt?fastly_token=NWU5ZjkxOGVfNzNjZTZlZWE1OTY2YTU3OTFlYTc2YTljZGUyYTI2NzhjYjliNDY0Y2UxZWJkZGY4YWJiZTVmOGI2MTM2ZjkwN18vL2hvdXNlLWZhc3RseS1zaWduZWQtdXMtZWFzdC0xLXByb2QuYnJpZ2h0Y292ZWNkbi5jb20vbWVkaWEvdjEvaGxzL3Y0L2NsZWFyLzEwMjA3NjY3MTAwMS8wYzgzMmEwMy0yZGM4LTQyZGYtYTBhMy0xNmRlNTlmZjQ4MDgvMzQyYWQxMzAtN2JiYi00YWE5LTljZDYtZDdiNmI4NDhlNWNlLw%3D%3D"

while False:
    urlSound = "https://house-fastly-signed-us-east-1-prod.brightcovecdn.com/media/v1/hls/v4/clear/102076671001/0c832a03-2dc8-42df-a0a3-16de59ff4808/834f2391-1bec-4c0f-9465-510d69d9283c/5x/segment3.ts?fastly_token=NWU5ZjkyMDJfN2M5ZWE0N2EwNzhjYTE1YjFiZGQwMjE5OTQyMzkxZDM2Nzc3MjU2MDBjOTlkOGZiODhmZmE4MGVkMjZlN2RkZV8vL2hvdXNlLWZhc3RseS1zaWduZWQtdXMtZWFzdC0xLXByb2QuYnJpZ2h0Y292ZWNkbi5jb20vbWVkaWEvdjEvaGxzL3Y0L2NsZWFyLzEwMjA3NjY3MTAwMS8wYzgzMmEwMy0yZGM4LTQyZGYtYTBhMy0xNmRlNTlmZjQ4MDgvODM0ZjIzOTEtMWJlYy00YzBmLTk0NjUtNTEwZDY5ZDkyODNjLw%3D%3D"
    urlMovie = "https://house-fastly-signed-us-east-1-prod.brightcovecdn.com/media/v1/hls/v4/clear/102076671001/0c832a03-2dc8-42df-a0a3-16de59ff4808/5cea89eb-3a8f-47ea-bcc7-fde4563cc86c/5x/segment3.ts?fastly_token=NWU5ZjkyMjdfZGYyMmQ4MjYxMTFmNjQ0NjZhODY1YmJjNzc1NjY3ZDVhZWRkN2ZhNzAwZjE3MWNlOTdmNGEwMzU3NjFhMWEzMV8vL2hvdXNlLWZhc3RseS1zaWduZWQtdXMtZWFzdC0xLXByb2QuYnJpZ2h0Y292ZWNkbi5jb20vbWVkaWEvdjEvaGxzL3Y0L2NsZWFyLzEwMjA3NjY3MTAwMS8wYzgzMmEwMy0yZGM4LTQyZGYtYTBhMy0xNmRlNTlmZjQ4MDgvNWNlYTg5ZWItM2E4Zi00N2VhLWJjYzctZmRlNDU2M2NjODZjLw%3D%3D"
    urlt = urlSound.split('.ts')
    urlt[0] = urlt[0].rstrip(string.digits)
    urlSound = urlt[0] + str(i) + ".ts" + urlt[1]
    del urlt

    urlt = urlMovie.split('.ts')
    urlt[0] = urlt[0].rstrip(string.digits)
    urlMovie = urlt[0] + str(i) + ".ts" + urlt[1]
    del urlt

    r = requests.get(urlMovie)
    print("for " + str(i) + " response is " + str(r))
    if r.status_code != 200:
        break
    movieTS = "./" + operaName + "/" + str(i).zfill(4) + ".ts"
    if not os.path.exists(os.path.dirname(movieTS)):
        try:
            os.makedirs(os.path.dirname(movieTS))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    song = open(movieTS, "wb")
    song.write(r.content)
    song.close()

    r2 = requests.get(urlSound)
    print("for audio " + str(i) + " response is " + str(r))
    soundTS = "./" + operaName + "/audio/" + str(i).zfill(4) + ".ts"
    if not os.path.exists(os.path.dirname(soundTS)):
        try:
            os.makedirs(os.path.dirname(soundTS))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    song2 = open(soundTS, "wb")
    song2.write(r2.content)
    song2.close()

    i = i+1

i=0
subsFile_vvt = "./" + operaName + "/" + operaName + ".vvt"
while True:
    urlt = subsurl.split('.vtt')
    urlt[0] = urlt[0].rstrip(string.digits)
    subsurl = urlt[0] + str(i) + ".vtt" + urlt[1]
    del urlt

    r = requests.get(subsurl)
    print("for subs " + str(i) + " response is " + str(r))
    if r.status_code != 200:
        break

    if not os.path.exists(os.path.dirname(subsFile_vvt)):
        try:
            os.makedirs(os.path.dirname(subsFile_vvt))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with io.open(subsFile_vvt, "a", encoding="utf-8") as song:
        song.write(r.text.lstrip("\n X-TIMESTAMP-MAP=LOCAL:00:00:00.000,MPEGTS:0"))
    song.close()
    i = i + 1

cur_dir = os.path.abspath(".")
movieDir = "./" + operaName
soundDir = "./" + operaName + "/audio"

shutil.copyfile( "joiner.bat", movieDir + '/joiner.bat')
shutil.copyfile( "joiner.bat", soundDir + '/joiner.bat')
joinerMovieTS = cur_dir + "/" + operaName + '\\joiner.bat'
joinerSoundTS = cur_dir + "\\" + operaName + '\\audio\\joiner.bat'
joinedMovie = cur_dir + "\\" + operaName + "\\joined_files.ts"
joinedSound = cur_dir + "\\" + operaName + "\\audio\\joined_files.ts"
joinedSubs = cur_dir + "\\" + operaName + "\\" + operaName + ".vvt"
joinedSubs_srt = cur_dir + "\\" + operaName + "\\" + operaName + ".srt"
out =  cur_dir + "\\" + operaName + "\\" + operaName + ".ts"
subprocess.check_call([joinerMovieTS], cwd=movieDir)
subprocess.check_call([joinerSoundTS], cwd=soundDir)
arg1= "\"" + joinedMovie + "\""
arg2 = "-i \"" + joinedSound + "\""
arg3 = "-c copy \"" + out
subprocess.run(["ffmpeg.exe", "-i", joinedSubs, joinedSubs_srt], cwd=cur_dir)
subprocess.run(["ffmpeg.exe", "-i", joinedMovie, "-i", joinedSound, "-c", "copy", out], cwd=cur_dir)
