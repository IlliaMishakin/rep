import math
import numpy as np
print('1.1 A - B:\n', np.matrix('1 2; 4 -1') - np.matrix('2 -3; -4 1'))
print('1.2 A - B:\n', np.matrix('2 3 1; -1 1 0; 1 2 -1') - np.matrix('1 2 1; 0 1 2; 3 1 1'))
print('1.3 A - B:\n', np.matrix('1 1 1; 0 1 1; 0 0 1') - np.matrix('7 5 3; 0 7 5; 0 0 7'))

print('2.1 A ^ 2\n', pow(np.matrix('-1 2; 0 1'), 2))
print('2.2 A ^ 2\n', pow(np.matrix('-1 0 2; 0 1 0; 1 2 -1'), 2))
print('2.3 A ^ 2\n', pow(np.matrix('1 0 0 0; 0 2 0 0; 0 0 3 0; 0 0 0 4'), 2))

print('3.1 A * B:\n', np.matrix('3 5; 6 -1') * np.matrix('2 1; -3 2'))
print('3.2 A * B:\n', np.matrix('5 8 -4; 6 9 -5; 4 7 -3') * np.matrix('3 2 5; 4 -1 3; 9 6 5'))
print('3.3 A * B:\n', np.matrix('3 0 7; -4 2 3; -1 1 2') * np.matrix('1; 2; 4'))
print('3.4 A * B:\n', np.matrix('5 0 2 3; 4 1 5 3; 3 1 -1 2') * np.matrix('6; -2; 7; 4'))
print('3.5 A * B:\n', np.matrix('3; 1; -1; 5; 2') * np.matrix('4 0 -2 3 1'))

a = np.matrix('2 3 4; 1 0 6; 7 8 9')
print('4.1 Det(A):\n', np.linalg.det(a))
a = np.matrix('0 2 0; 3 4 5; 6 7 8')
print('4.2 Det(A):\n', np.linalg.det(a))
a = np.matrix('3 4 5; 1 1 2; 2 4 3')
print('4.3 Det(A):\n', np.linalg.det(a))
a = np.matrix('1 2 3; -1 2 1; 1 3 2')
print('4.4 Det(A):\n', np.linalg.det(a))
a = np.matrix('1 5 -5; 4 0 3; 2 -10 3')
print('4.5 Det(A):\n', np.linalg.det(a))

a = np.matrix('1 2 3 4; -2 1 -4 3; 3 -4 -1 2; 4 3 -2 -1')
print('5.1 Det(A):\n', np.linalg.det(a))
a = np.matrix('2 3 4 1; 1 2 3 4; 3 4 1 2; 4 1 2 3')
print('5.2 Det(A):\n', np.linalg.det(a))
a = np.matrix('1 2 0 0 0; 1 0 2 0 0;1 0 0 2 0; 1 0 0 0 2; 0 0 1 1 1 ')
print('5.3 Det(A):\n', np.linalg.det(a))

a = np.matrix('1 2 -3; 0 1 2; 0 0 1')
print('6.1 Invers(A):\n', np.linalg.inv(a))
a = np.matrix('2 5 7; 6 3 4; 5 -2 -3')
print('6.2 Invers(A):\n', np.linalg.inv(a))
a = np.matrix('1 2 2; 2 1 -2; 2 -2 1')
print('6.3 Invers(A):\n', np.linalg.inv(a))
a = np.matrix('2 1 0 0; 3 2 0 0; 1 1 3 4; 2 -1 2 3')
print('6.4 Invers(A):\n', np.linalg.inv(a))
a = np.matrix('-2 3 1 -1; 1 1 -1 -1; 1 -1 1 -1; 1 -1 -1 1')
print('6.5 Invers(A):\n', np.linalg.inv(a))

a = np.matrix('1 2 3 4; 3 -1 2 5; 1 2 3 4; 1 3 4 5')
print('7.1 Rank(A):\n', np.linalg.matrix_rank(a))
a = np.matrix('1 -1 3 4; 0 -1 2 1; 1 1 -1 2; 2 3 -5 3')
print('7.2 Rank(A):\n', np.linalg.matrix_rank(a))
a = np.matrix('-2 3 1 -1; 3 2 1 4; 1 2 3 4; 0 2 3 3')
print('7.3 Rank(A):\n', np.linalg.matrix_rank(a))

