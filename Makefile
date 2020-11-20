# git helpers
GIT     := git
GITDIFF := $(GIT) diff
GITLOG  := $(GIT) log
GITPULL := $(GIT) pull
GITSTATUS := $(GIT) status

.PHONY: init test all

diff:
	$(GITDIFF)

init:
	python3 -mpip install --user -r requirements.txt

install:
	python3 ./setup.py develop --user

log:
	$(GITLOG)

pull:
	$(GITPULL)

pylinter:
	python3 ./pylinter.py

status:
	$(GITSTATUS)

test:
	python3 ./setup.py test

