import os
data_path = '/data/train/'
videos=[2,
9]
# 11,
# 14,
# 33,
# 33,
# 35,
# 49,
# 51,
# 58,
# 63,
# 66,
# 72,
# 73,
# 74,
# 83,
# 91,
# 93,
# 95,
# 97]

for video in videos:
    print('Extracting features from video: {}'.format(video))
    os.system('./debug/DenseTrack {}{}.mp4 > {}.txt'.format(data_path, video, video))