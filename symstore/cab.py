from os import path

# this flag is false on systems that don't provide gcab library
compression_supported = True

try:
    from gi.repository import GCab
    from gi.repository import Gio
except ImportError as e:
    compression_supported = False


def compress(src_path, dest_path):
    assert compression_supported
    cab_file = GCab.File.new_with_file(path.basename(src_path),
                                       Gio.File.new_for_path(src_path))

    cab_folder = GCab.Folder.new(GCab.Compression.MSZIP)
    cab_folder.add_file(cab_file, False)

    cab = GCab.Cabinet.new()
    cab.add_folder(cab_folder)

    out_file = Gio.File.new_for_path(dest_path)
    cab.write_simple(out_file.create(Gio.FileCreateFlags.NONE))
