def euclideanDistance(point1, point2):
  """
  İki nokta arasındaki Öklid mesafesini hesaplar.

  Parametreler:
    point1: (x1, y1) şeklinde bir demet olan ilk nokta.
    point2: (x2, y2) şeklinde bir demet olan ikinci nokta.

  Geri Dönüş Değeri:
    İki nokta arasındaki Öklid mesafesi (float).
  """
  x1, y1 = point1
  x2, y2 = point2
  return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

points = [(1, 2), (4, 5), (3, 1), (7, 6)]
distances = []

for i in range(len(points)):
  for j in range(i + 1, len(points)):
    distance = euclideanDistance(points[i], points[j])
    distances.append(distance)

minimumDistance = min(distances)

print("Minimum mesafe:", minimumDistance)
