#include "determinanteIterativo.h"

void determinanteIterativo() {
	vector<double> tiemposReales, nElementos;
	int max, min, incremento;

	cout << "Número mínimo de elementos: ";
	cin >> min;
	cout << "Número máximo de elementos: ";
	cin >> max;
	cout << "Incremento: ";
	cin >> incremento;

	tiempoDeterminante(min, max, incremento, tiemposReales, nElementos);
	escribeFichero(tiemposReales, nElementos, "../text/iterativo.txt");
}

void tiempoDeterminante(int min, int max, int incremento, vector<double> &tiemposReales, vector<double> &nElementos) {
	vector<vector <double>> M;
	Clock Tiempo;
	double det;

	for (int i = min; i <= max; i += incremento) {
		M = vector <vector <double>>(i, vector <double>(i));
		rellenarMatriz(M);

		Tiempo.start();
		det = calcularDeterminante(M, i);
		if (Tiempo.isStarted()) Tiempo.stop();

		tiemposReales.push_back(Tiempo.elapsed() * 0.000001);
		nElementos.push_back(i);

		cout << nElementos.back() << " ";
		cout << tiemposReales.back() << " ";
		cout << det << endl;
	}
}

double calcularDeterminante(vector <vector <double>> &M, int n) {
	double aux;
	double determinante = 1;
	
	for(int k = 0; k < n-1; k++){//recorrer la diagonal
		determinante *= M[k][k];
		
		if(M[k][k]==0) return 0;
		else {
			for (int i = k+1; i < n; i++) {//recorrer fila
				aux = -M[i][k];
				
				for(int j = k; j < n; j++)
					M[i][j] = M[i][j] + aux * M[k][j] / M[k][k];
			}
		}
	  
	}
	
	return determinante * M[n-1][n-1];
}
