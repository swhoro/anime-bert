replace:
	python replace.py ${dataname}

preprocess:
	cat ${dataname} | cut -d " " -f 1,4 > ${dataname}.txt
	python preprocess.py ${dataname}.txt

train:
	python train.py ${dataname}