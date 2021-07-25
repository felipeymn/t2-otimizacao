caminhada: caminhada.py
	printf '#!/usr/bin/env python3\n' >$@
	cat $< >> $@
	chmod +x $@
