#Kurva Bezier di Python

import matplotlib.pyplot as plt
import numpy as np
import time

# Fungsi-Fungsi Pembantu
def plot_control_points(control_points):
    x_points = [point[0] for point in control_points]
    y_points = [point[1] for point in control_points]
    plt.plot(x_points, y_points, 'bo-')

def evaluate_bezier_segment(segment_points, t):
    # Titik kontrol kurva Bezier
    P0, P1, P2 = segment_points
    
    # Rumus Bezier kuadratik 
    x = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t ** 2 * P2[0]
    y = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t ** 2 * P2[1]

    return x, y

# Fungsi Divide and Conquer
def bezierDivideConquer(control_points, iterations):
    # Inisialisasi array posisi titik kurva Bezier
    bezier_points = []

    for _ in range(iterations):
        new_control_points = [control_points[0]]
        for i in range(len(control_points) - 1):
            # Titik kontrol awal
            new_control_points.append(control_points[i])
            # Perhitungan titik tengah antara titik kontrol
            new_point = ((control_points[i][0] + control_points[i + 1][0]) / 2, 
                         (control_points[i][1] + control_points[i + 1][1]) / 2)
            new_control_points.append(new_point)
        # Titik kontrol akhir
        new_control_points.append(control_points[-1])
        
        control_points = new_control_points.copy()

        # Evaluasi kurva Bezier antara dua titik kontrol secara berurutan
        for i in range(0, len(new_control_points) - 3, 2):
            points = new_control_points[i:i+3]
            for t in np.linspace(0, 1, 10):
                point = evaluate_bezier_segment(points, t)
                bezier_points.append(point)

    # Plot kurva Bezier
    x_values = [point[0] for point in bezier_points]
    y_values = [point[1] for point in bezier_points]
    plt.plot(x_values, y_values, 'r-')

# Fungsi Brute Force
def bezierBruteForce(control_points, iterations):
    # Inisialisasi array posisi titik kurva Bezier
    bezier_points = []

    for _ in range(iterations):
        new_control_points = [control_points[0]]
        for i in range(len(control_points) - 1):
            # Tambahkan titik kontrol baru di tengah di tiap segmen
            new_point = ((control_points[i][0] + control_points[i + 1][0]) / 2, (control_points[i][1] + control_points[i + 1][1]) / 2)
            new_control_points.append(new_point)
            new_control_points.append(control_points[i + 1])
        control_points = new_control_points.copy()
    
    # Plot kurva Bezier
    for i in range(0, len(control_points) - 2, 2):
        # Mengambil tiap segmen dari tiga titik kontrol secara berurutan
        points = control_points[i:i+3]  
        bezier_points = []
        for t in np.linspace(0, 1, 1000):
            point = evaluate_bezier_segment(points, t)
            bezier_points.append(point)
        x_values = [point[0] for point in bezier_points]
        y_values = [point[1] for point in bezier_points]
        plt.plot(x_values, y_values, 'b-')

# Input titik kontrol dan jumlah iterasi
iterations = int(input())
control_points = []

for i in range(3):
    x, y = map(int, input().split())
    control_points.append((x , y))

# Input pemilihan algoritma
j = int(input("Divide & Conquer (1) / Brute Force (2): " ))

# Pemrosesan tiap algoritma serta waktu
if (j == 1):
    start_time = time.time()
    bezierDivideConquer(control_points, iterations)
    end_time = time.time()
else:
    start_time = time.time()
    bezierBruteForce(control_points, iterations)
    end_time = time.time()

end_time = time.time()
execution_time = end_time - start_time

# Output
print("Waktu:", execution_time, "detik")
plt.title('Kurva Bezier')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.grid(True)
plt.show()
