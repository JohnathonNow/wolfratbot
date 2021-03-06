ENCRYPTION=openssl aes-256-cbc
ENCRYPT=$(ENCRYPTION) -e
DECRYPT=$(ENCRYPTION) -d

GIT_ADD=src/* Makefile README.md conf/* .gitignore

all:

decrypt: ./conf/conf.dtxt
encrypt: ./conf/conf.etxt

# Decrypt an encrypted file
%.dtxt: %.etxt
	$(DECRYPT) -in $< -out $@

# Encrypt a file and destroy the original
%.etxt: %.dtxt
	$(ENCRYPT) -in $< -out $@ && rm $<

# Because I am super lazy:
push: 
	git add -A $(GIT_ADD)
	git commit
	git push

restart: 
	sudo /etc/init.d/apache2 restart

test:
	python -B src/main.py

clean:
	find src -name *.pyc -exec rm '{}' \;

# vim: setlocal noexpandtab
