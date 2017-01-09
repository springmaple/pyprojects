class Dictionary:

	_INIT_SIZE = 4
	_PERTURB_SHIFT = 5

	def __init__(self):
		self._size = self._INIT_SIZE 
		self._mask = self._INIT_SIZE - 1
		self._keys = [None] * self._INIT_SIZE 
		self._vals = [None] * self._INIT_SIZE
		self._used = 0

	def get(self, key):
		ep, i = self._lookup(key, self._keys)
		if ep is None: 
			raise KeyError(key)
		return self._vals[i] 

	def set(self, key, val):
		if self._used / self._size > 0.7:
			self._resize_arr()
		
		ep, i = self._lookup(key, self._keys)

		if (ep is None): 
			self._keys[i] = key
			self._vals[i] = val
			self._used += 1
		else:
			self._vals[i] = val

	def _resize_arr(self):
		self._size <<= 1
		self._mask = self._size - 1
		new_keys = [None] * self._size
		new_vals = [None] * self._size
		for key, val in zip(self._keys, self._vals):
			if key is None:
				continue
			_, i = self._lookup(key, new_keys)
			new_keys[i] = key
			new_vals[i] = val
		self._keys = new_keys
		self._vals = new_vals

	def _lookup(self, key, ls):
		"""Returns (found_key, index), found_key can be None if not found."""
		perturb = key_hash = hash(key)
		i = key_hash & self._mask
		ep = ls[i]
		while ep is not None and key_hash != hash(ep):
			perturb >>= self._PERTURB_SHIFT
			i = (i << 2) + i + perturb + 1
			i &= self._mask
			ep = ls[i]
		return ep, i


if __name__ == '__main__':
	dct = Dictionary()
	for i in (3, 7, 15, 31):
		try:
			dct.set(i, i)
		except Exception as ex:
			print('insert:', i, type(ex), ex)
			exit(0)
		try:
			assert dct.get(i) == i
		except Exception as ex:
			print('getter:', i, type(ex), ex)
			exit(0)
	print('SUCCESS', dct._vals)
