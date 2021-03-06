class Matrix(object):
	"""docstring for Matrix"""
	def __init__(self, n):
		super(Matrix, self).__init__()
		self.n = int(n)
		self.matrix = [[[0 for k in xrange(self.n)] for j in xrange(self.n)] for i in xrange(self.n)]

	def update_value(self, x, y, z, value):
		self.matrix[int(x)-1][int(y)-1][int(z)-1] = int(value)

	def query(self, x1, y1, z1, x2, y2, z2):
		s = 0
		for i in xrange(int(x1)-1, int(x2)):
			for j in xrange(int(y1)-1, int(y2)):
				for k in xrange(int(z1)-1, int(z2)):
					s += self.matrix[i][j][k]
		return s

	def get_matrix(self):
		return self.matrix