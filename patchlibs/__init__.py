    def create_thumbnail(self, size, quality=None):
        # invalidate the cache of the thumbnail with the given size first
        invalidate_cache(self.user, size)
        try:
            orig = self.avatar.storage.open(self.avatar.name, 'rb')
            image = Image.open(orig)
            image = self.transpose_image(image)
            quality = quality or settings.AVATAR_THUMB_QUALITY
            w, h = image.size
            if w != size or h != size:
                if w > h:
                    diff = int((w - h) / 2)
                    image = image.crop((diff, 0, w - diff, h))
                else:
                    diff = int((h - w) / 2)
                    image = image.crop((0, diff, w, h - diff))
                if image.mode in ('RGBA', 'LA'):
                   mode = image.mode
                   alpha = image.getchannel('A')
                   image = image.convert(mode[:-1]) \
                       .convert('P', palette=Image.ADAPTIVE, colors=255)
                   mask = Image.eval(alpha, lambda px: 255 if px < 128 else 0)
                   image.paste(255, mask)
                   image.info['transparency'] = 255
                if image.mode not in ("RGB", "RGBA"):
                    image = image.convert("RGB")
                image = image.resize((size, size), settings.AVATAR_RESIZE_METHOD)
                thumb = six.BytesIO()
                image.save(thumb, settings.AVATAR_THUMB_FORMAT, quality=quality)
                thumb_file = ContentFile(thumb.getvalue())
            else:
                thumb_file = File(orig)
            thumb = self.avatar.storage.save(self.avatar_name(size), thumb_file)
        except IOError as error:
            print("ERROR: ", error )
            #return" # What should we do here?  Render a "sorry, didn't work" img?

