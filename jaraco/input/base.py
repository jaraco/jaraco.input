
class NormalizingAxisJoystick(object):
	def set_translate_method(self, normalize_axes):
		"""
		Set the method that will be called to normalize
		the values for analog axis.
		"""
		choices = [self.translate_identity, self.translate_using_data_size]
		self.translate = choices[normalize_axes]

	def translate_using_data_size(self, value, data_size):
		"""
		Normalizes analog data to [0,1] for unsigned data
		and [-0.5,0.5] for signed data.
		data_size is the binary size of the data in bytes.
		"""
		data_bits = 8*data_size
		return float(value)/(2**data_bits-1)

	def translate_identity(self, value, data_size=None):
		return value

