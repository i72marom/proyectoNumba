#include "exponenciacion.h"

vector<vector<double>> productoMatriz(
vector<vector<double>> &A, vector<vector<double>> &B) {
	vector<vector<double>> resultado(A.size(), vector <double>(A.size()));

	for (int i = 0; i < A.size(); ++i) {
		for (int j = 0; j < A.size(); ++j) {
			resultado[i][j] = 0;

			for (int k = 0; k < A.size(); ++k) {
				resultado[i][j] += A[i][k] * B[k][j];
			}
		}
	}

	return resultado;
}

void expMatriz() {
	int min, max, inc, exp;

	cout << "Orden mínimo: ";
	cin >> min;
	cout << "Orden máximo: ";
	cin >> max;
	cout << "Incremento: ";
	cin >> inc;
	cout << "Exponente: ";
	cin >> exp;

	tiemposExponenciacion(min, max, inc, exp);
}

void tiemposExponenciacion(int min, int max, int inc, int exp) {
	vector<vector <double>> M;
	vector<double> orden, tiempos;
	Clock Tiempo;

	for (int i = min; i <= max; i += inc) {
		M = vector <vector <double>>(i, vector <double>(i));
		rellenarMatriz(M);

		Tiempo.start();
		exponenciacion(M, i, exp);

		if (Tiempo.isStarted()) Tiempo.stop();

		tiempos.push_back(Tiempo.elapsed() * 0.000001);
		orden.push_back(i);

		cout << orden.back() << " ";
		cout << tiempos.back() << " " << endl;
	}

	escribeFichero(tiempos, orden, "../text/exponenciacion.txt");
}

void exponenciacion(vector<vector<double>> M, int o, int exp) {
	vector<vector<double>> resultado(o, vector <double>(o));

	resultado = productoMatriz(M, M);
	for (int i = 3; i < exp; ++i)
		resultado = productoMatriz(M, resultado);
}
