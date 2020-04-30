from ImageProcess import imageproc


class FrameObject:
	def __init__(self, frames=None, yimg=None):
		"""
		:param frames: list(PIL.Image]
		"""
		self.frames = frames
		if yimg is not None:
			self.frames = [yimg.img]
		self.frame_index = 0

	def w(self):
		return self.frames[self.frame_index].size[0]

	def h(self):
		return self.frames[self.frame_index].size[1]

	def add_to_frame(self, background, x_offset, y_offset, alpha=1):
		imageproc.add(self.frames[self.frame_index], background, x_offset, y_offset, alpha=alpha)