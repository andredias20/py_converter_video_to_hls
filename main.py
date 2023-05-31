import ffmpeg_streaming
from ffmpeg_streaming import Formats

print('Input arquivo')
video = ffmpeg_streaming.input("/bases_video/video.mp4")

print('Configurando HLS - Instanciando ')

hls = video.hls(Formats.h264())

print('Configurando HLS - Representações')
hls.auto_generate_representations()

print('Iniciando conversão')

hls.output("./transcode_output/output.m3u8")