a = np.matrix('14 4 6; 5 -3 2; 10 -11 5')
if (np.linalg.det(a) != 0):
    x1 = np.matrix('14 4 30; 5 -3 15; 10 -11 36')
    print('8.1 Det(A)\n x1 =', np.linalg.det(x1) / np.linalg.det(a))
    x2 = np.matrix('14 30 6; 5 15 2; 10 36 5')
    print(' x2 =', np.linalg.det(x2) / np.linalg.det(a))
    x3 = np.matrix('30 4 6; 15 -3 2; 36 -11 5')
    print(' x3 =', np.linalg.det(x3) / np.linalg.det(a))

    a = np.matrix('2 -1 1; 3 2 2; 1 -2 1')
if (np.linalg.det(a) != 0):
    x1 = np.matrix('2 -1 2; 3 2 -2; 1 -2 1')
    print('8.2 Det(A)\n x1 =', np.linalg.det(x1) / np.linalg.det(a))
    x2 = np.matrix('2 2 1; 3 -2 2; 1 1 1')
    print(' x2 =', np.linalg.det(x2) / np.linalg.det(a))
    x3 = np.matrix('2 -1 1; -2 2 2; 1 -2 1')
    print(' x3 =', np.linalg.det(x3) / np.linalg.det(a))

    a = np.matrix('3 -5 3; 1 2 1; 2 7 -1')
if (np.linalg.det(a) != 0):
    x1 = np.matrix('3 -5 1; 1 2 4; 2 7 8')
    print('8.3 Det(A)\n x1 =', np.linalg.det(x1) / np.linalg.det(a))
    x2 = np.matrix('3 1 3; 1 4 1; 2 8 -1')
    print(' x2 =', np.linalg.det(x2) / np.linalg.det(a))
    x3 = np.matrix('1 -5 3; 4 2 1; 8 7 -1')
    print(' x3 =', np.linalg.det(x3) / np.linalg.det(a))

    a = np.matrix('7 3 -6; 7 9 -9; 2 -4 9')
if (np.linalg.det(a) != 0):
    x1 = np.matrix('7 3 -1; 7 9 5; 2 -4 28')
    print('8.4 Det(A)\n x1 =', np.linalg.det(x1) / np.linalg.det(a))
    x2 = np.matrix('7 -1 -6; 7 5 -9; 2 28 9')
    print(' x2 =', np.linalg.det(x2) / np.linalg.det(a))
    x3 = np.matrix('-1 3 -6; 5 9 -9; 28 -4 9')
    print(' x3 =', np.linalg.det(x3) / np.linalg.det(a))

    a = np.matrix('2 1 -5; 1 2 -4; 1 -1 -1')
if (np.linalg.det(a) != 0):
    x1 = np.matrix('2 1 -1; 1 2 1; 1 -1 -2')
    print('8.5 Det(A)\n x1 =', np.linalg.det(x1) / np.linalg.det(a))
    x2 = np.matrix('2 -1 -5; 1 1 -4; 1 -2 -1')
    print(' x2 =', np.linalg.det(x2) / np.linalg.det(a))
    x3 = np.matrix('-1 1 -5; 1 2 -4; -2 -1 -1')
    print(' x3 =', np.linalg.det(x3) / np.linalg.det(a))
else: 
    print('8.5 Det(a)\n x e R')
 
a = np.matrix('1 2 -1; 3 4 1; 5 1 -3') 
inv = np.linalg.inv(a)
b = np.matrix('-3; 1; -2')
print('9.1 Matrix Metod:\n', inv * b)

a = np.matrix('1 -2 3; 4 2 -3; 3 -3 5') 
inv = np.linalg.inv(a)
b = np.matrix('-5; 0; -9')
print('9.2 Matrix Metod:\n', inv * b)

a = np.matrix('3 2 1; 2 -1 1; 1 5 0') 
inv = np.linalg.inv(a)
b = np.matrix('5; 6; -3')
print('9.3 Matrix Metod:\n', inv * b)

a = np.matrix('2 -1 1; 3 4 -2; 1 -3 1') 
inv = np.linalg.inv(a)
b = np.matrix('5; -3; 4')
print('9.4 Matrix Metod:\n', inv * b)

a = np.matrix('4 1 4; 1 1 2; 2 1 2') 
inv = np.linalg.inv(a)
b = np.matrix('-2; -1; 0')
print('9.5 Matrix Metod:\n', inv * b)

a = np.matrix('1 -4 0; 2 -3 1; 1 4 2') 
inv = np.linalg.inv(a)
b = np.matrix('-5; -7; -1')
print('9.6 Matrix Metod:\n', inv * b)
