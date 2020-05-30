import argparse

def main(args):
    import os
    import glob
    from subprocess import Popen

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

    files = glob.glob(source + f'/*.{ext}' )
    print(f'Found {len(files)} .{ext} files')

    cmd_list = []

    for f in files:
        name, ext = os.path.basename(f).split('.')
        f_out = f'{dest}\\{prefix}{name}{postfix}.{ext}'

        preset_name = ''
        if preset:
            preset_name = ',' + os.path.basename(preset)

        cmd = [mrswatson, '--plugin-root', plugin_dir, '-p', f'{plugin}{preset_name}', '-i', f, '-o', f_out, '-q']
        cmd_list.append(cmd)

    proc_list =[Popen(cmd) for cmd in cmd_list]

    for proc in proc_list:
        proc.wait()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A batch wav file processor for applying a vst fx over a set of input wav files using mrswatson')
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