from networks import Generator, Discriminator
import torch
import os.path
import torchvision.utils as vutils
import torch.nn.functional as F
import collections
import ipdb 
st = ipdb.set_trace
class Inferencer:
    def __init__(self, generator_channels, nz, style_depth):
        self.nz = nz
        self.generator = Generator(generator_channels, nz, style_depth).cuda()

    def inference(self, n):
        test_z = torch.randn(n, self.nz).cuda()
        with torch.no_grad():
            self.grow()
            img_size = 8
            # st()
            filename = 'checkpoints/{}x{}_last.pth'.format(img_size, img_size)
            while os.path.isfile(filename):
                # st()
                self.load_checkpoint(img_size, filename)
                
                self.generator.eval()
                fake = self.generator(test_z, alpha=1)
                fake = (fake + 1) * 0.5
                fake = torch.clamp(fake, min=0.0, max=1.0)
                fake = F.interpolate(fake, size=(256, 256))
                # st()
                vutils.save_image(fake, 'images/{}x{}.png'.format(img_size, img_size))

                self.grow()
                img_size *= 2
                filename = 'checkpoints/{}x{}_last.pth'.format(img_size, img_size)


    def grow(self):
        self.generator.grow()
        self.generator.cuda()
  
    def load_checkpoint(self, img_size, filename):
        checkpoint = torch.load(filename)
        # st()
        print('load {}x{} checkpoint'.format(checkpoint['img_size'], checkpoint['img_size']))
        while img_size < checkpoint['img_size']:
            self.grow()

        generator_checkpoint = checkpoint['generator']
        d = collections.OrderedDict()
        for key in generator_checkpoint.keys():
            # d[key] = generator_checkpoint[key] 
            d[key[7:]] = generator_checkpoint[key] 
        self.generator.load_state_dict(d)
