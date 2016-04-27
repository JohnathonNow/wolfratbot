ENCRYPTION=openssl cast5-cbc 
ENCRYPT=$(ENCRYPTION) -e
DECRYPT=$(ENCRYPTION) -d

GIT_ADD=src/* Makefile README.md conf/*

push: 
	git add $(GIT_ADD)
	git commit
	git push

%.dtxt: %.etxt
	$(DECRYPT) -in $< -out $@ && rm $<

%.etxt: %.dtxt
	$(ENCRYPT) -in $< -out $@ && rm $<

restart: 
	sudo /etc/init.d/apache2 restart

