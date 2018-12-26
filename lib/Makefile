.SUFFIXES : .py .class

PY = python

.py.class:
	$(PY) $*.py

CLASSES = \
	getSoup_mdl.py \


default : classes

classes : $(CLASSES:.py=.class)
