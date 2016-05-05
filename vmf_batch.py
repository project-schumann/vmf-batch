import os
import argparse
import sys
from multiprocessing import Pool
from conversion_descriptors import ConversionDescriptor, ConversionTask
from invalid_format_error import InvalidFormatError
from vmf_converter.vmf_converter import VMFConverter
from music21 import converter


def get_task_list(conversion_descriptor):
    """
    Gets a list of tasks based on the files in the provided directory.

    :param conversion_descriptor: The conversion descriptor instance.
    :return: A list of tasks to complete.
    """
    return [ConversionTask(conversion_descriptor, file_name) for file_name in os.listdir(conversion_descriptor.source)]


def parse_arguments():
    """
    Parses the command line arguments and produces a conversion descriptor.

    :return: A converstion descriptor indicating the paramters of this conversion job.
    """
    parser = argparse.ArgumentParser(description='Batch converts music files.')
    parser.add_argument('sourceDir', help='The absolute source directory path.', type=str)
    parser.add_argument('targetDir', help='The absolute target directory path.', type=str)
    parser.add_argument('outputFormat', help='The output format to use.', type=str)

    args = parser.parse_args()

    return ConversionDescriptor(args.sourceDir, args.targetDir, args.outputFormat)


def convert(task):
    """
    Performs the conversion task.

    :param task: The conversion task to execute.
    """
    print(task.source + ' -> ' + task.target + ' [STARTED]')
    
    try:
        score = converter.parse(task.source)
        score.write(task.format, task.target)
        print(task.source + ' -> ' + task.target + ' [DONE]')
    except:
        print('Unable to convert file: {0}. File Incompatible.'.format(task.source))


def initialize_converter():
    """
    Initializes the music21 converter.
    """
    converter.registerSubconverter(VMFConverter)


if __name__ == "__main__":
    conversion_descriptor = None

    try:
        conversion_descriptor = parse_arguments()
    except InvalidFormatError:
        print("ERROR: Invalid format requested.")
        sys.exit()

    initialize_converter()

    tasks = get_task_list(conversion_descriptor)

    with Pool() as pool:
        pool.map(convert, tasks)
