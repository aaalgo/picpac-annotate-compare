import os
from jinja2 import Environment, FileSystemLoader

TMPL_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                './templates')
env = Environment(loader=FileSystemLoader(searchpath=TMPL_DIR))
tmpl = env.get_template('overlay_gallery.html')

class OverlayGallery:
    def __init__ (self, path, ext = '.jpg'):
        self.next_id = 0
        self.path = path
        self.ext = ext
        self.images = []
        try:
            os.makedirs(path)
        except:
            pass
        pass

    def next (self):
        path1 = '%03d%s' % (self.next_id, self.ext)
        path2 = '%03d_orig%s' % (self.next_id, self.ext)
        self.images.append((path1, path2))
        self.next_id += 1
        return os.path.join(self.path, path1), os.path.join(self.path, path2)

    def flush (self):
        with open(os.path.join(self.path, 'index.html'), 'w') as f:
            f.write(tmpl.render(images = self.images))
            pass
        pass

