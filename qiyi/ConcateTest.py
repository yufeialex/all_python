file_list_txt = "D/test.txt"
file_name = 'xyz'
cmd = 'ffmpeg -f concat -safe 0 -i {} -c:v copy -c:a copy -y  \"{}.mp4\"'.format(file_list_txt, file_name)
print(cmd)
