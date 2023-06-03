import ffmpeg_streaming
from ffmpeg_streaming import Formats
import os

def auto_conversion(title, origin_path, destiny_path):
    print('Verificando caminhos...')
    origin = os.path.expanduser(f'{origin_path}')
    destiny = os.path.expanduser(f'{destiny_path}/')

    print('Criando pastas...')

    if not os.path.exists(f'{destiny}/{title}/'):
        os.mkdir(f'{destiny}/{title}/')

    print('Input arquivo')
    video = ffmpeg_streaming.input(origin)

    print('Configurando HLS - Instanciando ')

    hls = video.hls(Formats.h264())

    print('Configurando HLS - Representações')
    hls.auto_generate_representations()

    print('Iniciando conversão')

    hls.output(f"{destiny}/{title}/output.m3u8")


auto_conversion('eminem-mockingbird', '~/Videos/bases/eminem-mockingbird.mp4', '~/Videos/hls_videos/')