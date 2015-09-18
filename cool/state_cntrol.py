import numpy as np
import scipy as sp
import control as ct

A = np.array([[0, 1],
              [0, -1]])
B = np.array([[0],
              [1]])
Q = np.diag([2, 1])
R = np.array([[1]])

def ricat(A,B,Q,R):
	P = sp.linalg.solve_continuous_are(A, B, Q, R)
	return P

def K(B,R,P):
	K = np.linalg.inv(R).dot(B.T).dot(P)
	return K

def E(A,B,K):
	E = np.linalg.eigvals(A-B.dot(K))
	return E


if __name__ == '__main__':
	print(ricat)