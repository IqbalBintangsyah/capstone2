import matplotlib.ticker as plticker
import matplotlib.pyplot as plt
import numpy as np
import os.path
from PIL import Image

#fungsi buat bikin sel 11x11
def cellConverter(dem):
	cell = []
	for x in range(303):
		#print(x)
		cell_y = []
		for y in range(303):
			sum = 0
			for k in range(11):
				for l in range(11):
					sum = sum + dem[x*11-k, y*11-l]
			sum = sum/121
			cell_y.append(sum)
		cell.append(cell_y)
	return cell

#fungsi buat ngubah cell jadi pixel
def openCell(cell):
	pixel = []
	for (x, y) in cell:
		for k in range(11):
			for l in range(11):
				pixel.append((x*11-k, y*11-l))
	return pixel

def getKawah(dem):
	max_point = dem.argmax()										#tinggi titik tertinggi
	max_point_tup = list(np.unravel_index(max_point, dem.shape))	#koordinat titik tertinggi

	max_point_tup[0] = max_point_tup[0] + 100
	kawah = []														#koordinat kawah

	#kawah merapi berdiameter 400m -> 50 pixel
	max_point_tup[0] = max_point_tup[0] - 25
	for i in range(6):
		kawah.append((max_point_tup[0], max_point_tup[1]))
		for j in range(1, (2*i)+1):
			kawah_point = (max_point_tup[0], max_point_tup[1]-j*5)
			kawah.append(kawah_point)
		max_point_tup[0] = max_point_tup[0] + 5
		max_point_tup[1] = max_point_tup[1] + 5
	
	max_point_tup[1] = max_point_tup[1] - 10
	for i in range(5):
		kawah.append((max_point_tup[0], max_point_tup[1]))
		for j in range(1, 9-(2*i)):
			kawah_point = (max_point_tup[0], max_point_tup[1]-j*5)
			kawah.append(kawah_point)
		max_point_tup[0] = max_point_tup[0] + 5
		max_point_tup[1] = max_point_tup[1] - 5

	return kawah

#fungsi CA
def som(dem, kawah, volume):
	max_point_tup = kawah									#koordinat kawah
	x_max = max_point_tup[0]
	y_max = max_point_tup[1]
	#print(kawah)
	flow = [] 												#variabel yang ngetrack jalur lava
	flow_now = dem[x_max, y_max]
	flow.append(max_point_tup)

	x = 0
	y = 0

	#ngitung iterasi
	i = volume//6561

	for n in range(i):
		flow_now = 9999

		#cek 3 piksel di atas
		for i in range(-1, 2):
			y_now = y_max - 1
			x_now = x_max - i
			flow_check = dem[x_now, y_now]

			#cek apakah sel yang diperiksa lebih rendah
			if flow_check<flow_now and dem[x_max, y_max]>flow_check:
				if n>2:
					if x_now!=flow[n-1][0] or y_now!=flow[n-1][1]:
						#print("a ", x_now, flow[n-1][0], y_now, flow[n-1][1])
						flow_now = flow_check
						x = x_now
						y = y_now
				else:
					flow_now = flow_check
					x = x_now
					y = y_now
		
		#cek piksel kiri dan kanan
		flow_check = dem[x_max-1, y_max]
		if flow_check<flow_now and dem[x_max, y_max]>flow_check:
				if n>2:
					if x_now!=flow[n-1][0] or y_now!=flow[n-1][1]:
						#print("b ", x_now, flow[n-1][0], y_now, flow[n-1][1])
						flow_now = flow_check
						x = x_now
						y = y_now
				else:
					flow_now = flow_check
					x = x_now
					y = y_now
		flow_check = dem[x_max+1, y_max]
		if flow_check<flow_now and dem[x_max, y_max]>flow_check:
				if n>2:
					if x_now!=flow[n-1][0] or y_now!=flow[n-1][1]:
						#print("b ", x_now, flow[n-1][0], y_now, flow[n-1][1])
						flow_now = flow_check
						x = x_now
						y = y_now
				else:
					flow_now = flow_check
					x = x_now
					y = y_now

		#cek 3 piksel di bawah
		for j in range(-1, 2):
			y_now = y_max + 1
			x_now = x_max - j
			flow_check = dem[x_now, y_now]

			if flow_check<flow_now and dem[x_max, y_max]>flow_check and (x!=x_max or y!=y_max):
				if n>2:
					if x_now!=flow[n-1][0] or y_now!=flow[n-1][1]:
						#print("c ", x_now, flow[n-1][0], y_now, flow[n-1][1])
						flow_now = flow_check
						x = x_now
						y = y_now
				else:
					#print("pass")
					flow_now = flow_check
					x = x_now
					y = y_now

		x_max = x
		y_max = y

		dem[x_max][y_max] = dem[x_max][y_max]+1

		flow.append((x_max, y_max))
		#print(x_max, y_max, dem[x_max][y_max])
	return flow

#-----------------------------MAIN PROGRAM---------------------------------#
#--------------------------------------------------------------------------#
def main(volume=10000000, viskositas=10000000):
	print("INITIALIZING")
	print(volume, viskositas)

	diy = Image.open('static/lava/DIY.tif')		#buka DEM
	diy_arr = np.array(diy)						#ubah DEM jadi array
	kawah = getKawah(diy_arr)					#data koordinat kawah

	#buka map buat ditampilin
	base_map = Image.open('static/lava/DIY_render.tif')

	for (x, y) in kawah:
		titik_kawah = (x, y)

		#Pixel -> cell -> CA -> pixel
		#cell = np.array(cellConverter(diy_arr))
		flow_cell = som(diy_arr, titik_kawah, volume)
		#flow = openCell(flow_cell)

		"""
		#bikin log file
		file_exist = os.path.exists('simulation\Static\lava\diy_arr.txt')
		if not file_exist:
			with open('flow.txt', 'w') as f:
				f.write(str(flow))
			with open('flow_cell.txt', 'w') as f:
				f.write(str(flow_cell))
		"""

		#ngewarnaiin jalur
		for (x, y) in flow_cell:
			base_map.putpixel((y, x), (255, 0, 0))

	#grid
	#buat figure
	my_dpi = 300
	fig = plt.figure(figsize=(float(base_map.size[0])/my_dpi,float(base_map.size[1])/my_dpi),dpi=my_dpi)
	ax = fig.add_subplot(111)

	#set interval
	myInterval=100.
	loc = plticker.MultipleLocator(base=myInterval)
	ax.xaxis.set_major_locator(loc)
	ax.yaxis.set_major_locator(loc)

	#tambah grid
	ax.grid(which='major', axis='both', linestyle='-')

	#tambah image
	ax.imshow(base_map)

	#save map
	base_map = base_map.convert("RGB")
	base_map.save("static/lava/DIY_result.jpg", 'JPEG')

	#base_map.show()
	return base_map
	
