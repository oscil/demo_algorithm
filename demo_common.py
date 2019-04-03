import wave
import numpy as np
import os


def read_wav(wav_file):
    types = {
        1: np.int8,
        2: np.int16,
        4: np.int32
    }
    w = wave.open(wav_file)
    params = dict(zip(['nchannels', 'sampwidth', 'framerate', 'nframes', 'comptype', 'compname'], w.getparams()))
    print(params)
    content = w.readframes(params['nframes'])
    samples = np.frombuffer(content, dtype=types[params['sampwidth']])
    channels = np.zeros((params['nchannels'], int(samples.size/params['nchannels']) ))
    for n in range(params['nchannels']):
        channels[n] = samples[n::params['nchannels']]
    return params, channels


def convert2wav(file, mono=True, freq = 10000):
    mpg123_command = 'mpg123 -w \"%s\" -r {} \"%s\"'.format(freq)
    if mono:
        mpg123_command = 'mpg123 -w \"%s\" -r {} -m \"%s\"'.format(freq)
    # file_name = file.split('.')[0]
    # file_name = file_name.split('/')[-1]
    file_name = file.replace('/', '_')
    out_file = '/mnt/tmpfs/{}.wav'.format(file_name)
    cmd = mpg123_command % (out_file, file)
    os.system(cmd)
    return out_file

