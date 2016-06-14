from input_query.models import Hotel

a = open('list.txt', 'r')
src = a.read()
src = src.split("\n")
a.close()
src.pop()
for i in src:
	dir1 = './Collection/' + i
	t_dir1 = open(dir1, 'r')
	dir2 = './clip/' + str(i) + '.clip'
	t_dir2 = open(dir2, 'r')

	data1 = t_dir1.read()
	data1 = data1.split("\n")	

	data2 = t_dir2.read()
	if len(data1)==4:
		Hotel.objects.create(rating=data1[0], hotel_id=data1[1], name=data1[2], state=data1[3], comment=data2)

	t_dir1.close()
	t_dir2.close()
