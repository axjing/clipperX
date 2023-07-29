import argparse
import os

from common.log_wrappers import Logging
from common import utils
from common.yaml_parser import YamlParser

logger=Logging(__name__).get_logger()

TRANSCRIBE,CUT, DAEMON,TO_MD,SRT_TO_COMACT=["transcribe","cut", "daemon","to_md","srt_to_compact"]

def get_input_param():
    parser = argparse.ArgumentParser(
        description="Edit videos based on transcribed subtitles",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("inputs", type=str, default=r"E:/ARTLIFEVido/230430/20230430_225530-1.m4a",nargs="+", help="Inputs filenames/folders")
    parser.add_argument('-cfg', '--cfg', default='config', required=False, type=str,
                        help='Your detailed configuration of Flow')

    args = parser.parse_args()
    args = YamlParser(args.cfg, path='').add_args(args)
    logger.info(args)
    return args

def main():
    
    args = get_input_param()

    if args.cut_mode==TRANSCRIBE:
        from cores.transcriber import Transcribe
        Transcribe(args).run()
    elif args.cut_mode==TO_MD:
        from common.utils import trans_srt_to_md

        if len(args.inputs) == 2:
            [input_1, input_2] = args.inputs
            base, ext = os.path.splitext(input_1)
            if ext != ".srt":
                input_1, input_2 = input_2, input_1
            trans_srt_to_md(args.encoding, args.force, input_1, input_2)
        elif len(args.inputs) == 1:
            trans_srt_to_md(args.encoding, args.force, args.inputs[0])
        else:
            logger.warn("Wrong number of files, please pass in a .srt file or an additional video file")

    elif args.cut_mode==CUT:
        from cores.cut import Cutter

        Cutter(args).run()
    elif args.cut_mode==DAEMON:
        from cores.daemon import Daemon

        Daemon(args).run()
    elif args.cut_mode==SRT_TO_COMACT:
        utils.compact_rst(args.inputs[0], args.encoding)
    else:
        logger.warn("No action, use -c, -t or -d")


if __name__ == "__main__":
    main()
