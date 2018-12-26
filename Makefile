.SUFFIXES : .py .class

PY = python

.py.class:
	$(PY) $*.py

CLASSES = \
	webcraw.py \


default : classes

classes : $(CLASSES:.py=.class)
