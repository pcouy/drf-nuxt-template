import gzip
import logging
import logging.handlers
import pathlib
import shutil

logger = logging.getLogger(__name__)


class RotatingFileHandlerGzipBackups(logging.handlers.RotatingFileHandler):
    def rotation_filename(self, default_name):
        return f"{super().rotation_filename(default_name)}.gz"

    def rotate(self, source, dest):
        if source[-3:] != ".gz" and dest[-3:] == ".gz":
            with open(source, "rb") as f_in:
                with gzip.open(dest, "wb") as f_out:
                    shutil.copyfileobj(f_in, f_out)
            pathlib.Path.unlink(source)
        else:
            super().rotate(source, dest)
