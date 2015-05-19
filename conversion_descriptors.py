import os
from invalid_format_error import InvalidFormatError

class ConversionDescriptor:
    """
    Describes the parameters necessary for a conversion job.
    """

    def __init__(self, src, target, fmt):
        """
        Initializes the Conversion Descriptor

        :param src: The absolute path of the source directory.
        :param target: The absolute path of the target directory.
        :param fmt: The format to convert to.
        """
        if not self.__validate_format(fmt):
            raise InvalidFormatError()

        self.source = src
        self.target = target
        self.format = fmt

    @staticmethod
    def __validate_format(format):
        """
        Validates that the user selected format is supported.

        :param format: The user selected format.
        :return: True if the format is supported, False otherwise.
        """

        return format.lower() in ['vmf', 'midi', 'xml']


class ConversionTask:
    """
    Describes a single conversion task.
    """

    def __init__(self, conversion_descriptor, file_name):
        """
        Initializes the Conversion Task

        :param conversion_descriptor: The conversion descriptor.
        :param file_name: The name of the file converted in this task.
        """
        self.source = os.path.join(conversion_descriptor.source, file_name)
        self.target = os.path.join(conversion_descriptor.target, file_name)
        self.format = conversion_descriptor.format

        file_name, file_extension = os.path.splitext(file_name)

        self.target = self.target.replace(file_extension[1:], conversion_descriptor.format)