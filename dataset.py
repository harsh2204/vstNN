# Dataset located in data/*BASS and data/*GUITAR*
# vst2.x plugin dlls located in plugins/*/

# Goal: create a utility to process a set of wav files through a given vst and it's respective parameters and presets using mrswatson

# REPLACE THESE WITH ARGPARSE
import argparse

def main(args):
    import os
    import glob
    import subprocess

    source = args.source
    dest = args.dest
    mrswatson = 'mrswatson64' if not args.mrswatson else 'mrswatson'
    postfix = args.postfix
    prefix = args.prefix

    plugin = args.plugin
    preset = args.preset


    cwd = os.getcwd()
    plugin_dir = os.path.abspath(os.path.dirname(preset))
    source = os.path.abspath(source)
    dest = os.path.abspath(dest)

    os.chdir(plugin_dir)
    ext = args.ext

    print(source)
    files = glob.glob(source + f'/*.{ext}' )
    print(f'Found {len(files)} .{ext} files')

    for f in files[:1]:
        name, ext = os.path.basename(f).split('.')
        f_out = f'{dest}\\{prefix}{name}{postfix}.{ext}'

        preset_name = ''
        if preset:
            preset_name = ',' + os.path.basename(preset)

        cmd = [mrswatson, '--plugin-root', plugin_dir, '-p', f'{plugin}{preset_name}', '-i', f, '-o', f_out, '-q']
        print(cmd)
        subprocess.run(cmd)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='source', required=True, help='Input source files directory containing supported audio files')
    parser.add_argument('-o', dest='dest', required=True, help='Output directory to store the procossed audio files')
    parser.add_argument('-p', dest='plugin', required=True, help='FX plugin to apply to the set of audio files')
    parser.add_argument('-r', dest='preset', required=True, help='FX plugin preset file only *.fxp file')
    parser.add_argument('-x86', dest='mrswatson', help='Use 32-bit variant of mrswatson', action='store_true')
    parser.add_argument('-postfix', dest='postfix', help='Postfix for the output files', default='_y')
    parser.add_argument('-prefix', dest='prefix', help='Prefix for the output files', default='')
    parser.add_argument('-ext', dest='ext', help=argparse.SUPPRESS , default='wav')

    args = parser.parse_args()
    main(args)