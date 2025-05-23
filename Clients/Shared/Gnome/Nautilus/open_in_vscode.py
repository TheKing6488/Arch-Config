from os.path import isdir
from gi import require_version
from gi.repository import Nautilus, GObject, Gio, GLib


class OpenInVSCodeAction(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        super().__init__()
        session = Gio.bus_get_sync(Gio.BusType.SESSION, None)
        self._systemd = None
        # Check if the this system runs under systemd, per sd_booted(3)
        if isdir('/run/systemd/system/'):
            self._systemd = Gio.DBusProxy.new_sync(session,
                    Gio.DBusProxyFlags.NONE,
                    None,
                    "org.freedesktop.systemd1",
                    "/org/freedesktop/systemd1",
                    "org.freedesktop.systemd1.Manager", None)

    def _open_vscode(self, path):
        cmd = ['code', path]
        child = Gio.Subprocess.new(cmd, Gio.SubprocessFlags.NONE)
        if self._systemd:
            # Move new VS Code process into a dedicated systemd scope
            pid = int(child.get_identifier())
            props = [("PIDs", GLib.Variant('au', [pid])),
                ('CollectMode', GLib.Variant('s', 'inactive-or-failed'))]
            name = 'app-nautilus-code-{}.scope'.format(pid)
            args = GLib.Variant('(ssa(sv)a(sa(sv)))', (name, 'fail', props, []))
            self._systemd.call_sync('StartTransientUnit', args,
                    Gio.DBusCallFlags.NO_AUTO_START, 500, None)

    def _menu_item_activated(self, _menu, paths):
        for path in paths:
            self._open_vscode(path)

    def _make_item(self, name, paths):
        item = Nautilus.MenuItem(
            name=name,
            label="Open in VS Code",
            icon="com.visualstudio.code"
        )
        item.connect("activate", self._menu_item_activated, paths)
        return item

    def _paths_to_open(self, files):
        paths = []
        for file in files:
            location = file.get_location()
            path = location.get_path()
            if path and path not in paths:
                paths.append(path)
        if 10 < len(paths):
            # Limit to prevent accidentally opening too many VS Code windows
            return []
        else:
            return paths

    def get_file_items(self, *args):
        # Nautilus 3.0 API passes args (window, files), 4.0 API just passes files
        files = args[0] if len(args) == 1 else args[1]
        paths = self._paths_to_open(files)
        if paths:
            return [self._make_item(name='VSCodeNautilus::open_in_vscode', paths=paths)]
        else:
            return []

    def get_background_items(self, *args):
        # Nautilus 3.0 API passes args (window, file), 4.0 API just passes file
        file = args[0] if len(args) == 1 else args[1]
        paths = self._paths_to_open([file])
        if paths:
            return [self._make_item(name='VSCodeNautilus::open_folder_in_vscode', paths=paths)]
        else:
            return []
